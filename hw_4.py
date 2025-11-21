from math import log


# Task 1
class CountVectorizer:
    def __init__(self):
        self.vocabulary = []
        self.vectors = []

    def fit_transform(self, corpus):
        tokenized_corpus = [doc.lower().split() for doc in corpus]
        seen = set()
        for doc in tokenized_corpus:
            for word in doc:
                if word not in seen:
                    self.vocabulary.append(word)
                    seen.add(word)
        word_to_index = {word: i for i, word in enumerate(self.vocabulary)}
        for doc in tokenized_corpus:
            vector = [0] * len(self.vocabulary)
            for word in doc:
                index = word_to_index[word]
                vector[index] += 1
            self.vectors.append(vector)
        return self.vectors

    def get_feature_names(self):
        return self.vocabulary


# Task 2
def tf_transform(count_matrix):
    tf_matrix = []
    for vector in count_matrix:
        text_len = sum(vector)
        tf_vector = [
            round(count / text_len, 3) if text_len > 0 else 0.0 for count in vector
        ]
        tf_matrix.append(tf_vector)

    return tf_matrix


# Task 3
def idf_transform(count_matrix):
    len_voc = len(count_matrix[0])
    idf_vector = [0] * len_voc
    num_docs = len(count_matrix) + 1
    for i in range(len_voc):
        word_count = sum(1 for vector in count_matrix if vector[i] > 0) + 1
        idf = log(num_docs / word_count) + 1
        idf_vector[i] = round(idf, 1)
    return idf_vector


# Task 4
class TfidfTransformer:
    def __init__(self):
        self.idf = []
        self.len_voc = 0

    def fit(self, count_matrix):
        self.idf = idf_transform(count_matrix)
        self.len_voc = len(count_matrix[0])

    def transform(self, count_matrix):
        tf_matrix = tf_transform(count_matrix)
        tf_idf_matrix = tf_matrix
        for i in range(len(tf_idf_matrix)):
            for j in range(self.len_voc):
                tf_idf_matrix[i][j] *= self.idf[j]
                tf_idf_matrix[i][j] = round(tf_idf_matrix[i][j], 3)

        return tf_idf_matrix

    def fit_transform(self, X):
        self.fit(X)
        return self.transform(X)

    def __tf_transform(count_matrix):
        tf_matrix = []
        for vector in count_matrix:
            text_len = sum(vector)
            tf_vector = [
                round(count / text_len, 3) if text_len > 0 else 0.0 for count in vector
            ]
            tf_matrix.append(tf_vector)

        return tf_matrix

    def __idf_transform(count_matrix):
        len_voc = len(count_matrix[0])
        idf_vector = [0] * len_voc
        num_docs = len(count_matrix) + 1
        for i in range(len_voc):
            word_count = sum(1 for vector in count_matrix if vector[i] > 0) + 1
            idf = log(num_docs / word_count) + 1
            idf_vector[i] = round(idf, 1)
        return idf_vector


# Task 5
class TfidfVectorizer(CountVectorizer):
    def __init__(self):
        super().__init__()
        self.tfidf_transformer = TfidfTransformer()

    def fit_transform(self, corpus):
        super().fit_transform(corpus)
        tfidf_matrix = self.tfidf_transformer.fit_transform(self.vectors)
        return tfidf_matrix
