# src/summarizers/tfidf_summarizer.py

from sklearn.feature_extraction.text import TfidfVectorizer
from ..preprocess import preprocess_text, get_stopwords, get_sentences

def summarize_tfidf(text, num_sentences=3):
    """
    Generates an extractive summary of a text using the TF-IDF algorithm.
    """
    sentences = get_sentences(text)
    if not sentences:
        return ""
        
    cleaned_sentences = [preprocess_text(s) for s in sentences]

    stop_words = list(get_stopwords())
    vectorizer = TfidfVectorizer(stop_words=stop_words)
    tfidf_matrix = vectorizer.fit_transform(cleaned_sentences)

    sentence_scores = tfidf_matrix.sum(axis=1)
    
    sentence_ranks = sentence_scores.A1.argsort()[::-1]
    top_sentence_indices = sentence_ranks[:num_sentences]
    
    top_sentence_indices.sort()
    
    summary = ' '.join([sentences[i] for i in top_sentence_indices])
    return summary