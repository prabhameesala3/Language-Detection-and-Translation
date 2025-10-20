from flask import Flask, render_template, request
from googletrans import Translator, LANGUAGES

app = Flask(__name__)
translator = Translator()

@app.route('/')
def index():
    return render_template('index.html', languages=LANGUAGES)


@app.route('/trans', methods=['POST'])
def trans():
    text = request.form['text']
    target_lang = request.form['target_lang']


    translated = translator.translate(text, dest=target_lang)


    detected = translator.detect(text)
    detected_code = detected.lang
    detected_name = LANGUAGES.get(detected_code, detected_code).title()

    return render_template('index.html',
                           original_text=text,
                           translation=translated.text,
                           detected_lang=detected_name,
                           selected_lang=target_lang,
                           languages=LANGUAGES)

@app.route('/detect', methods=['POST'])
def detect_language():
    text = request.form['text']

    detected = translator.detect(text)
    detected_code = detected.lang
    detected_name = LANGUAGES.get(detected_code, detected_code).title()

    return render_template('index.html',
                           original_text=text,
                           detected_lang=detected_name,
                           languages=LANGUAGES)
if __name__ == "__main__":
    app.run(debug=True, port=5500)