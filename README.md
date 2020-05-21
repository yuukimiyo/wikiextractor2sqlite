# wikiextractor2sqlite

Make SQLite DB from wikiextractor's jsonfile.

Many thanks!<br />
[wikiextractor](https://github.com/attardi/wikiextractor)

# Install

```
git clone https://github.com/yuukimiyo/wikiextractor2sqlite.git
pip install tqdm
```

# Usage

```
python wikiextractor2sqlite.py <extracted dir> [-o <name of sqlite db>] [-d] [-q] [-h]

extracted dir:
    extracted dir by wikiextractor.
	required

[-o | --output]:
    name of sqlite db.
    default: wikipedia.db

[-d | --drop]:
    drop table if exists in sqlite db.
    default: True

[-q | --quiet]:
    quiet mode. no message without errors. 
    default: False

[-h | --help]:
	Show help.

e.g.
python ./wikiextractor2sqlite/wikiextractor2sqlite.py ./extracted -o wikipedia.db

```

# Example Usage

```
# Download Wiki dump.
wget https://dumps.wikimedia.org/jawiki/latest/jawiki-latest-pages-articles.xml.bz2

# Download wikiextractor
git clone https://github.com/attardi/wikiextractor

# Extract Wiki data.
./wikiextractor/WikiExtractor.py --json -q -o extracted jawiki-latest-pages-articles.xml.bz2

# Download wikiextractor2sqlite
git clone https://github.com/yuukimiyo/wikiextractor2sqlite.git

# Install Requiments.
pip install tqdm

# Create wikipedia.db
python ./wikiextractor2sqlite/wikiextractor2sqlite.py ./extracted -o wikipedia.db

# Check db data
(install sqlite3 if not installed. e.g.> apt install sqlite3)
sqlite3 wikipedia.db "select count(*) from pages;"

```

# License

BSD 3-Clause "New" or "Revised" License
