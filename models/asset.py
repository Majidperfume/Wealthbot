from database.database import db


class Asset:

    @staticmethod
    def create(name, asset_type, currency_id):
        db.execute(
            """
            INSERT INTO assets
            (name, asset_type, currency_id)
            VALUES (?, ?, ?)
            """,
            (name, asset_type, currency_id),
        )

    @staticmethod
    def all():
        return db.fetchall(
            """
            SELECT *
            FROM assets
            WHERE active = 1
            ORDER BY name
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
    def update(asset_id, name, asset_type, currency_id):
        db.execute(
            """
            UPDATE assets
            SET
                name = ?,
                asset_type = ?,
                currency_id = ?
            WHERE id = ?
            """,
            (name, asset_type, currency_id, asset_id),
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
