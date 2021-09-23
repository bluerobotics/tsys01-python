#!/usr/bin/python3

import matplotlib.pyplot as plt

DEVICE = 'tsys01'

def generate_figures(log):
    footer = f'{DEVICE} test report'

    f, spec = log.figure(height_ratios=[1,1], suptitle=f'{DEVICE} data', footer=footer)
    plt.subplot(spec[0,0])
    log.rom.T.ttable(rl=True)
    """ TODO: uncomment once config is available from test-tsys01.py
    plt.subplot(spec[0,1])
    log.config.T.ttable(rl=True)
    """

    plt.subplot(spec[1,:])
    log.data.temperature.pplot()

if __name__ == '__main__':
    from llog import LLogReader
    from matplotlib.backends.backend_pdf import PdfPages

    parser = LLogReader.create_default_parser(__file__, DEVICE)
    args = parser.parse_args()

    log = LLogReader(args.input, args.meta)

    generate_figures(log)

    if args.output:
        # todo check if it exists!
        with PdfPages(args.output) as pdf:
            for n in plt.get_fignums():
                pdf.savefig(n)

    if args.show:
        plt.show()
