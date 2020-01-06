import fasttext


def fasttext_and_save(text_file, model_type='cbow',
                      dim=300,
                      ws=5,
                      neg=10,
                      epoch=5,
                      lr=0.05):
    """
     "These models were trained using CBOW with position-weights, in dimension 300,
    with character n-grams of length 5, a window of size 5 and 10 negatives."
    :param text_file:
    :param model_path:
    :param model_type:
    :param dim:
    :param ws:
    :param neg:
    :param epoch:
    :param lr:
    :return:
    """

    print(f"Training fasttext embedding ({dim} dimensions)")
    model = fasttext.train_unsupervised(input=text_file,
                                        model=model_type,
                                        dim=dim,
                                        lr=lr,
                                        epoch=epoch,
                                        ws=ws,
                                        neg=neg,
                                        )
    model.save_model(f'dtra_{dim}.bin')


if __name__ == "__main__":
    fasttext_and_save('dtra_data/dtra.txt', dim=300)