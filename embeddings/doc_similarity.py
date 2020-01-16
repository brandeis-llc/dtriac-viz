from gensim.models.doc2vec import Doc2Vec
import argparse
from os.path import join as pjoin

parser = argparse.ArgumentParser()
parser.add_argument("query", help="the query string")
parser.add_argument("-i", help="query is a doc id", action="store_true")
parser.add_argument("-v", "--verbose", help="show original results documents", action="store_true")
args = parser.parse_args()


def get_most_similar_documents(doc2vec, query, use_id, topn=5, wiki_only=True):
    if use_id:
        query_vec = doc2vec.docvecs[query]
    else:
        query_vec = doc2vec.infer_vector(query.strip().split())
    sims = model.docvecs.most_similar([query_vec], topn=len(doc2vec.docvecs))
    if wiki_only:
        result_ids = []
        for s_id in sims:
            if s_id[0].startswith('w'):
                result_ids.append(s_id)
                topn -= 1
            if not topn:
                return result_ids
    else:
        return sims[:topn]


if __name__ == "__main__":
    model = Doc2Vec.load("wiki_dtra_doc2vec")
    similar_docs = get_most_similar_documents(model, args.query, use_id=args.i)
    for doc in similar_docs:
        print(doc)
        if args.verbose:
            with open(pjoin('wiki_data', f"{doc[0][1:]}.txt"), 'r') as f:
                print(f.readline())



