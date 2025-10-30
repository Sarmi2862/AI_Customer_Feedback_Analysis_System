# app_streamlit.py - simple demo app
import streamlit as st, pandas as pd
st.title('Intelligent Customer Feedback Analysis - Demo')
uploaded = st.file_uploader('Upload CSV', type=['csv'])
if uploaded is not None:
    df = pd.read_csv(uploaded)
    st.write('Preview', df.head())
    st.write('Showing demo sentiment labels (random)')
    import random
    df['pred'] = df['text'].apply(lambda x: random.choice(['positive','negative','neutral']))
    st.write(df[['text','pred']].head())