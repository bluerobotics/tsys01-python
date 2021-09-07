#!/usr/bin/python3

import argparse
from tsys01 import TSYS01
from pathlib import Path
import llog
import time

device = "tsys01"
defaultMeta = Path(__file__).resolve().parent / f"{device}.meta"

parser = argparse.ArgumentParser(description=f'{device} test')
parser.add_argument('--output', action='store', type=str, default=None)
parser.add_argument('--meta', action='store', type=str, default=defaultMeta)
parser.add_argument('--frequency', action='store', type=int, default=1)
args = parser.parse_args()


with llog.LLogWriter(args.meta, args.output) as log:
    sensor = TSYS01()
    
    if not sensor.init():
        log.log(llog.LLOG_ERROR, "Error initializing sensor")
        exit(1)

    while True:
        try:
            if not sensor.read():
                log.log(llog.LLOG_ERROR, "Error reading sensor")
            else:
                log.log(llog.LLOG_DATA, f"{sensor.temperature()}")
        except Exception as e:
            log.log(llog.LLOG_ERROR, e)

        if args.frequency:
            time.sleep(1.0/args.frequency)
