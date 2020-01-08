from os.path import join as pjoin
from gensim.models.doc2vec import Doc2Vec, TaggedDocument


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


def load_dtra_docs(data_dir='dtra_data'):
    with open('index_files/dtra_ids.txt', 'r') as f:
        wiki_ids = [line.strip() for line in f]
    documents = []
    for i, doc_id in enumerate(wiki_ids, 1):
        with open(pjoin(data_dir, doc_id), 'r') as f:
            doc = f.read().strip()
            documents.append(TaggedDocument(doc.split(), ['d' + doc_id.split('.')[0]]))
            if i % 1000 == 0:
                print('Processing {} dtra document!'.format(i))
    return documents


def train(docs, vector_size, out_file):
    model = Doc2Vec(docs,
                    dm=1,
                    vector_size=vector_size,
                    window=4,
                    min_count=1,
                    epochs=40,
                    workers=4)
    model.save(out_file)
    model.delete_temporary_training_data(keep_doctags_vectors=True, keep_inference=True)
    print(f'finish training! the doc size is {len(model.docvecs)}')


if __name__ == "__main__":
    all_documents = []
    all_documents.extend(load_dtra_docs())
    all_documents.extend(load_wiki_docs())
    train(all_documents, 200, "wiki_dtra_doc2vec")
    # model = Doc2Vec.load("wiki_doc2vec")
    # print(len(model.docvecs))
    # print(model.docvecs['1000559'])
