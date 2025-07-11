from flask import Flask, request, render_template, flash, redirect, url_for
import nltk
import trafilatura
from urllib.parse import urlparse
import validators
import requests
import json
from translator import translate_to_english
from bs4 import BeautifulSoup

nltk.download('punkt')

app = Flask(__name__)
app.secret_key = 'your_secret_key'

def get_website_name(url):
    parsed_url = urlparse(url)
    domain = parsed_url.netloc
    if domain.startswith("www."):
        domain = domain[4:]
    return domain

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        url = request.form['url']

        if not validators.url(url):
            flash('Please enter a valid URL.')
            return redirect(url_for('index'))

        try:
            downloaded_html = trafilatura.fetch_url(url)
            if not downloaded_html:
                flash("Could not download the article.")
                return redirect(url_for('index'))

            extracted = trafilatura.extract(downloaded_html, include_images=True, output_format='json')
            if not extracted:
                flash("Could not extract article content.")
                return redirect(url_for('index'))

            data = json.loads(extracted)
            article_text = data.get('text', '')
            title = data.get('title', '').strip()
            if title.lower() == 'untitled':
                title = ''
            authors = get_website_name(url)

            # Image logic
            top_image = data.get('image', '')
            if not top_image:
                soup = BeautifulSoup(downloaded_html, 'html.parser')
                og_image = soup.find('meta', property='og:image')
                if og_image and og_image.get('content'):
                    top_image = og_image['content']

        except Exception as e:
            print("Extraction error:", e)
            flash("Error extracting content.")
            return redirect(url_for('index'))

        if not article_text.strip():
            flash("Could not extract article content.")
            return redirect(url_for('index'))

        try:
            sentences = nltk.sent_tokenize(article_text)
            original_summary = ' '.join(sentences[:5])
            translated_summary = translate_to_english(original_summary)
        except Exception as e:
            print("Translation error:", e)
            flash("Translation failed.")
            return redirect(url_for('index'))

        if not translated_summary.strip():
            flash("Summary translation returned empty.")
            return redirect(url_for('index'))

        return render_template('index.html', title=title, authors=authors,
                               summary_en=translated_summary,
                               summary_original=original_summary, top_image=top_image)

    return render_template('index.html')
if __name__ == '__main__':
    app.run(debug=True)
