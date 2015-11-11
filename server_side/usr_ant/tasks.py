from celery.decorators import task, periodic_task
from celery.task.schedules import crontab
from datetime import timedelta
from celery.utils.log import get_task_logger
from time import sleep
import django
import socket
from broadcastHelper.helper import get_data, debug_func, begin_broadcast
import json

@task(name = "malicious_loop")
def malicious_loop(time):
    print 'entered '
    for count in range(1, 10):
        sleep(time)
        print "10s passed " + "haha x " + str(count)
    return

# @periodic_task(run_every = (timedelta(seconds = 10)),
#                 name = "malicious_periodic")
@task(name = "malicious_periodic")
def malicious_periodic():
    print "wow This is malicious"
    return

@task(name = "udp_broadcast")
def udp_broadcast(): #default udp port is 5005
    begin_broadcast()

    return
