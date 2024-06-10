import torch
from utils.BERT_processing import tokenize_function
from transformers import BertForSequenceClassification, BertTokenizer


model_name = "bert-base-cased"
model_path = "models\saved_models\google_review_finetuned_BERT_model.pt"
tokenizer_path = "models?saved_models/google_review_BERT_tokenizer"
model = BertForSequenceClassification.from_pretrained(model_name, num_labels=3)
model.load_state_dict(torch.load(model_path, map_location=torch.device('cpu')))
model.eval()
tokenizer = BertTokenizer.from_pretrained(tokenizer_path)
class_labels = ["negative", "neutral", "positive"]

def predict_sentiment(encoding, model):
    output = model(input_ids=encoding["input_ids"].unsqueeze(0), attention_mask=encoding["attention_mask"].unsqueeze(0))
    _, pred = torch.max(output, dim=1)
    return class_labels[pred]
