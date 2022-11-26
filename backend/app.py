from asyncore import write
from crypt import methods
from flask import Flask, redirect
from flask import render_template
from flask import request
from flask import Response
from flask import session
from flask import Flask
from flask import flash
from flask import send_from_directory
from werkzeug.utils import secure_filename
import os

from flask import url_for
from Etsi import Etsi

app = Flask(__name__)
app.secret_key = "test"
os.chdir('/var/www/html/kotisivut')
UPLOAD_FOLDER = os.getcwd() + "/minun"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


@app.route('/')
@app.route('/index.html')
def hello_world():
   return render_template('index.html')


@app.route("/test")
def testi():
    cwd = os.getcwd()
    return Response(cwd, mimetype="text/plain")




@app.route('/sanajahti', methods=['GET', 'POST'])
def sanajahti():
    #print(foundWords)
    if request.method == 'GET':
        print("IN GET")
        return render_template('sanajahti.html')
    if request.method == 'POST':
        print("IN POST")
        input_letters = request.form.get("input_letters")
        #input_letters = []

        lettersForEtsi = []
      

        for x in range(1,len(input_letters)):
            previous = x -1
            if(input_letters[previous]=='='):
                lettersForEtsi.append(input_letters[x])

        if len(lettersForEtsi) != 16:
            return ('', 204)

        foundWords = Etsi(lettersForEtsi)
        foundWords = foundWords.foundWords
        #print(foundWords)
        writeOrReadWordsFound("write", foundWords)
        return('', 204)

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route("/wordsFound")
def wordsFound():
    wf = writeOrReadWordsFound("read")
    return Response(wf, mimetype="text/plain")

@app.route("/wordle")
def wordle():
    return render_template("wordle.html")

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        if user == "manteli":
            session["user"] = user
            return redirect(url_for("controls"))

    return render_template("login.html")

@app.route("/controls", methods=["POST", "GET"])
def controls():
    if request.method == "GET":
        if "user" in session:
            return render_template("controls.html")
    
    if request.method == "POST":
        towrite = request.form.get("datatoput")
        print(towrite)
        writeOrReadWordsFound("write", towrite=towrite, filepath="mulle.txt")
        return('', 204)
    return redirect(url_for("login"))

@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("login"))

@app.route("/myFile")
def myFile():
    if "user" in session:
        mf = writeOrReadWordsFound("read",filepath="mulle.txt")
        print(mf)
        return Response(mf, mimetype="text/plain")
    return('', 204)



#File uploads
def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if "user" not in session:
        return redirect(url_for("login"))
    if request.method == 'POST':
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['file']
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            flash("not supported file type")
            return redirect(url_for('download_file', name=filename))
    return '''
    <!doctype html>
    <form method=post enctype=multipart/form-data>
      <input type=file name=file>
      <input type=submit value=Upload>
    </form>
    '''
@app.route('/upload/<name>')
def download_file(name):
    if "user" not in session:
        return redirect(url_for("login"))
    
    return send_from_directory(app.config["UPLOAD_FOLDER"], name)

      
def writeOrReadWordsFound(writeOrRead, towrite=None, filepath="wordsFound.txt"):
    #filepath = "wordsFound.txt"
    if(writeOrRead=="read"):
        file = open(filepath, encoding="utf-8", mode="r")
        found = ""
        for item in file:
            found += str(item)
        print("Luettu tiedosto")
        file.close()
        return found
    
    if(writeOrRead=="write"):
        file = open(filepath, encoding="utf-8", mode="w")
        file.write(towrite)
        print(towrite)
        print("Kirjoitettu tiedostoon")
        file.close()



if __name__ == '__main__':
    app.run(debug=True)

