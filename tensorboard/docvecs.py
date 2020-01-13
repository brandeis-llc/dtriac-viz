import random
from os.path import join as pjoin
from os.path import expanduser

import numpy
from gensim.models.doc2vec import Doc2Vec

import create_ckpt


def prep_docvecs(datadir):
    EMB = pjoin(datadir, 'dtra_doc2vec')
    META_F = 'metadata.tsv'
    META = pjoin(datadir, META_F)
    CONFIG = pjoin(datadir, 'projector_config.pbtxt')

    model = Doc2Vec.load(EMB)
    DIM = len(model.docvecs['d000997'])
    SIZE = len(model.docvecs)
    vectors = numpy.zeros((SIZE, DIM))

    print(SIZE, DIM)
    with open(CONFIG, 'w+') as config_f:
        config_f.write(f'embeddings {{ metadata_path: "{META_F}" }}\n')
    with open(META, 'w+') as meta_f:
        meta_f.write("index\tname\tgroup\n")
        for i, docid in enumerate(model.docvecs.doctags):
            vectors[i] = model.docvecs[docid]
            meta_f.write(f'{i}\t{docid}\t<a href="5">{random.sample(range(5),1)[0]}</a>\n')
    return vectors


if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser(
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
        description=__doc__
    )
    parser.add_argument(
        '-d', '--datadir',
        action='store',
        nargs='?',
        help='Directory name where doc2vec npy file is stored.'
    )
    parser.add_argument(
        '-n', '--name',
        required=False,
        default='',
        action='store',
        nargs='?',
        help='Human-friendly name of the embedding. When not given, npy filename will be re-used.'
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
    vectors = prep_docvecs(datadir)
    create_ckpt.create_ckpt(vectors, datadir, args.name)

    from tensorboard import program
    tb = program.TensorBoard()
    tb.configure(argv=[None, '--logdir', datadir, '--port', args.port])
    url = tb.main()


