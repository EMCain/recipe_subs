#!/usr/bin/env bash

cd /var/app

# Since this is running multiple processes, 
# run the first process in the background so
# that the second process is launched.
python app/task_queue/scheduler.py & 
python app/task_queue/worker.py
