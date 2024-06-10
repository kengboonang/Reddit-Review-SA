from dotenv import load_dotenv
from huggingface_hub import login
import os
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification, BertTokenizer, BertForSequenceClassification

# Set model name
model_name = "kbang2021/yelp_polarity_tuned_bert_base_1000"

# load pre-trained model
model = BertForSequenceClassification.from_pretrained(model_name)
model.eval()

# load local tokenizer
tokenizer = BertTokenizer.from_pretrained("./models/yelp_polarity_bert_1000_tokenizer")

class_labels = ["negative", "positive"]

def predict_sentiment(encoding, model):
    output = model(input_ids=encoding["input_ids"].unsqueeze(0), attention_mask=encoding["attention_mask"].unsqueeze(0))
    _, pred = torch.max(output.logits, dim=1)
    return class_labels[pred]
