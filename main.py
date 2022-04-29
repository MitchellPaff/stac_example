from pystac.catalog import Catalog, CatalogType
from pystac.collection import Collection
from pystac.item import Item
from pystac.layout import HrefLayoutStrategy
from pystac import read_file

class GeostoreSTACLayoutStrategy(HrefLayoutStrategy):
    def get_catalog_href(self, cat: Catalog, parent_dir: str, is_root: bool) -> str:
        return str(cat.get_self_href())

    def get_collection_href(self, col: Collection, parent_dir: str, is_root: bool) -> str:
        assert not is_root
        return str(col.get_self_href())

    def get_item_href(self, item: Item, parent_dir: str) -> str:
        return str(item.get_self_href())

"""Handle writing a new dataset version to the dataset catalog"""



root_catalog = Catalog.from_file(
    "parent_catalog.json"
)

dataset_version_metadata = read_file(f"test_dataset_1/catalog.json")
dataset_catalog.add_child(child=dataset_version_metadata, strategy=GeostoreSTACLayoutStrategy())

dataset_catalog.normalize_hrefs(
    f"{storage_bucket_path}/{dataset_prefix}", strategy=GeostoreSTACLayoutStrategy()
)
dataset_catalog.save(catalog_type=CatalogType.SELF_CONTAINED)
