#!/usr/bin/python3

import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())

    ip_part1 = random.randint(1, 255)
    ip_part2 = random.randint(1, 255)
    ip_part3 = random.randint(1, 255)
    ip_part4 = random.randint(1, 255)

    timestamp = datetime.datetime.now()
    status_code = random.choice([200, 301, 400, 401, 403, 404, 405, 500])
    file_size = random.randint(1, 1024)

    log_entry = (
        f"{ip_part1}.{ip_part2}.{ip_part3}.{ip_part4} - "
        f"[{timestamp}] \"GET /projects/260 HTTP/1.1\" "
        f"{status_code} {file_size}\n"
        )
    sys.stdout.write(log_entry)
    sys.stdout.flush()
