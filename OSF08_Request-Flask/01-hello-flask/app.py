from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
import os

app = Flask(__name__)


model_cache = {
    1: 1,
    4: 2,
    9: 3
}

@app.route('/')
def index():
    return "It's alive!"


@app.route('/ruok')
def ruok():
    return 'yes...'


@app.route('/sqrt', methods=['POST'])
def sqrt():
    n = request.json['n']
    return jsonify(sqrt=model_cache[n])


@app.route('/echo', methods=['POST'])
def echo():
    is_upper = request.args.get('uppercase', False)
    data = request.form['data']
    if is_upper:
        data = data.upper()
    else:
        data = data.lower()
    return jsonify({'data': data})


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['image']
    filename = (file.filename)
    file.save(os.path.join('uploads', filename))
    return jsonify(status='success')


@app.route('/user/<user_id>')
def get_user(user_id):
    return jsonify(err="Can't find {}".format(user_id)), 404


@app.route('/info', methods=['GET', 'POST'])
def info():
    return jsonify({
        'method': request.method,
        'url': request.url,
        'form': request.form.to_dict(),
        'json': request.json,
        'args': request.args
    })


if __name__ == '__main__':
    app.run(
        host = '127.0.0.1',
        port = 5000
    )