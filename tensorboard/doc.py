from os.path import join as pjoin
from os.path import dirname

import numpy
from gensim.models.doc2vec import Doc2Vec

PDF_BROWSER_DATA_URL = 'http://tarski.cs-i.brandeis.edu:8181/data/{docid}/pdf.pdf'


def load_vectors(data_path, size):
    data_dir = dirname(data_path)
    metadata = pjoin(data_dir, 'metadata.tsv')

    model = Doc2Vec.load(data_path)
    dim_vectors = len(model.docvecs['d000997'])
    # dim_vectors = len(model.docvecs[next(iter(model.docvecs.doctags))])
    size_vectors = min(size, len(model.docvecs))
    vectors = numpy.zeros((size_vectors, dim_vectors))

    with open(metadata, 'w+') as meta_f:
        meta_f.write("index\tname\tpdf\n")
        for i, docid in enumerate(model.docvecs.doctags):
            if i == size:
                break
            vectors[i] = model.docvecs[docid]
            meta_f.write(f'{i}\t'
                         f'{docid}\t'
                         f'{PDF_BROWSER_DATA_URL.format(docid=docid[1:])}'
                         f'\n')
    return vectors
