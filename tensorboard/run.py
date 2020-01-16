import math
import os
from os.path import expanduser

import create_ckpt

if __name__ == '__main__':
    import argparse
    import importlib
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__doc__
    )
    parser.add_argument(
        '-l', '--loader',
        required=True,
        action='store',
        nargs='?',
        help='module name to use for loading vector data.'
    )
    parser.add_argument(
        '-s', '--size',
        default=math.inf,
        action='store',
        type=int,
        nargs='?',
        help='Number of data instance to load in. If not given, read all data in. '
    )
    parser.add_argument(
        '-d', '--datapath',
        action='store',
        nargs='?',
        help='A file name with persisted vectors.'
    )
    parser.add_argument(
        '-n', '--name',
        required=False,
        default=None,
        action='store',
        nargs='?',
        help='Human-friendly name of the embedding. When not given, last node in the base file name will be used.'
    )
    parser.add_argument(
        '-p', '--port',
        default='6006',
        action='store',
        nargs='?',
        help='Port to the board to listen to serve a web app.'
    )
    args = parser.parse_args()
    datapath = os.path.normpath(expanduser(args.datapath))
    data_dir, data_base = os.path.split(datapath)
    loader = importlib.import_module(args.loader)
    vectors = loader.load_vectors(datapath, args.size)
    if args.name is None:
        name = data_base
    else:
        name = args.name
    create_ckpt.create_ckpt(vectors, data_dir, name)

    # writes config fils for tb
    from tensorboard import program
    tb = program.TensorBoard()
    tb.configure(argv=[None, '--logdir', data_dir, '--port', args.port])
    url = tb.main()


