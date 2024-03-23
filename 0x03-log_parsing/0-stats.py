#!/usr/bin/python3


"""
log parsing
"""

import random
import sys
import datetime
import time


def generate_random_ip():
    return ".".join(str(random.randint(1, 255)) for _ in range(4))


def generate_random_status_code():
    return random.choice([200, 301, 400, 401, 403, 404, 405, 500])


def generate_log_entry():
    ip_address = generate_random_ip()
    current_time = datetime.datetime.now()
    status_code = generate_random_status_code()
    random_number = random.randint(1, 1024)
    return f"{ip_address} - [{current_time}] \"GET /projects/260 HTTP/1.1\" {status_code} {random_number}\n"


for i in range(10000):
    time.sleep(random.random())
    log_entry = generate_log_entry()
    sys.stdout.write(log_entry)
    sys.stdout.flush()
