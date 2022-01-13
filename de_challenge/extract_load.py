import json
import psycopg2
import requests
import pandas as pd
from sqlalchemy import create_engine

# connect to database
engine = create_engine('postgresql+psycopg2://mlevisrossi:mlevisrossi@localhost:5432/postgres')
connection = engine.raw_connection()

# create a cursor
cur = connection.cursor()

# read sql file
f = open('DDL_incidents.sql', 'r')
sql_create = f.read()
f.close()

# execute create table statement
cur.execute(sql_create)

# data extraction from API and creation of pandas dataframe
URL = 'https://data.sfgov.org/resource/wr8u-xric.json'
df = pd.read_json(URL)

# replace point type for text
df['point'] = str(df['point'])

# insert in database
connection.commit()
df.to_sql('incidents', engine, schema='public', if_exists='replace', index=False)
connection.commit()

#close connection
cur.close()
connection.close()