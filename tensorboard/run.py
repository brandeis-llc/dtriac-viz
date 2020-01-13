import math
import os
from os.path import expanduser

import create_ckpt

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__doc__
    )
    parser.add_argument(
        '-m', '--model',
        required=True,
        choices=['doc', 'page', 'mm'],
        action='store',
        nargs='?',
        help='Model to use. `doc` to visualize doc2vec vectors, `page` image vectors from first 2 pages, `mm` combined vectors.'
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
        '-d', '--datadir',
        action='store',
        nargs='?',
        help='Directory name where persist vector file is stored.'
    )
    parser.add_argument(
        '-n', '--name',
        required=False,
        default='',
        action='store',
        nargs='?',
        help='Human-friendly name of the embedding. When not given, last node in the `datadir` will be used.'
    )
    parser.add_argument(
        '-p', '--port',
        default='6006',
        action='store',
        nargs='?',
        help='Port to the board to listen to serve a web app.'
    )
    args = parser.parse_args()
    datadir = expanduser(args.datadir)
    if args.model == 'doc':
        import doc
        loader = doc
    elif args.model == 'page':
        import page
        loader = page
    elif args.model == 'mm':
        import mm
        loader = mm
    vectors = loader.load_vectors(datadir, args.size)
    if args.name == "":
        name = os.path.basename(args.datadir)
    else:
        name = args.name
    create_ckpt.create_ckpt(vectors, datadir, name)

    from tensorboard import program
    tb = program.TensorBoard()
    tb.configure(argv=[None, '--logdir', datadir, '--port', args.port])
    url = tb.main()


