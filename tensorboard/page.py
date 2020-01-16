import pickle
from os.path import join as pjoin
from os.path import dirname

import numpy

PAGE_CLUSTER_ANNOTATION_TOOL_URL = 'http://tarski.cs-i.brandeis.edu:5100/query/{docid}_{page:04}.png'


def load_vectors(data_path, size):
    data_dir = dirname(data_path)
    metadata = pjoin(data_dir, 'metadata.tsv')
    emb, names = pickle.load(open(data_path, 'br'))
    num_vecs = min(size, len(emb))
    dim_vecs = len(emb[0])
    vectors = numpy.zeros((num_vecs, dim_vecs))
    with open(metadata, 'w') as meta_f:

        meta_f.write(f'index\tdocid\tpage\tannotate\n')
        for i in range(num_vecs):
            name = names[i]
            vectors[i] = emb[i]
            docid, page = name[0].split('/')[-2:]
            docid = int(docid)
            page = int(page.replace('.png', ""))
            meta_f.write(f'{i}\t'
                         f'{docid}\t'
                         f'{page}\t'
                         f'{PAGE_CLUSTER_ANNOTATION_TOOL_URL.format(docid=docid, page=page)}'
                         f'\n')

    return vectors
