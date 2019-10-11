# wikiextractor2sqlite

This script creates a sqlite db from wikiextractor's jsonfile.

[wikiextractor](https://github.com/attardi/wikiextractor)

# Install
git clone https://github.com/yuukimiyo/wikiextractor2sqlite.git
pip install tqdm

# Usage

```
python wikiextractor2sqlite.py <extracted dir by wikiextractor> [-o <name of sqlite db>] [-d]
```

-o: name of sqlite db.
-d: drop table in sqlite.

# License

BSD 3-Clause "New" or "Revised" License
