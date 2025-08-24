# src/summarizers/bart_summarizer.py

from transformers import pipeline
import nltk
from nltk.tokenize import sent_tokenize
import sys
import os
import re

# Add the parent directory to the path to import preprocess.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocess import preprocess_text

# Download necessary NLTK data if not already downloaded
try:
    nltk.data.find('tokenizers/punkt')
except nltk.downloader.DownloadError:
    nltk.download('punkt', quiet=True)

def summarize_bart(text, num_sentences=3):
    """
    Generates an abstractive summary of a text using a BART model.
    """
    # Check if the text is a string and not empty or only whitespace
    if not isinstance(text, str) or len(text.strip()) == 0:
        return ""
    
    # Use a pre-trained BART model fine-tuned for summarization.
    try:
        summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")

        # The pipeline has a token limit, so we handle long texts by truncating.
        max_len = 2048
        if len(text.split()) > max_len:
            text = " ".join(text.split()[:max_len])
        
        # Generate the summary
        # The max_length has been increased to allow for a longer summary.
        summary = summarizer(text, max_length=200, min_length=50, do_sample=False)
        
        # The output is a list of dictionaries, so we extract the summary text.
        return summary[0]['summary_text']
    except Exception as e:
        print(f"Error during BART summarization: {e}")
        # Return an empty string to trigger the fallback in app.py
        return ""
