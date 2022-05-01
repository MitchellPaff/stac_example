# Setup

- `python3 -m venv .venv`
- `. .venv/bin/activate`
- `pip install -r requirements.txt`
- `python3 main.py`


After the script has been run, pystac will have modified the json and added the child catalog to the parent catalog.
There seems to be an issue with asset href's contained in an Item.
