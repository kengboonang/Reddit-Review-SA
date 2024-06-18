# Training requires input_ids, attention_mask, and labels
# Validation requires input_ids, attention_mask, and labels
# Prediction requires input_ids and attention_mask

def tokenize_function(data, tokenizer, max_len=160):
    encoding = tokenizer.encode_plus(
        data,
        add_special_tokens=True,
        max_length=max_len,
        return_token_type_ids=False,
        pad_to_max_length=True,
        return_attention_mask=True,
        return_tensors="pt",
        )
    return {
        "text" : data,
        "input_ids": encoding["input_ids"].flatten(),
        "attention_mask": encoding["attention_mask"].flatten(),
    }
