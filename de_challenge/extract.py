import json
import psycopg2
import requests

def extract_from_api():
    headers = requests.utils.default_headers()
    response = requests.get(
        'https://data.sfgov.org/resource/wr8u-xric.json',
        headers=headers,
        verify=False
    )

    if response.status_code == 200:
        data_incidents = json.loads(response.text)
        connect(data_incidents)

def connect(data_incidents):
    connection = psycopg2.connect("dbname=postgres user=mlevisrossi password=mlevisrossi")

    # create a cursor
    cur = connection.cursor()

    # read sql file
    f = open('incidents_ddl.sql', 'r')
    sql_create = f.read()
    f.close()
    # execute create table statement
    cur.execute(sql_create)

    first_record = data_incidents[0]
    columns = list(first_record.keys())
    sql_insert = 'INSERT INTO {} '.format('incidents')
    sql_insert += "(" + ', '.join(columns) + ")\nVALUES "
    # insert incidents data into incidents table
    cur.execute(sql_insert)

    #close connection
    cur.close()
    connection.close()