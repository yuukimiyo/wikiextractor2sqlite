# -*- coding:utf-8 -*-
""" This script creates a wikipedia db in SQLite from wikiextractor's jsonfile. 
"""

import sys
import os
import argparse
import logging
import glob
import sqlite3
import json
import codecs
from tqdm import tqdm
from contextlib import closing

# Define Log settings
# LOG_LINE_FM = '%(asctime)s(%(levelname)s) %(name)s: %(message)s'
LOG_LINE_FM = '%(asctime)s(%(levelname)s): %(message)s'
LOG_DATE_FM = '%H:%M:%S'
LOG_LEVEL = logging.INFO

# Defines
DB_NAME = './wikipedia.db'
TABLE_NAME = 'pages'

# SQL
CREATE_PAGES_TBL = '''
CREATE TABLE IF NOT EXISTS `{}` (
    `id` bigint PRIMARY KEY,
    `url` varchar(512),
    `title` varchar(1024),
    `text` text
);
'''.format(TABLE_NAME)

INSERT_PAGES_TBL = '''
INSERT INTO `{}` (
    `id`,
    `url`,
    `title`,
    `text`
) values (
    ?,
    ?,
    ?,
    ?
);
'''.format(TABLE_NAME)


def json_to_sqlite(log, input_dir, dbname):
    """ insert pages data to sqlite.
    """

    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()

        # Create table if not exists.
        c.execute(CREATE_PAGES_TBL)

        count = 0
        count_error = 0
        for file in tqdm(glob.glob("{}/[A-Z][A-Z]/*".format(input_dir))):
            with codecs.open(file, 'r', 'utf-8') as f:
                insert_datas = []
                for l in f:
                    try:
                        j = json.loads(l)
                        insert_datas.append((j['id'], j["url"], j["title"], j["text"]))
                        count += 1
                    except json.decoder.JSONDecodeError as e:
                        log.warning("JSON Decord error : {}".format(l[0:30]))
                        count_error += 1
                c.executemany(INSERT_PAGES_TBL, insert_datas)
                conn.commit()

        log.info("insert {} records! / {} error..".format(count, count_error))

def drop_table_if_exists(log, dbname):
    """ Drop table.
    """
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()

        result = c.execute("DROP TABLE IF EXISTS `{}`;".format(TABLE_NAME))
        log.info(result.fetchall())


def check_table(log, dbname, n=1):
    """ show n records to check.
    """
    with closing(sqlite3.connect(dbname)) as conn:
        c = conn.cursor()

        result = c.execute("SELECT count(*) FROM `{}`;".format(TABLE_NAME))
        log.info("count({}): {}".format(TABLE_NAME, result.fetchall()[0][0]))

        for row in c.execute("SELECT * FROM `{}` limit {};".format(TABLE_NAME, n)):
            log.info(row)


if __name__ == '__main__':

    # Setup Argparse.
    parser = argparse.ArgumentParser(description="Create sqlite db from wikiextractor's jsonfile.")
    parser.add_argument("input_dir", help="Input dir that contain json dirs by wikiextractor.")
    parser.add_argument("-o", "--output", default=DB_NAME, help="Output sqlitefile.")
    parser.add_argument("-d", "--drop", default=True, help="Drop table if exists.")
    parser.add_argument("-q", "--quiet", default=False, action='store_true', help="No message without errors.")
    args = parser.parse_args()

    # Setup Logger
    if not args.quiet:
        logging.basicConfig(level=LOG_LEVEL, format=LOG_LINE_FM, datefmt=LOG_DATE_FM)
    else:
        logging.basicConfig(level=logging.ERROR, format=LOG_LINE_FM, datefmt=LOG_DATE_FM)
    log = logging.getLogger(__name__)

    # Exit if input dir not fount.
    if not os.path.isdir(args.input_dir):
        log.error("Input dir not found. ({})".format(args.input_dir))
        sys.exit(1)

    # Drop table if exists.
    if args.drop:
        drop_table_if_exists(log, args.output);

    # exec insert
    json_to_sqlite(log, args.input_dir, args.output)
