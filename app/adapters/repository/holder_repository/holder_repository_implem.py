from sqlalchemy.orm import Session
from typing import List

from app.domain.model import Holder


class HolderRepositoryImplem:
    def __init__(self, session):
        self.session: Session = session
        self.seen = set()

    def add(self, holder: Holder) -> None:
        self.session.add(holder)

    def get(self, id: str) -> Holder:
        holder = self.session.query(Holder).filter_by(id=id).one()
        if holder:
            self.seen.add(holder)
        return holder

    def list(self) -> List[Holder]:
        return self.session.query(Holder).all()
