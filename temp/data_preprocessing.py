# data_preprocessing.py - cleaning & simple preprocessing
import argparse, pandas as pd, re
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import nltk
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)
nltk.download('wordnet', quiet=True)

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def clean_text(s):
    if pd.isna(s): return ''
    s = str(s)
    s = s.replace('@','e')
    s = re.sub(r'[^A-Za-z0-9\\s\\.,!\\?]','',s)
    s = re.sub(r'\\s+',' ',s).strip()
    return s

def preprocess_text(s):
    s = s.lower()
    tokens = word_tokenize(s)
    tokens = [t for t in tokens if t.isalpha()]
    tokens = [t for t in tokens if t not in stop_words]
    tokens = [lemmatizer.lemmatize(t) for t in tokens]
    return ' '.join(tokens)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', default='data/simulated_feedback.csv')
    parser.add_argument('--output', default='data/cleaned_feedback.csv')
    args = parser.parse_args()

    df = pd.read_csv(args.input)
    df = df.drop_duplicates(subset=['text']).reset_index(drop=True)
    df['raw_text'] = df['text'].astype(str)
    df['cleaned_text'] = df['raw_text'].apply(clean_text)
    df['processed_text'] = df['cleaned_text'].apply(preprocess_text)
    df = df[df['processed_text'].str.strip() != '']
    df.to_csv(args.output, index=False)
    print('Saved', args.output, 'with', len(df), 'rows')