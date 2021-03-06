from os.path import join as pjoin

import tensorflow as tf
from tensorflow.contrib.tensorboard.plugins import projector


def create_ckpt(vectors, datadir, name):
    medatada_fname = 'metadata.tsv'
    config_fname = pjoin(datadir, 'projector_config.pbtxt')
    with open(config_fname, 'w+') as config_f:
        config_f.write(f'embeddings {{ metadata_path: "{medatada_fname}" }}\n')
    SIZE, DIM = vectors.shape
    X_init = tf.placeholder(tf.float32, shape=vectors.shape, name=f'{name}-{DIM}d')
    X = tf.Variable(X_init)

    init = tf.global_variables_initializer()

    sess = tf.Session()
    sess.run(init, feed_dict={X_init: vectors})

    saver = tf.train.Saver()
    writer = tf.summary.FileWriter('.', sess.graph)

    config = projector.ProjectorConfig()
    embed = config.embeddings.add()
    embed.metadata_path = medatada_fname

    projector.visualize_embeddings(writer, config)
    saver.save(sess, pjoin(datadir, 'model.ckpt'), global_step=SIZE)
    sess.close()

