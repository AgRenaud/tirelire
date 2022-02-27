from app.service_layer.unit_of_work import AbstractUnitOfWork


def get_holder_by_id(id: str, uow: AbstractUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM holders WHERE id = :id
            """,
            dict(id=id),
        )
    return [dict(r) for r in results][0]


def get_accounts_of_holder(holder_id: str, uow: AbstractUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM accounts WHERE holder_id = :holder_id
            """,
            dict(holder_id=holder_id),
        )
    return [dict(r) for r in results]


def get_account_by_id(holder_id: str, account_id: str, uow: AbstractUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM accounts 
            WHERE 
                holder_id = :holder_id AND
                id = :account_id
            """,
            dict(holder_id=holder_id, account_id=account_id),
        )
    return [dict(r) for r in results][0]


def get_operations_from_account(
    holder_id: str, account_id: str, uow: AbstractUnitOfWork
):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM operations o
            JOIN accounts a ON o.account_id = a.id
            JOIN holders h ON a.holder_id = h.id
            WHERE 
                holder_id = :holder_id AND
                id = :account_id
            """,
            dict(holder_id=holder_id, account_id=account_id),
        )
    return [dict(r) for r in results]
