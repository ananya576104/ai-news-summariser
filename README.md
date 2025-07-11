# AI News Summariser

AI News Summariser is a Flask-based web app that extracts news articles from any public URL, summarizes the content in the original language, and then translates that summary into English using Google Translate.

> Supports articles in **Telugu, Hindi, Bengali, Tamil, Kannada, Marathi, and more.

---

## Features

-  Accepts any valid news URL
-  Automatically extracts full article text
-  Summarizes the article in the **original language**
-  Translates the summary to **English**
-  Displays the article’s title, source, image, and both summaries
-  Mobile-friendly UI using Bootstrap 5

---

##  Tech Stack

- Python 3.9+
- Flask
- [trafilatura](https://github.com/adbar/trafilatura) – for web article extraction
- [deep-translator](https://github.com/nidhaloff/deep-translator) – Google Translate support
- NLTK – for sentence tokenization
- Bootstrap 5 – modern responsive UI

---

##  Installation

```bash
# Clone the repo
git clone https://github.com/ananya576104/ai-news-summariser.git
cd ai-news-summariser

# Create and activate a virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
