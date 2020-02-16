# US nuclear test programs in an ES index

## Data
Data of US nuclear tests was manually scrapped following the procedure below. Resulting JSON files are stored in `nuclear_operations_json/`

### Manual procedure for extracting tabular information from Wikipedia page data:

1. List of test programs are obtained from [this wiki article](https://en.wikipedia.org/wiki/List_of_United_States%27_nuclear_weapons_tests)
1. Use URL of each test program article on wikitable2csv, a webapp with source code available on GitHub (https://github.com/gambolputty/wikitable2csv)
1. Copy CSV markup to CSVJSON, another webapp with source code available on GitHub (https://github.com/martindrapeau/csvjson-app)
1. Take output JSON file and add to JSON ‘megadoc’ of all nuclear tests across all operations



## Indexing to ES

Once data is ready, use [`index_to_es.py`](index_to_es.py) to create an ES index. Note that ES address and index name are all hard-coded in the script and used to grab a mapping file ([`nuke_tests.mappings`](nuke_tests.mappings)) for the index. 


## Timeline of programs visualized on kibana
Test timeline visualization is defined in vega JSON in [`test-timeline-kibana.vega`](test-timeline-kibana.vega) file. To add it to Kibana dashboard, Create a new visualization on Kibana and select **vega** type. Then paste the file contents.


