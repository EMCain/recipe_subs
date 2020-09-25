#!/usr/bin/env bash

cd /var/app

#python app/task_queue/print_review.py
python app/task_queue/scheduler.py
python app/task_queue/worker.py
