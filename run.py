#!/usr/bin/env python
import os

def get_worker_number():
    # Rumus jumalah pekerja = (2 x $num_cores) + 1
    return (os.cpu_count() * 2) + 1

PORT = 8080
HOST = "0.0.0.0"
PRODUCTION_MODE = True
PYTHON_INTERPRETER_PATH = "../venv/bin/python3.11"
PRODUCTION_COMMAND=f"export ANONYMIZED_TELEMETRY=False & {PYTHON_INTERPRETER_PATH} -m gunicorn app.main:app --timeout 120 --workers {get_worker_number()} --worker-class uvicorn.workers.UvicornWorker --bind {HOST}:{PORT}"
DEVELOPMENT_COMMAND=f"export ANONYMIZED_TELEMETRY=False & {PYTHON_INTERPRETER_PATH} -m uvicorn app.main:app --reload --host={HOST} --port={PORT}"

def run_production():
    os.system(PRODUCTION_COMMAND)

def run_development():
    os.system(DEVELOPMENT_COMMAND)


def main():
    if PRODUCTION_MODE:
        run_production()
    else:
        run_development()

if __name__ == "__main__":
    main()