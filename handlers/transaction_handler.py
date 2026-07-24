from services.transaction_service import TransactionService


def create_transaction(data):
    return TransactionService.create_transaction(
        template_id=data["template_id"],
        entries=data["entries"],
        project_id=data.get("project_id"),
        person_id=data.get("person_id"),
        note=data.get("note", "")
    )


def get_transactions():
    return TransactionService.get_transactions()


def get_transaction(transaction_id):
    return TransactionService.get_transaction(transaction_id)


def delete_transaction(transaction_id):
    return TransactionService.delete_transaction(transaction_id)
