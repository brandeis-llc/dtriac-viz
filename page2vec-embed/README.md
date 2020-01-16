# Simple image-to-vector and clustering 

Use `cluster.py` to generate resnet- or vgg19-based vectors from input images. This sciprt also can be used to train K-Means clusters with `--cluster_model` option. 
```bash 
usage: cluster.py [-h] [--data DATA] [--model {vgg19,resnet50}]
                  [--output OUTPUT] [--data-count INST_COUNT]
                  [--data-store DATA_EMBED] [--cluster_model CLUSTER_STORE]
                  [--vis]

Model Training

optional arguments:
  -h, --help            show this help message and exit
  --data DATA           path to directory containing image dataset
  --model {vgg19,resnet50}
                        pretrained model name
  --output OUTPUT       location to store the output pickle
  --data-count INST_COUNT
                        number of instances to use for cluster training
  --data-store DATA_EMBED
                        If this param is used, data and model are
                        ignored,data-store should contain a tuple where the
                        first element is anumpy array where each row is an
                        embedding and the second elementis a list of
                        filenames.
  --cluster_model CLUSTER_STORE
                        location to store the KMeans model.
  --vis                 generate output for tensorboard visualization
  ```

 The persisted K-Means model from `cluster.py` can be used as a classifier. Use `apply_model.py` for doing so. 

 ```bash 
 usage: apply_model.py [-h] [--cluster_model MODEL_PATH] [--data DATA]
                      [--output OUT_CSV]

optional arguments:
  -h, --help            show this help message and exit
  --cluster_model MODEL_PATH
                        path to kmeans model
  --data DATA           path to directory containing image dataset
  --output OUT_CSV      path to csv file to store cluster prediction results
  ```
