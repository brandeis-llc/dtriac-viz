# Tensorboard Projector

Simple wrapper around [the tensorboard vector projector](https://projector.tensorflow.org/) for locally stored vectorized data. 

## Usage

Write a module with a function `load_vectors(datafile, size)` with parameters; 
* `datafile`: a file name that persists the vectorized data.
* `size`: number of vectors to return and to be projected in the tensorboard. 

and that returns; 
* `vectors`: a numpy array (shape is `[SIZE, DIM]`, where SIZE is #instances and DIM is dimension of the vectors)

In this function, you are also responsible for writing a metadata file. A metadata file MUST be named as `metadata.tsv`, placed in the same directory as the `datafile` file, and MUST contain a header line at the top. Metadata values will only be interpreted as literal strings (e.g. no HTML tag embedding). This means it is RECOMMENDED to use separate directories to hold different datasets for tensorboard projection, because this script may overwrite the metadata file generated for a specific dataset, which can result in a broken tensorboard. 

Once your module is ready, (see [`doc.py`](doc.py), or [`page.py`](page.py) for examples) you can pass the name of the module as an argument to `-l` option to the [`run.py`](run.py). 
For more options see help message from `run.py`. 

#### example

```
python ./run.py   -l page -d /data/dtriac/dtriac-19d/vectorization/page2vec/all.res.pkl -n page2vec -p 6008
```

## TODO

* add support for sprite (see [this issue](https://github.com/tensorflow/tensorboard/issues/670) for how)
