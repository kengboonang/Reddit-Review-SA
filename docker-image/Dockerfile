FROM python:3.8
WORKDIR /src
COPY . /src
RUN pip install -r requirements.txt
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
ENTRYPOINT ["python", "-m", "streamlit", "run", "src/streamlit_app.py", "--server.port=8501", "--server.address=0.0.0.0"]