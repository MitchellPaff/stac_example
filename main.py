from pystac.catalog import Catalog, CatalogType
from pystac.collection import Collection
from pystac.item import Item
from pystac.layout import HrefLayoutStrategy
from pystac import read_file

from pathlib import Path


class GeostoreSTACLayoutStrategy(HrefLayoutStrategy):
    def get_catalog_href(self, cat: Catalog, parent_dir: str, is_root: bool) -> str:
        return str(cat.get_self_href())

    def get_collection_href(
        self, col: Collection, parent_dir: str, is_root: bool
    ) -> str:
        assert not is_root
        return str(col.get_self_href())

    def get_item_href(self, item: Item, parent_dir: str) -> str:
        return str(item.get_self_href())


parent_catalog = Catalog.from_file("example/parent_catalog.json")

child_catalog = read_file(f"example/test_dataset_1/catalog.json")
parent_catalog.add_child(child=child_catalog, strategy=GeostoreSTACLayoutStrategy())

path = str(Path(__file__).parent.absolute().joinpath("example"))
parent_catalog.normalize_hrefs(path, strategy=GeostoreSTACLayoutStrategy())
parent_catalog.save(catalog_type=CatalogType.SELF_CONTAINED)
