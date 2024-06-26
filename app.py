from flask import Flask, render_template, request
import spacy

app = Flask(__name__)

# Load spaCy model
nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    entities = [(entity.text, entity.label_) for entity in doc.ents]
    return entities

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    text = request.form['text']
    entities = extract_entities(text)
    return render_template('index.html', entities=entities, text=text)

if __name__ == '__main__':
    app.run(debug=True)
