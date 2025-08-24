# main.py
import sys
import os
from src.data_loader import load_text_from_file, save_original_text
from src.preprocess import preprocess_text, save_processed_text
from src.summarizers.bert_summarizer import summarize_bert

def save_summary(text, file_path):
    """Saves a summary to a text file."""
    output_dir = os.path.dirname(file_path)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    try:
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(text)
        print(f"\nSummary saved to {file_path}")
    except Exception as e:
        print(f"An error occurred while saving the summary: {e}")

def main():
    """Runs the text summarization pipeline for a single model (BART)."""
    
    # Check for file path argument only
    if len(sys.argv) < 2:
        print("Usage: python main.py <path_to_file>")
        return

    file_path = sys.argv[1]
    
    print(f"Loading text from {file_path}...")
    article = load_text_from_file(file_path)

    if article:
        # Get file name and define paths
        base_name = os.path.basename(file_path)
        name, extension = os.path.splitext(base_name)
        
        original_file_path = f"data/raw/original_{name}.txt"
        processed_file_path = f"data/processed/cleaned_{name}.txt"
        summary_output_path = f"data/summaries/summary_bart_{name}.txt"

        # Save original and processed text
        save_original_text(article, original_file_path)
        cleaned_text = preprocess_text(article)
        save_processed_text(cleaned_text, processed_file_path)
        
        # Run the single chosen summarizer (BART)
        print("\nUsing **BART** for summarization...")
        summary = summarize_bert(article)
        
        # Save the generated summary
        save_summary(summary, summary_output_path)
        
        # Print the results
        print("\n--- Generated Summary ---")
        print(summary)
        print("-------------------------")
    else:
        print("Could not proceed with summarization due to a loading error.")

if __name__ == '__main__':
    main()