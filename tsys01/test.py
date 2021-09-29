#!/usr/bin/python3

from tsys01 import TSYS01
from llog import LLogWriter

device = "tsys01"
parser = LLogWriter.create_default_parser(__file__, device)
args = parser.parse_args()

with LLogWriter(args.meta, args.output, console=args.console) as log:
    tsys = TSYS01()
    if not tsys.init():
        print("Failed to initialize Keller LD sensor!")
        exit(1)
    def data_getter():
        tsys.read()
        return f'{tsys.temperature()}'
    log.log_data_loop(data_getter, parser_args=args)
