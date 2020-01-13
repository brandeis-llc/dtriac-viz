from os.path import join as pjoin

import numpy
from gensim.models.doc2vec import Doc2Vec


def load_vectors(datadir, size):
    EMB = pjoin(datadir, 'dtra_doc2vec')
    META_F = 'metadata.tsv'
    META = pjoin(datadir, META_F)
    CONFIG = pjoin(datadir, 'projector_config.pbtxt')

    model = Doc2Vec.load(EMB)
    DIM = len(model.docvecs['d997'])
    SIZE = min(size, len(model.docvecs))
    vectors = numpy.zeros((SIZE, DIM))

    print(SIZE, DIM)
    with open(CONFIG, 'w+') as config_f:
        config_f.write(f'embeddings {{ metadata_path: "{META_F}" }}\n')
    with open(META, 'w+') as meta_f:
        meta_f.write("index\tname\tpdf\n")
        for i, docid in enumerate(model.docvecs.doctags):
            if i == size:
                break
            vectors[i] = model.docvecs[docid]
            meta_f.write(f'{i}\t{docid}\thttp://tarski.cs-i.brandeis.edu:8181/data/{docid[1:]}/pdf.pdf\n')
    return vectors
