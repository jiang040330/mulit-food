class DatasetSplit(object):

    def __init__(self):
        self.texts = []
        self.labels = []
        self.images = []

    def load_data(self, data_file, delimiter):
        with open(data_file) as tr:
            for line in tr.readlines():
                line = line.replace('\n', '')
                line = line.split(delimiter)
                #line[0]变为一个文本文件
                #self.texts.append(line[0])
                with open(line[0]) as txtf:
                    eletxt = txtf.read()
                    self.texts.append(eletxt)
                    
                self.labels.append(line[1])
                self.images.append(line[2])

    def get_texts(self):
        return self.texts

    def get_labels(self):
        return self.labels

    def get_images(self):
        return self.images

    def set_texts(self, texts):
        self.texts = texts

    def set_labels(self, labels):
        self.labels = labels

    def set_images(self, images):
        self.images = images
