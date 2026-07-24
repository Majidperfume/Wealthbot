from models.transaction import (
    create_transaction,
    add_transaction_entry
)


def create_financial_transaction(
    transaction_type_id,
    description,
    transaction_date,
    entries,
    category_id=None,
    person_id=None
):
    """
    Creates a transaction with multiple financial effects.

    entries example:

    [
        {
            "account_id": 1,
            "currency_id": 1,
            "amount": -46000000,
            "entry_type": "debit"
        },
        {
            "currency_id": 2,
            "amount": 500,
            "entry_type": "credit"
        }
    ]
    """

    create_transaction(
        transaction_type_id,
        description,
        transaction_date,
        category_id,
        person_id
    )


    # get last inserted transaction id
    from models.database import execute_one

    result = execute_one(
        """
        SELECT id
        FROM transactions
        ORDER BY id DESC
        LIMIT 1
        """
    )

    transaction_id = result["id"]


    for entry in entries:

        add_transaction_entry(
            transaction_id=transaction_id,
            account_id=entry.get("account_id"),
            currency_id=entry.get("currency_id"),
            person_id=entry.get("person_id"),
            amount=entry.get("amount"),
            entry_type=entry.get("entry_type"),
            note=entry.get("note", "")
        )


    return transaction_id
