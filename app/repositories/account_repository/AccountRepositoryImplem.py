from app.domain import Account


class AccountRepositoryImplem:
    def __init__(self, session):
        self.session = session

    def add(self, account):
        self.session.add(account)
        self.session.commit()

    def get(self, id: str):
        return self.session.query(Account).filter_by(id=id).one()

    def list(self):
        return self.session.query(Account).all()
