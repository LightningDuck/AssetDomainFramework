class AssetService:

    def transfer_ownership(self, asset, new_owner):
        asset.owner = new_owner

    def loan(self, asset, borrower):
        asset.holder = borrower

    def return_asset(self, asset):
        asset.holder = asset.owner

    def move(self, asset, new_location):
        asset.location = new_location