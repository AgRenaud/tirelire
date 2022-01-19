class AccountNotFoundError(Exception):
    message = "The account you spcecified does not exist."

    def __str__(self):
        return AccountNotFoundError.message


class AccountsNotFoundError(Exception):
    message = "No accounts were found."

    def __str__(self):
        return AccountsNotFoundError.message
