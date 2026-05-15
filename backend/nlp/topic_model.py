from gensim import corpora
from gensim.models.ldamodel import LdaModel

def generate_topics(texts, num_topics=3):

    tokenized = [text.split() for text in texts]

    dictionary = corpora.Dictionary(tokenized)

    corpus = [
        dictionary.doc2bow(text)
        for text in tokenized
    ]

    lda_model = LdaModel(
        corpus=corpus,
        id2word=dictionary,
        num_topics=num_topics,
        passes=10
    )

    topics = lda_model.print_topics()

    return topics