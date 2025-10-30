# Intelligent Customer Feedback Analysis System

This repo contains a ready-to-run scaffold for the assignment: *Intelligent Customer Feedback Analysis System using AI*.
Files included:
- data/simulated_feedback.csv (1200 rows)
- make_dataset.py (dataset generator)
- data_preprocessing.py
- train_sentiment_model.py
- summarization.py
- insights.py
- app_streamlit.py
- requirements.txt
- examples/long_feedback.txt
- AI_insights_report.pdf (generated sample report)

Run steps (local):
1. Create virtual env and install dependencies:
   python -m venv venv
   source venv/bin/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
2. (Optional) Regenerate sample data: python make_dataset.py
3. Preprocess data: python data_preprocessing.py --input data/simulated_feedback.csv --output data/cleaned_feedback.csv
4. Train model: python train_sentiment_model.py --input data/cleaned_feedback.csv --model_out models/distilbert_sentiment
5. Run summarization examples: python summarization.py --text "<your text>"
6. Generate insights (sample PDF included): python insights.py --input data/cleaned_feedback.csv --output AI_insights_report.pdf
7. Run Streamlit demo: streamlit run app_streamlit.py

Personalize the code/comments before submission to reflect your own work.
