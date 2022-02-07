from app.service_layer.unit_of_work import AbstractHolderUnitOfWork


def get_account_by_id(account_id: str, uow: AbstractHolderUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM accounts WHERE id = :account_id
            """,
            dict(account_id=account_id),
        )
    return [dict(r) for r in results][0]

def get_account_operations(account_id: str, uow: AbstractHolderUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM operations WHERE account_id = :account_id
            """,
            dict(account_id=account_id),
        )
    return [dict(r) for r in results]

def get_account_category_operations(account_id: str, category: str, uow: AbstractHolderUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM operations WHERE account_id = :account_id AND category = :category
            """,
            dict(account_id=account_id, category=category),
        )
    return [dict(r) for r in results]