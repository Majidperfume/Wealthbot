from services.asset_service import AssetService


def add_asset(data):
    return AssetService.create_asset(
        name=data["name"],
        asset_type_id=data["asset_type_id"],
        currency_id=data["currency_id"],
        note=data.get("note", "")
    )


def get_assets():
    return AssetService.get_assets()


def get_asset(asset_id):
    return AssetService.get_asset(asset_id)


def update_asset(data):
    return AssetService.update_asset(
        asset_id=data["id"],
        name=data["name"],
        asset_type_id=data["asset_type_id"],
        currency_id=data["currency_id"],
        note=data.get("note", "")
    )


def delete_asset(asset_id):
    return AssetService.remove_asset(asset_id)
