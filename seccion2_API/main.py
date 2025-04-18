from flask import Flask, request, render_template, jsonify
from app.number_set import NumberSet
import os

template_dir = os.path.join(os.path.dirname(__file__), 'app', 'templates')
static_dir = os.path.join(os.path.dirname(__file__), 'app', 'static')

app = Flask(__name__, template_folder=template_dir, static_folder=static_dir)

number_set = NumberSet()

@app.route('/', methods=['GET', 'POST'])
def index():
    extracted = number_set.get_extracted_numbers()
    return render_template('index.html', extracted=extracted)

@app.route('/api/extract', methods=['POST'])
def api_extract():
    data = request.json
    try:
        number = int(data.get('number'))
        extracted = number_set.extract(number)
        return jsonify({
            "extracted": extracted, 
            "all_extracted": number_set.get_extracted_numbers()
        }), 200
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)