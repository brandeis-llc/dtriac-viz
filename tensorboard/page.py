import pickle
from os.path import join as pjoin

import numpy


def load_vectors(datadir, size):
    VGG = pjoin(datadir, 'all.res.pkl')
    META = pjoin(datadir, 'metadata.tsv')
    emb, names = pickle.load(open(VGG, 'br'))
    SIZE = min(size, len(emb))
    DIM = len(emb[0])
    vectors = numpy.zeros((SIZE, DIM))
    with open(META, 'w') as meta_f:

        meta_f.write(f'index\tdocid\tpage\tannotate\n')
        for i in range(SIZE):
            name = names[i]
            vectors[i] = emb[i]
            docid, page = name[0].split('/')[-2:]
            docid = int(docid)
            page = int(page.replace('.png', ""))
            meta_f.write(f'{i}\t{docid}\t{page}\thttp://tarski.cs-i.brandeis.edu:5100/query/{docid}_{page:04}.png\n')

    return vectors

