# make_dataset.py - generate simulated feedback CSV (~1200 rows)
import random, csv
from faker import Faker
fake = Faker()

templates = {
    'positive': [
        "I loved the product! It arrived on time and works perfectly.",
        "Great service — the support team helped me quickly.",
        "Very satisfied. Quality exceeded my expectations."
    ],
    'negative': [
        "The product stopped working after two days. Very disappointed.",
        "Customer support never replied, I want a refund.",
        "Received wrong color and it took weeks to replace."
    ],
    'neutral': [
        "It's okay — does the job but nothing special.",
        "Average experience, delivery was fine.",
        "Not bad, but could improve packaging."
    ]
}

rows = []
for i in range(1200):
    sentiment = random.choices(['positive','negative','neutral'], weights=[0.45,0.35,0.2])[0]
    template = random.choice(templates[sentiment])
    text = template
    if random.random() < 0.6:
        text += ' ' + fake.sentence(nb_words=random.randint(3,12))
    if random.random() < 0.15:
        text = text.replace(' ', '  ').replace('e', '@')
    rows.append({'feedback_id': i+1, 'source': random.choice(['email','chat','social']), 'text': text, 'label': sentiment})

with open('data/simulated_feedback.csv','w',newline='',encoding='utf-8') as f:
    writer = csv.DictWriter(f, fieldnames=['feedback_id','source','text','label'])
    writer.writeheader()
    writer.writerows(rows)
print('Saved data/simulated_feedback.csv (1200 rows)')