# insights.py - recurring terms and forecast placeholder
import argparse, pandas as pd
from collections import Counter

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='data/cleaned_feedback.csv')
    args = parser.parse_args()
    df = pd.read_csv(args.input)
    neg = df[df['label']=='negative']
    text = ' '.join(neg['processed_text'].fillna('').tolist())
    words = text.split()
    common = Counter(words).most_common(20)
    print('Top recurring terms in negative feedback:', common[:10])