# src/summarizers/bert_summarizer.py

from summarizer import Summarizer

def summarize_bert(text, num_sentences=3):
    """
    Generates an extractive summary of a text using a BERT-based model.
    """
    if not text:
        return ""
    
    # Initialize the BERT extractive summarizer
    # This uses a pre-trained BERT model to create sentence embeddings
    model = Summarizer()
    
    # Generate the summary by selecting the top sentences
    # The summarizer selects sentences that are most representative of the text
    summary = model(text, num_sentences=num_sentences)
    
    # The output is a string, no need for extra processing
    return summary