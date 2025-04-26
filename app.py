from flask import Flask, request, render_template, jsonify
import language_tool_python
import logging

app = Flask(__name__)
tool = language_tool_python.LanguageTool('en-US')
logging.basicConfig(level=logging.INFO)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/correct', methods=['POST'])
def correct_sentence():
    sentence = request.form.get('sentence', '').strip()
    if not sentence:
        return jsonify({'error': 'Please enter a valid sentence.'})

    try:
        app.logger.info(f"User Input: {sentence}")
        corrected = tool.correct(sentence)
        app.logger.info(f"Corrected Output: {corrected}")
        return jsonify({'original': sentence, 'corrected': corrected})
    except Exception as e:
        app.logger.error(f"Error during correction: {str(e)}")
        return jsonify({'error': 'An error occurred while processing your sentence.'})

if __name__ == '__main__':
    app.run(debug=True)

