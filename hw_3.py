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
