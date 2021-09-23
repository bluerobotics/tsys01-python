#!/usr/bin/python3

from tsys01 import TSYS01
from llog import LLogWriter

device = "tsys01"
parser = LLogWriter.create_default_parser(__file__, device, default_frequency=1)
args = parser.parse_args()


with llog.LLogWriter(args.meta, args.output) as log:
    sensor = TSYS01()
    
    if not sensor.init():
        log.log_error("Error initializing sensor")
        exit(1)
        
    log.log_rom(' '.join(sensor._k))

    def data_getter():
        if not sensor.read():
            raise Exception("Error reading sensor")
        return f"{sensor.temperature()}"
    
    log.log_data_loop(data_getter, parser_args=args)
