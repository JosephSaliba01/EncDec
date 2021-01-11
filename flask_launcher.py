import os
from flask import Flask, render_template, request
from werkzeug.utils import secure_filename

def encrypt(key, f):
    output_path = os.getcwd() + "\\output\\encrypted_files"

    for line in f:
        line = line.strip()
        print(line)
        key_str = key
        while len(line) > len(key_str):
            key_str += key
        key_str = key_str[0:len(line)]
        print(key_str)

    f.save(os.path.join(output_path, secure_filename(f.filename[0:-4] + "_ENC.txt")))

################################################################################

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = os.getcwd() + "\\output"
print("Output path set to '" + app.config['UPLOAD_FOLDER'] + "'")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/', methods = ['GET', 'POST'])
def upload_file():
    f = request.files['infile']
    key = request.form['key']
    #f.save(os.path.join(app.config['UPLOAD_FOLDER'], secure_filename(f.filename)))
    encrypt(key.upper(), f)
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)
