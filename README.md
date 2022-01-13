# Requirements
## 1. Instalation
- Python 3.8
- Docker

## 2. Clone repository
`git clone https://github.com/mlevisrossi/data_engineer_challenge.git`
  
## 3. Run the following commands inside the project directory:
- `pip install requests`
- `pip install psycopg2`
- `pip install dbt-postgres`
- `pip install pandas`
- `pip install sqlalchemy`
- `dbt init`

## 3. Modify the profiles.yml file
The file usually will be placed in _C:\Users\{Username}\\.dbt\profiles.yml_.

Replace the content of the file with the following code:

`de_challenge:
  outputs:
    dev:
      type: postgres
      threads: 10
      host: 127.0.0.1
      port: 5432
      user: mlevisrossi
      pass: mlevisrossi
      dbname: postgres
      schema: bi_warehouse
  target: dev`

# Execution
Run:
- `docker compose up`
  It will initialize a postgres database service in a docker container.
- `extract.py`
  Executes the script that extracts the fire incidents data from the API and ingests the data into the incidents table in the public schema.
- `dbt run`
Creates the data model
  
# Testing
Connect to the postgres database and run the queries.
Database connection info:
- host: 127.0.0.1
- port: 5432
- user: mlevisrossi
- pass: mlevisrossi

# Assumptions
- The generated data model consists in 4 tables:
  - bi_warehouse.incidents_by_batallion: Total incidents by battalion. It aggregates the incidents along the battalion dimension.
  - bi_warehouse.incidents_by_district: Total incidents by district. It aggregates the incidents along the district dimension.
  - bi_warehouse.incidents_by_time_period: Total incidents by time period. It aggregates the incidents along the district time period.
  - bi_warehouse.incidents_by_timeperiod_district_battalion: Total incidents by battalion, district and time period.It aggregates the incidents along the time period, district and battalion dimension.
- The process will be scheduled to run everyday using cron.
- For each execution, the incidents table will be created and all the data from the API will be ingested.
