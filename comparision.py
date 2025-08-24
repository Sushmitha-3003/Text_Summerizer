import sys
import os
from src.data_loader import load_text_from_file
from src.summarizers.tfidf_summarizer import summarize_tfidf
from src.summarizers.bert_summarizer import summarize_bert
from src.summarizers.bart_summarizer import summarize_bart

def save_comparison_output(results, original_text, output_dir="data/comparisons"):
    """
    Saves a text file with a side-by-side comparison of summaries and the original text.
    """
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    file_name = f"summary_comparison_{os.path.basename(sys.argv[1]).split('.')[0]}.txt"
    output_path = os.path.join(output_dir, file_name)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write("--- Original Text ---\n")
        f.write(original_text[:1000] + "...\n\n") # Save first 1000 chars of original text
        
        for model_name, summary in results.items():
            f.write(f"--- {model_name.upper()} Summary ---\n")
            f.write(summary)
            f.write("\n\n")
            
    print(f"\nComparison report saved to: {output_path}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python run_comparison.py <path_to_file>")
        return

    file_path = sys.argv[1]
    
    print(f"Loading and summarizing text from {file_path}...")
    article = load_text_from_file(file_path)

    if not article:
        print("Error: Could not load the article.")
        return

    results = {}

    # Run TF-IDF Summarizer
    print("Running TF-IDF summarizer...")
    results['tfidf'] = summarize_tfidf(article)

    # Run BERT Extractive Summarizer
    print("Running BERT (Extractive) summarizer...")
    results['bert'] = summarize_bert(article)

    # Run BART Abstractive Summarizer
    print("Running BART (Abstractive) summarizer...")
    results['bart'] = summarize_bart(article)
    
    # Save the results to a single file
    save_comparison_output(results, article)

    print("\n--- Summary Outputs ---\n")
    for model, summary in results.items():
        print(f"**{model.upper()} Summary:**")
        print(summary)
        print("-" * 20)
        
if __name__ == "__main__":
    main()