import os
from flask import *
from convertfasta import convertfasta
import proteinfinder

app = Flask(__name__)


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/convert')
def convert():
    return render_template("convert.html")


@app.route('/converted', methods=['POST'])
def converted():
    if request.method == 'POST':
        f = request.files['file']
        f.save(f.filename)
        convertfasta()
        return render_template("success.html", name="output.fasta")


@app.route('/output.fasta', methods=['GET'])
def download():
    root = os.path.join(current_app.root_path)
    return send_from_directory(directory=root, filename='output.fasta')


@app.route('/proteinfind', methods=['GET', 'POST'])
def proteinfind():
    if request.method == 'GET':
        return render_template("proteinfind.html")
    if request.method == 'POST':
        f = request.files['file']
        sequence = request.form['sequence']
        f.save(f.filename)
        proteinfinder.proteinfind(sequence, f.filename, "proteome")
        return render_template("success.html", name="outputproteome.fasta")


@app.route('/outputproteome.fasta', methods=['GET'])
def downloadsecond():
    root = os.path.join(current_app.root_path)
    return send_from_directory(directory=root, filename='outputproteome.fasta')


@app.route('/outputdna.fasta', methods=['GET'])
def downloadthird():
    root = os.path.join(current_app.root_path)
    return send_from_directory(directory=root, filename='outputdna.fasta')


@app.route('/dnafind', methods=['GET', 'POST'])
def dnafind():
    if request.method == 'GET':
        return render_template("dnafind.html")
    if request.method == 'POST':
        f = request.files['file']
        sequence = request.form['sequence']
        f.save(f.filename)
        proteinfinder.proteinfind(sequence, f.filename, "dna")
        return render_template("success.html", name="outputdna.fasta")


if __name__ == '__main__':
    app.run(debug=True)
