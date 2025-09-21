# backend/app.py
import time
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
from bs4 import BeautifulSoup

app = Flask(__name__)
CORS(app)

# --- ADVANCED SIMULATION ENGINE ---
def get_advanced_simulated_analysis(text, url):
    print("Simulating ADVANCED AI analysis...")
    time.sleep(2) # Simulate the AI thinking

    # 1. Source Reputation Check
    known_sources = {
        "wikipedia.org": "High (Factual Encyclopedia)",
        "reuters.com": "High (International News Agency)",
        "apnews.com": "High (International News Agency)",
        "indiatimes.com": "Medium (Major News Publisher)",
        "thehindu.com": "Medium (Major News Publisher)"
    }
    source_reputation = "Unknown"
    for source, reputation in known_sources.items():
        if source in url:
            source_reputation = reputation
            break

    # 2. Emotional Language Check (Basic Sentiment)
    sensational_words = ['shocking', 'outrageous', 'unbelievable', 'miracle', 'worst', 'disaster', 'scandal']
    sensational_word_count = sum(text.lower().count(word) for word in sensational_words)
    emotional_tone = "Neutral"
    if sensational_word_count > 2:
        emotional_tone = "Sensationalized / Emotionally Charged"

    # 3. Subjective Language Check
    opinion_words = ['believe', 'feel', 'seems', 'apparently', 'could', 'might']
    opinion_word_count = sum(text.lower().count(word) for word in opinion_words)
    objectivity_level = "High"
    if opinion_word_count > 5:
        objectivity_level = "Low (Contains Speculative Language)"
        
    # 4. Generate the final report based on the checks
    report = f"""
    SIMULATED ANALYSIS REPORT:
    - Source Reputation: {source_reputation}.
    - Tone Analysis: The text's tone appears to be largely {emotional_tone.lower()}.
    - Objectivity Level: {objectivity_level}.
    - Summary: This article's content should be read with the above factors in mind. Sources with a high reputation and neutral tone are generally more reliable.
    """
    return report
# --- END OF SIMULATION ENGINE ---

@app.route('/analyze', methods=['POST'])
def analyze():
    data = request.get_json()
    url = data.get('url')
    if not url: return jsonify({"error": "URL is required"}), 400

    try:
        headers = {'User-Agent': 'Mozilla/5.0'}
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.content, 'html.parser')
        title = soup.find('h1').get_text(strip=True) if soup.find('h1') else 'No title found'
        paragraphs = soup.find_all('p')
        article_text = ' '.join([p.get_text(strip=True) for p in paragraphs])

        ai_summary = get_advanced_simulated_analysis(article_text, url)

        return jsonify({
            "status": "success",
            "title": title,
            "scraped_text_preview": article_text[:500] + "...",
            "ai_analysis": ai_summary 
        })
    except Exception as e:
        return jsonify({"error": f"An error occurred: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)