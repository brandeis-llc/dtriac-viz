# Tensorboard Projector

Simple wrapper around [the tensorboard vector projector](https://projector.tensorflow.org/) for locally stored vectorized data. 

## Usage

Write a module with a function `load_vectors(datadir, size)` with parameters; 
* `datadir`: directory name where your persisted vectorized data. Actual persist file name is not passed as a parameter, so you need to hard-code the name in this function. 
* `size`: number of vectors to return and to be projected in the tensorboard. 

and that returns; 
* `vectors`: a numpy array (shape is `[SIZE, DIM]`, where SIZE is #instances and DIM is dimension of the vectors)

In this function, you are also responsible for writing a metadata file. A metadata file MUST be named as `/datadir/metadata.tsv` and MUST contain a header line at the top. Metadata values will only be interpreted as literal strings (e.g. no HTML tag embedding). 

Once your module is ready, (see [`doc.py`](doc.py), or [`page.py`](page.py) for examples) you can pass the name of the module as an argument to `-l` option to the [`run.py`](run.py). 
For more options see help message from `run.py`. 
