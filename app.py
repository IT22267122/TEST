from flask import Flask, request, jsonify,render_template
from test import summarize_large_text,analyze_sentiment,extract_keywords_from_large_text,topic_modeling_on_large_texts

# Initialize the Flask app
app = Flask(__name__)

# Flask routes

@app.route('/')
def index():
    return render_template('index.html')

# Route for summarizing text
@app.route('/summarize', methods=['POST'])
def summarize():
    data = request.json
    text = data.get('text', '')
    max_length = data.get('max_length', 150)  # Default to 150 if no length is provided

    if text:
        # Pass max_length to the summarization function
        summary = summarize_large_text(text, max_length=max_length)
        return jsonify(summary)
    return jsonify({"error": "No text provided"}), 400

# Route for sentiment analysis
@app.route('/sentiment', methods=['POST'])
def sentiment():
    data = request.json
    text = data.get('text', '')
    if text:
        sentiment_scores = analyze_sentiment(text)
        return jsonify(sentiment_scores)
    return jsonify({"error": "No text provided"}), 400

# Route for keyword extraction
@app.route('/keywords', methods=['POST'])
def keywords():
    data = request.json
    text = data.get('text', '')
    if text:
        keywords = extract_keywords_from_large_text(text)
        return jsonify(keywords)
    return jsonify({"error": "No text provided"}), 400

# Route for topic modeling
@app.route('/topics', methods=['POST'])
def topics():
    data = request.json
    texts = data.get('texts', [])
    if texts:
        topics = topic_modeling_on_large_texts(texts)
        return jsonify(topics)
    return jsonify({"error": "No text provided"}), 400

# Main function to run Flask app
if __name__ == '__main__':
    app.run(debug=True)
