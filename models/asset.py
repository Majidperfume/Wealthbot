from database.database import db


class Asset:

    @staticmethod
    def create(name, asset_type_id, currency_id, note=""):
        db.execute(
            """
            INSERT INTO assets
            (name, asset_type_id, currency_id, note)
            VALUES (?, ?, ?, ?)
            """,
            (name, asset_type_id, currency_id, note),
        )


    @staticmethod
    def all():
        return db.fetchall(
            """
            SELECT
                assets.id,
                assets.name,
                asset_types.name AS type,
                currencies.code AS currency,
                assets.note
            FROM assets

            JOIN asset_types
            ON assets.asset_type_id = asset_types.id

            JOIN currencies
            ON assets.currency_id = currencies.id

            WHERE assets.active = 1

            ORDER BY assets.id
            """
        )


    @staticmethod
    def get(asset_id):
        return db.fetchone(
            """
            SELECT *
            FROM assets
            WHERE id = ?
            """,
            (asset_id,),
        )


    @staticmethod
    def update(asset_id, name, asset_type_id, currency_id, note=""):
        db.execute(
            """
            UPDATE assets

            SET
                name = ?,
                asset_type_id = ?,
                currency_id = ?,
                note = ?

            WHERE id = ?
            """,
            (
                name,
                asset_type_id,
                currency_id,
                note,
                asset_id,
            ),
        )


    @staticmethod
    def delete(asset_id):
        db.execute(
            """
            UPDATE assets

            SET active = 0

            WHERE id = ?
            """,
            (asset_id,),
        )
