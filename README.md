# Reddit Reviews Sentiment Analysis

Personal project to work on an NLP project and also to create something usable for people to interact with.

How to use:
- General Steps
    - download requirements.txt
    - Load tokenizer file inside models directory
    - login to Hugging Face using CLI "huggingface-cli login"
- HTML with Flask App
    - run "python main.py"
- Streamlit App
    - run "streamlit run streamlit_app.py

Current Tech Stack:
- Sentiment Analysis Model:
  - HuggingFace Base SA
  - BERT finetuned on Yelp Reviews

- Frontend:
  - HTML
  - Streamlit
    
- Backend:
  - Selenium to scrape posts from Reddit
  - Flask to route requests

Todos:
- Test different LLMs i.e. DistilBert, BART, FlanT5
- Finetune on different datasets i.e. Amazon Product Reviews
- Scrape other urls
