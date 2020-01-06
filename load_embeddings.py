import fasttext

model = fasttext.load_model('dtra_300.bin')

print(model.get_nearest_neighbors('rocket', 20))


