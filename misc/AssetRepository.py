warehouse.assets
factory.assets_owned
factory.assets_held

class AssetRepository(ABC):

    def find_by_owner(self, owner):
        ...

    def find_by_holder(self, holder):
        ...

    def find_by_location(self, location):
        ...

    def get(self, asset_id):
        ...

    def save(self, asset):
        ...