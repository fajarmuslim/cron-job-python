# cron-job-python

In this repo, we are going to feed data into PostgreSQL, retrieve that data, doing labeling, and then return it back into db

## How to use this Repo

### Prerequisite
1. This repo is inseparable with `https://github.com/fajarmuslim/postgres-alembic-migration`. So, you may follow instruction there to setup the db
2. Install poetry
```bash
pip3 install poetry
```

### How to run
1. Create virtual environment for python
```bash
python3 -m venv venv
```
2. Change directory into `app`
```bash
cd app
```
3. Create `.env` file, the example can be found on `.env-example` file. Make sure that you have same variable with your actual postgres db 
4. Install all the python package dependency
```bash
poetry install
```
5. Feed the data first
```bash
python3 feed_data.py
```
6. Run the scheduler job to retrieve data, doing labeling on that data, and return the label into db on another table
```bash
python3 label_data.py
```
