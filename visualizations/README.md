# README.md

## Visualizations for DTRIAC project

Samples of each visualization in directory /visualizations/samples/

These are "ideas" of what could be done with the data, 
Only a very small sample of the articles are currently used for these visualizations

Note: Some of these are currently set up to use CDNs (external resources).
The dynamic webpages will not work without online connection 
Screenshots of webpages are included here in samples subdirectory


**Network Graphs**

See: /visualizations/src_network_graph/

Description: Used original 534 articles about network science
	to construct networks linking authors, article, and 
	datasets used in article

To discover the datasets, I used data from ICON, 
a collection of datasets created by Aaron Clauset (CU Boulder)
https://icon.colorado.edu/

(1) 2D network graph
- In this graph, all nodes are labeled (compared to other where you have to hover over node to see label)
- Set up for a large screen 
- Kind of unwieldy (graph is hard to customize)
- To view in browser:
	- From main directory, start server in terminal (for Python3): 
	``` python -m http.server ```
	- Open localhost in browser (usually 8000)
- Sample: /visualizations/samples/network_graph_2d

(2) 3D network graph
- Needed: plotly (https://plot.ly/python/)
- Jupyter notebook: plot_3d_icon_datasets.ipynb
- Can only see one label at a time
- Dark blue are datasets, grayish are authors, etc.
- Can rotate, zoom in, etc.
- Sample: /visualizations/samples/network_graph_3d



**Map of temporally-sequenced nuclear weapons testing events**

See: /visualizations/src_nuclear_weapons_testing/

Description: 
- Map of the world showing the nuclear weapons testing events
- Location and time sequencing
- Radius of circle indicates number of tests at that time/location
- Linked to a subset of DTRIAC articles (from a selection of fewer than 200 articles)

Most of this information about the testing events was scraped from Wikipedia;
I "link" each event to a handful of DTRIAC articles by searching titles for keywords (see Google drive document)

(1) To render html, open index.html from a browser
Time delay currently set at 3000ms (see line 137)

Samples:

/visualizations/samples/operation_charioteer_1982
/visualizations/samples/operation_dominic_1962
/visualizations/samples/operation_fishbowl_1962
/visualizations/samples/operation_fulcrum_1976
/visualizations/samples/operation_plumbbob_1957

