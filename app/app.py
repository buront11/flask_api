from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def hello_world():
    return '<h2>Hello Flask+uWSGI+Nginx</h2>'

@app.route('/api/convert_text', methods=['GET'])
def convert_text():
    text = request.args.get('text')
    json_text = {'text': text}
    return jsonify(json_text)

if __name__ == '__main__':
    app.run()