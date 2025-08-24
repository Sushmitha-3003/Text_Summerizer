import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize
import re

# Download necessary NLTK data
nltk.download('punkt', quiet=True)
nltk.download('stopwords', quiet=True)

def preprocess_text(text):
    """
    Cleans and preprocesses a given text.
    
    Args:
        text (str): The input string.
        
    Returns:
        A cleaned string.
    """
    # Convert text to lowercase
    clean_text = text.lower()
    
    # Remove special characters, but keep numbers and standard punctuation
    # This is a less aggressive approach that preserves more of the text's structure.
    clean_text = re.sub(r'[^a-zA-Z0-9\s\.\,\!\?]', '', clean_text)
    
    # Normalize multiple whitespace characters into a single space
    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
    
    return clean_text

def get_sentences(text):
    """
    Splits text into a list of sentences.
    
    Args:
        text (str): The input string.
        
    Returns:
        A list of sentences.
    """
    return sent_tokenize(text)

def get_stopwords():
    """Returns a set of English stopwords."""
    return set(stopwords.words('english'))

def save_processed_text(text, file_path):
    """
    Saves a string of text to a file.

    Args:
        text (str): The text to save.
        file_path (str): The path to the output file.
    """
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"Processed text saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the file: {e}")

