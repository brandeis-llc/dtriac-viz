from os.path import join as pjoin
from elasticsearch import Elasticsearch, helpers


es = Elasticsearch("http://tarski.cs-i.brandeis.edu:9200/")
wiki_data_dir = 'wiki_data'

wiki_index = helpers.scan(es, query={"query": {"match_all": {}}}, index='enwiki-nuke_tech')

for i, doc in enumerate(wiki_index, 1):
    with open(pjoin(wiki_data_dir, f"{doc['_id']}.txt"), 'w') as f:
        f.write(doc['_source']['opening_text'])
    if i % 1000 == 0:
        print(f"working on {i} wiki documents!")

