import re
import argparse
from os.path import join as pjoin
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

parser = argparse.ArgumentParser()
parser.add_argument("dims", help="the dimension of the embeddings", type=int)
parser.add_argument("-d", help="use dtra data", action="store_true")
parser.add_argument("-w", help="use wiki data", action="store_true")
parser.add_argument("out", help="output file name", type=str)


args = parser.parse_args()


def load_wiki_docs(data_dir='wiki_data'):
    with open('index_files/wiki_ids.txt', 'r') as f:
        ids = [line.strip() for line in f]
    documents = []
    for i, doc_id in enumerate(ids, 1):
        with open(pjoin(data_dir, doc_id), 'r') as f:
            doc = f.read().strip()
            documents.append(TaggedDocument(doc.split(), ['w' + doc_id.split('.')[0]]))
            if i % 1000 == 0:
                print('Processing {} wiki document!'.format(i))
    return documents


def load_dtra_docs(data_dir='dtra_data', start_page=5):
    page_pattern = r'📃 \d{4} 📃'
    with open('index_files/dtra_ids.txt', 'r') as f:
        dtra_ids = [line.strip() for line in f]
    documents = []
    for i, doc_id in enumerate(dtra_ids, 1):
        with open(pjoin(data_dir, doc_id), 'r') as f:
            doc = f.read().strip()
            pages = ' '.join(re.split(page_pattern, doc)[start_page-1: -1])
            if pages:
                doc = pages
            documents.append(TaggedDocument(doc.split(), ['d' + doc_id.split('.')[0]]))
            if i % 1000 == 0:
                print('Processing {} dtra document!'.format(i))
    return documents


def train(docs, vector_size, out_file):
    model = Doc2Vec(docs,
                    dm=1,
                    vector_size=vector_size,
                    window=5,
                    min_count=1,
                    epochs=30,
                    workers=4)
    model.save(out_file)
    model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)
    print(f'finish training! the doc size is {len(model.docvecs)}')


if __name__ == "__main__":
    all_documents = []
    if args.d:
        all_documents.extend(load_dtra_docs())
    elif args.w:
        all_documents.extend(load_wiki_docs())
    elif not all_documents:
        raise ValueError("Use at least one source of data!")

    train(all_documents, args.dims, args.out)
