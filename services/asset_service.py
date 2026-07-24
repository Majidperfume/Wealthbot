from models.asset import Asset


class AssetService:

    @staticmethod
    def create_asset(name, asset_type_id, currency_id, note=""):
        return Asset.create(
            name=name,
            asset_type_id=asset_type_id,
            currency_id=currency_id,
            note=note,
        )


    @staticmethod
    def get_assets():
        return Asset.all()


    @staticmethod
    def get_asset(asset_id):
        return Asset.get(asset_id)


    @staticmethod
    def update_asset(
        asset_id,
        name,
        asset_type_id,
        currency_id,
        note=""
    ):
        return Asset.update(
            asset_id,
            name,
            asset_type_id,
            currency_id,
            note,
        )


    @staticmethod
    def remove_asset(asset_id):
        return Asset.delete(asset_id)
