#!/usr/bin/env bash

cd /var/app

echo "running tasks-start"
ls
pwd
python app/task_queue/print_review.py

#exec python task_queue/run_scheduler.py
#exec python task_queue/run_worker.py