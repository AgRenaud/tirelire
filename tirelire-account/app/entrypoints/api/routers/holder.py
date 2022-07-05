from fastapi import APIRouter, Depends
from uuid import uuid4

from app import views
from app.domain import commands
from app.entrypoints.api.schemas import input
from app.adapters.event_publisher import RedisConnector
from app.service_layer.messagebus import MessageBus
from app.service_layer.factory import SQL_ALCHEMY_UOW_FACTORY, REDIS_FACTORY
from app.bootstrap import bootstrap


router = APIRouter(prefix="/holders", tags=["holders"])

async def get_event_publisher():
    r = REDIS_FACTORY()
    r = RedisConnector(r)
    return r.publish

async def get_message_bus():
    return bootstrap(uow=SQL_ALCHEMY_UOW_FACTORY(), publish=await get_event_publisher())

def create_id():
    return str(uuid4())


@router.post("/")
def add_holder(bus: MessageBus=Depends(get_message_bus)):
    new_id = create_id()
    cmd = commands.CreateHolder(new_id)
    bus.handle(cmd)
    return {"holder_id": new_id}


@router.get("/{holder_id}")
async def get_holder_by_id(holder_id: str, uow=Depends(SQL_ALCHEMY_UOW_FACTORY)):
    return views.holder.get_holder_by_id(holder_id, uow)


@router.post("/{holder_id}/accounts")
async def add_account_to_holder(holder_id: str, input: input.AddAccount, bus: MessageBus=Depends(get_message_bus)):
    new_id = create_id()
    cmd = commands.CreateAccount(holder_id, new_id, input.currency)
    bus.handle(cmd)
    return {"holder_id": holder_id, "account_id": new_id, "currency": input.currency}


@router.get("/{holder_id}/accounts")
async def get_all_accounts_of_holder(holder_id: str, uow=Depends(SQL_ALCHEMY_UOW_FACTORY)):
    return views.holder.get_accounts_of_holder(holder_id, uow)


@router.get("/{holder_id}/accounts/{account_id}")
async def get_account_by_id(holder_id: str, account_id: str, uow=Depends(SQL_ALCHEMY_UOW_FACTORY)):
    return views.holder.get_account_by_id(holder_id, account_id, uow)


@router.post("/{holder_id}/accounts/{account_id}/operations")
async def add_operations_to_an_account(
    holder_id: str,
    account_id: str,
    input: input.AddOperations,
    bus: MessageBus=Depends(get_message_bus),
):
    cmds = []
    for operation in input.operations:
        new_cmd = commands.AddOperation(
            operation.name,
            operation.date,
            operation.value,
            operation.currency,
            operation.category,
        )
        cmds.append(new_cmd)
    cmd = commands.AddOperations(holder_id, account_id, cmds)
    bus.handle(cmd)
    return {
        "holder_id": holder_id,
        "account_id": account_id,
        "operations_added": len(cmds),
    }
