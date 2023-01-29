# Flask Application using PostreSQL Template

## System Requirements (for mac os Monterey)
### PostgreSQL
For using a PostgreSQL database with flask, flask relies on the python package psycopg2. The latter needs a local installation of 
PostgreSQL and the path to the `pg_config` file must be given in the `PATH` environment variable.

```bash
export PATH=$PATH$:/Library/PostgreSQL/14/bin
```

## Getting Started
### Download the template
```bash
git clone https://github.com/benoitregamey/template-flask-postgreSQL.git
```

### Create a python virtual environment
```bash
cd template-flask-postgreSQL
python3 -m venv .venv
source .venv/bin/activate
```

### Install dependencies
```bash
pip3 install -r requirements.txt
```

### Set up postgreSQL database connection
Create a .env file at the root of the directory and fill it with DB connection information
```bash
POSTGRES_HOST="localhost"
POSTGRES_PORT="5432"
POSTGRES_DB="db-name"
POSTGRES_USER="username"
POSTGRES_PASSWORD="password"
```

### Run the app
```bash
python3 app.py
```
Visit `localhost:5000`

### Fill the DB table with dummy records
```bash
python3 add_dummy_db_records.py
```
