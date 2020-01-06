from os.path import join as pjoin


with open('dtra_data/d.txt', 'r') as fd:
    doc_ids = [line.strip() for line in fd]


with open('dtra.txt', 'w') as f:
    for i, doc_id in enumerate(doc_ids, 1):
        with open(pjoin(doc_id, 'tesseract.txt'), 'r') as doc:
            f.write(doc.read())
        if i % 100 == 0:
            print('working on {} document!'.format(i))
