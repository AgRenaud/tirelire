import pytest

from app.domain.model import Holder, Account, Currency


def test_create_new_holder_and_add_operations():
    new_holder = Holder("str_id", [])
    assert isinstance(new_holder, Holder)

    new_account_1 = Account("id_account_1", Currency.EUR, [])
    new_account_2 = Account("id_account_2", Currency.USD, [])
    new_holder.create_account(new_account_1)
    new_holder.create_account(new_account_2)

    assert len(new_holder.accounts) == 2
    assert new_holder.get_account_by_id("id_account_1") == new_account_1
    assert new_holder.get_account_by_id("id_account_2") == new_account_2

