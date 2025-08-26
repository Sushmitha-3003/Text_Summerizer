📄 Text Summarizer App
This is a Streamlit application that provides an easy-to-use interface for summarizing text from .txt and .pdf files using a pre-trained BART model. The app allows you to upload a file and instantly get an abstractive summary.

Live Demo :https://textsummerizer-fzzbxs6gfzke7fhgwlwb2f.streamlit.app/

✨ Features
File Upload: Supports .txt and .pdf files.

Abstractive Summarization: Uses a BART model (sshleifer/distilbart-cnn-12-6) to generate a concise summary.

User-Friendly Interface: A clean and simple web interface powered by Streamlit.

🚀 Getting Started
Prerequisites
You need to have Python installed on your system. It's recommended to use a virtual environment.

Installation
Clone the repository:

git clone <your-repository-url>
cd <your-repository-name>

Create and activate a virtual environment:

python -m venv venv
# On Windows
venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

Install the required libraries:
The project relies on a few key libraries. You can install them all at once using the requirements.txt file.

pip install -r requirements.txt

Note: Based on your recent work, I've created an updated requirements.txt to avoid dependency issues.

How to Run
After setting up your environment and installing the dependencies, you can run the app with this command:

streamlit run app.py

This will start a local web server and open the application in your default web browser.

📂 Project Structure
app.py: The main Streamlit application file.

requirements.txt: A list of Python dependencies.

src/: A directory for source code.

data_loader.py: Handles loading text from different file types.

preprocess.py: Contains functions for text cleaning and preprocessing.

summarizers/: Contains the summarization models.

bart_summarizer.py: The script for the BERT summarizer.

🤝 Contributing
Feel free to open an issue or submit a pull request if you'd like to improve this project.

📄 License
This project is licensed under the MIT License.

