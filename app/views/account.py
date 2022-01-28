from app.service.unit_of_work import AccountUnitOfWork


def get_account_by_id(account_id: str, uow: AccountUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM accounts WHERE id = :account_id
            """,
            dict(account_id=account_id),
        )
    return [dict(r) for r in results][0]

def get_account_transactions(account_id: str, uow: AccountUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM transactions WHERE account_id = :account_id
            """,
            dict(account_id=account_id),
        )
    return [dict(r) for r in results]

def get_account_category_transactions(account_id: str, category: str, uow: AccountUnitOfWork):
    with uow:
        results = uow.session.execute(
            """
            SELECT * FROM transactions WHERE account_id = :account_id AND category = :category
            """,
            dict(account_id=account_id, category=category),
        )
    return [dict(r) for r in results]