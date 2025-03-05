from sklearn.feature_extraction.text import TfidfVectorizer


def compute_tfidf(documents):
    vectorizer = TfidfVectorizer(use_idf=True, smooth_idf=False)
    tfidf_matrix = vectorizer.fit_transform(documents)
    terms = vectorizer.get_feature_names_out()

    idf = vectorizer.idf_
    tf = tfidf_matrix.toarray().mean(axis=0)

    tfidf = [
        {"word": terms[idx], "tf": round(tf[idx], 5), "idf": round(idf[idx], 5)}
        for idx in range(len(terms))
    ]

    return sorted(tfidf, key=lambda x: x["idf"], reverse=True)[:50]
