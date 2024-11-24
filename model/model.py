import os
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import pymorphy2
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import numpy as np
import json

nltk.download('stopwords')
nltk.download('punkt_tab')
russian_stopwords = stopwords.words('russian')
morph = pymorphy2.MorphAnalyzer()

def preprocess_text(text):
    text = text.lower()
    text = re.sub(r'http\S+|www.\S+|mailto:\S+', '', text)
    text = re.sub(r'[^а-яё\s]', '', text)
    tokens = word_tokenize(text, language='russian')
    tokens = [morph.normal_forms(token)[0] for token in tokens if token not in russian_stopwords and token.isalpha()]
    text = ' '.join(tokens)

    return text


model_path = os.path.dirname(os.path.abspath(__file__))+'/model_bundle' 

tokenizer = AutoTokenizer.from_pretrained(model_path)
model = AutoModelForSequenceClassification.from_pretrained(model_path)
model.eval()

device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)

with open(f'{model_path}/label_to_id.json', 'r', encoding='utf-8') as f:
    label_to_id = json.load(f)

id_to_label = {int(v): k for k, v in label_to_id.items()}


def predict(text):
    inputs = tokenizer(
        text,
        padding='max_length',
        truncation=True,
        max_length=512,
        return_tensors='pt'
    )
    inputs = {k: v.to(device) for k, v in inputs.items()}

    with torch.no_grad():
        outputs = model(**inputs)

    logits = outputs.logits
    predicted_class_id = logits.argmax(dim=-1).item()
    predicted_label = id_to_label[predicted_class_id]
    print(predicted_class_id, predicted_label)
    probabilities = torch.nn.functional.softmax(logits, dim=-1)
    confidence = probabilities[0, predicted_class_id].item()
    
    return predicted_class_id, predicted_label, confidence
