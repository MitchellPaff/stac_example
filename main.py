from pystac.catalog import Catalog, CatalogType
from pystac import read_file

from pathlib import Path


parent_catalog = Catalog.from_file("example/catalog.json")

child_catalog = read_file(f"example/catalog_1/catalog.json")
parent_catalog.add_child(child=child_catalog)

path = str(Path(__file__).parent.absolute().joinpath("example"))
parent_catalog.normalize_hrefs(path)
parent_catalog.save(catalog_type=CatalogType.SELF_CONTAINED)
