#!/usr/bin/env python
import logging
import os
from signal import SIGINT
import sys

logging.basicConfig(format="[%(asctime)s] %(message)s")
log = logging.getLogger()
log.setLevel(logging.DEBUG)

command = sys.argv[1]

if command is None:
    log.error("No command provided.")
    sys.exit(1)

log.info("Starting command ({})".format(command))

while True:
    status = os.system(command)

    if status & 2:
        log.error("SIGINT received; terminating")
        sys.exit(status)
    else:
        log.info("Command ({}) exited, status {}; restarting".format(command, status))
