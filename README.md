# Doc2Vec Embeddings
Code here is to train doc2vec embeddings (Gensim) using DTRA data and Wiki data. 

## Requirements

`dtra_data/`: Contains DTRA txt files, each file is a "doc" and has the name is `dtra_id.txt`.

`wiki_data/`: Contains Wiki txt files, each file is a "doc" and has the name is `wiki_id.txt`.

`index_files/dtra_ids.txt`: A list of DTRA file ids that can be used to map to the original text file.

`index_files/wiki_ids.txt`: A list of Wiki file ids that can be used to map to the original text file.


## Training 
`doc2vec.py` is the main file we use to train doc2vec
```
Usage: doc2vec.py [-d] [-w] dims out
-d      use dtra data as part of training data
-w      use wiki data as part of training data
dims    the dimensions of embeddings
out     output embeddings file name
```

## Document Similarity