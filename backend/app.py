from flask import Flask, redirect
from flask import render_template
from flask import request
from flask import Response
from flask import session
from flask import Flask
from flask import jsonify
from flask import flash
from flask import send_from_directory
from werkzeug.utils import secure_filename
import json
import os
import sys
import stat
import pprint
import shutil

from flask import url_for
from Etsi import Etsi
from Wordle import Wordle

app = Flask(__name__)
app.secret_key = "seventeenthirtyeight"
os.chdir('/var/www/html/kotisivut')
UPLOAD_FOLDER = os.getcwd() + "/minun"
ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif','mp4','mp3','wav','doc','zip', 'm4b'}
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 1000 * 1000 * 1000 

sys.stdout = open("out.txt", "w")



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
        return render_template('sanajahti.html')
    if request.method == 'POST':
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
        wordDict = foundWords.wordDict
        #wordDict = dict(sorted(wordDict.items(), key=lambda key:len(key[0]), reverse=True))
        with open("wordsFound.json", "w") as output:
            json.dump(wordDict, output)
        
        foundWords = foundWords.foundWords
        
        #print(foundWords)
        writeOrReadWordsFound("write", foundWords)
        return('', 204)

@app.route("/jsonWordsFound")
def jsonWordsFound():
    with open("wordsFound.json", 'r') as infile:
        json_object = json.load(infile)
        
        return jsonify(json_object)


@app.route("/phase")
def phase():
    return render_template("phase.html")

@app.route('/about.html')
def about():
    return render_template('about.html')

@app.route("/wordsFound")
def wordsFound():
    wf = writeOrReadWordsFound("read")
    return Response(wf, mimetype="text/plain")


@app.route("/wordle", methods=["POST", "GET"])
def wordle():
    if request.method == "GET":
        eng_alpha = writeOrReadWordsFound("read",filepath="eng_alpha.txt")
        writeOrReadWordsFound("write", towrite=eng_alpha)
        return render_template("wordle.html",eng_alpha=eng_alpha)

    if request.method == "POST":
        
        input_letters_wordle = request.get_json()
        # print(input_letters_wordle)
        input_letters_wordle = input_letters_wordle["letterColorPair"]
        # print(input_letters_wordle)
        wordl = Wordle(input_letters_wordle, ongoing=True)
        words = str(wordl.parseWords())
        writeOrReadWordsFound("write", words)
        return('', 204)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form.get("username")
        if user == os.environ['MY_CREDS']:
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
            
            return redirect(request.url)

        makeFolder = request.form.get("teeKansio")
        folderName = request.form.get("kansioNimi")
        makeZip = request.form.get("teeZip")
        if makeFolder:
            if len(folderName) == 0:
                folderName = "DefaultName"
            os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], folderName))
            os.chmod(os.path.join(app.config['UPLOAD_FOLDER'], folderName), 0o777)
            os.mkdir(os.path.join(app.config['UPLOAD_FOLDER'], folderName, folderName)) 
            os.chmod(os.path.join(app.config['UPLOAD_FOLDER'], folderName, folderName), 0o777)

        files = request.files.getlist('file')
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        
        for file in files:
            if file.filename == '':
                
                return redirect(request.url)
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                if makeFolder:
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], folderName, folderName, filename))
                    if(makeZip):
                        archived = shutil.make_archive(os.path.join(app.config['UPLOAD_FOLDER'], folderName), 'zip',os.path.join(app.config['UPLOAD_FOLDER'], folderName) )
                else:
                    file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                
        return redirect(url_for('files'))
    return render_template("upload.html")

@app.route("/files")
def files():
    if "user" not in session:
        return redirect(url_for("login"))    
    files = os.listdir("./minun")

    return render_template("files.html", listFiles=files)


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
        
        file.close()
        return found
    
    if(writeOrRead=="write"):
        file = open(filepath, encoding="utf-8", mode="w")
        file.write(towrite)
        
        file.close()



if __name__ == '__main__':
    app.run(debug=True)

