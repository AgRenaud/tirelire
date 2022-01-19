class TransactionNotFoundError(Exception):
    message = "The transaction you spcecified does not exist."

    def __str__(self):
        return TransactionNotFoundError.message


class TransactionsNotFoundError(Exception):
    message = "No transactions were found."

    def __str__(self):
        return TransactionsNotFoundError.message
