## Project
Project contains 3 services:
- server - for making conversions at endpoint `0.0.0.0:8002/convert`
- db - postgres database with examples
- redis - redis server, where they are stored converted tables from postgres

### Run
`make run`

### Stop
`make stop`

### How to convert table from example db from this repository?
Put postgres config data (database, table, user, password, host, port) into GET request, like that:

`0.0.0.0:8002/convert?database=postgres&table=users&user=postgres&password=postgres&host=db&port=5432`

### How to convert table from external db?
`0.0.0.0:8002/convert?database=DATABASE_NAME&table=TABLE_NAME&user=USER_NAME&password=PASSWORD&host=DATABASE_HOST&port=DATABASE_PORT`

### Postgres with examples
configs
- database: postgres
- table: users or employees
- user: postgres
- password: postgres
- host: db
- port: 5432
