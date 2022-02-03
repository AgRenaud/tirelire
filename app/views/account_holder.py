from app.service_layer.unit_of_work import AbstractAccountHolderUnitOfWork


def get_account_holder_by_id(id: str, uow: AbstractAccountHolderUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM account_holders WHERE id = :id
            """,
            dict(id=id),
        )
    return [dict(r) for r in results][0]

def get_accounts_of_account_holder(account_holder_id: str, uow: AbstractAccountHolderUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM accounts WHERE account_holder_id = :account_holder_id
            """,
            dict(account_holder_id=account_holder_id),
        )
    return [dict(r) for r in results]

def get_account_by_id(account_holder_id: str, account_id: str, uow: AbstractAccountHolderUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM accounts 
            WHERE 
                account_holder_id = :account_holder_id AND
                id = :account_id
            """,
            dict(
                account_holder_id=account_holder_id, 
                account_id=account_id),
        )
    return [dict(r) for r in results][0]

def get_operations_from_account(account_holder_id: str, account_id: str, uow: AbstractAccountHolderUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM operations o
            JOIN accounts a ON o.account_id = a.id
            JOIN account_holders h ON a.account_holder_id = h.id
            WHERE 
                account_holder_id = :account_holder_id AND
                id = :account_id
            """,
            dict(
                account_holder_id=account_holder_id, 
                account_id=account_id),
        )
    return [dict(r) for r in results]