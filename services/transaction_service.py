from models.transaction import Transaction


class TransactionService:

    @staticmethod
    def create_transaction(
        template_id,
        entries,
        project_id=None,
        person_id=None,
        note=""
    ):
        transaction_id = Transaction.create(
            template_id=template_id,
            project_id=project_id,
            person_id=person_id,
            note=note,
        )

        for entry in entries:
            Transaction.add_entry(
                transaction_id=transaction_id,
                asset_id=entry["asset_id"],
                amount=entry["amount"],
            )

        return transaction_id


    @staticmethod
    def get_transactions():
        return Transaction.all()


    @staticmethod
    def get_transaction(transaction_id):
        return {
            "transaction": Transaction.get(transaction_id),
            "entries": Transaction.entries(transaction_id),
        }


    @staticmethod
    def delete_transaction(transaction_id):
        return Transaction.delete(transaction_id)
