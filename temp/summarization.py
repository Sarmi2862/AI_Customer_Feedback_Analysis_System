# summarization.py - extractive + abstractive examples (abstractive requires transformers & model download)
import argparse
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

def extractive_summary(text, top_n=2):
    sentences = [s.strip() for s in text.split('.') if s.strip()]
    if len(sentences) <= top_n:
        return '. '.join(sentences)
    vec = TfidfVectorizer().fit_transform(sentences)
    sim_mat = cosine_similarity(vec)
    scores = sim_mat.sum(axis=1)
    ranked_idx = np.argsort(scores)[::-1][:top_n]
    return '. '.join([sentences[i] for i in ranked_idx])

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--text', type=str, help='Feedback text', required=False)
    args = parser.parse_args()
    sample = args.text or open('examples/long_feedback.txt').read()
    print('Extractive summary:')
    print(extractive_summary(sample, top_n=2))
    print('\\n(Abstractive summary requires transformers & model download)')