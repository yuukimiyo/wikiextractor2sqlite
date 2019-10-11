# wikiextractor2sqlite

This script creates a wikipedia db in SQLite from wikiextractor's jsonfile.

Many thanks!<br />
[wikiextractor](https://github.com/attardi/wikiextractor)

# Install

```
git clone https://github.com/yuukimiyo/wikiextractor2sqlite.git
pip install tqdm
```

# Usage

```
python wikiextractor2sqlite.py <extracted dir> [-o <name of sqlite db>] [-d] [-h]

extracted dir:
    extracted dir by wikiextractor.
	required

[-o | --output]:
    name of sqlite db.
    default: wikipedia.db

[-d | --drop]:
    drop table if exists in sqlite db.
    default: True

e.g.
python wikiextractor2sqlite/wikiextractor2sqlite.py ./extracted -o wikipedia.db

```

# License

BSD 3-Clause "New" or "Revised" License
