import json
import os
import psycopg2
import requests
import pandas as pd

def extract_from_api():
    headers = requests.utils.default_headers()
    response = requests.get(
        'https://data.sfgov.org/resource/wr8u-xric.json',
        headers=headers,
        verify=False
    )

    if response.status_code == 200:
        incidents = json.load(response.text)
        connect(incidents)

def connect(data_incidents):
    connection = psycopg2.connect("dbname=postgres user=mlevisrossi password=mlevisrossi")

    # create a cursor
    cur = connection.cursor()

    # read sql file
    f = open('incidents_ddl.sql', 'r')
    sqlFile = f.read()
    f.close()
    cur.execute(sqlFile)

    data_incidents.to_sql('', connection, if_exists='append', index=False)
    # query_sql = "insert into json_table select * from json_populate_recordset(NULL::json_table, %s) "
    # cur.execute(query_sql, (json.dumps(incidents),))
    cur.close()
    connection.close()

