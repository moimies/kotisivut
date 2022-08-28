from asyncore import write
from flask import Flask, redirect
from flask import render_template
from flask import request
from flask import Response

from flask import url_for
from Etsi import Etsi

app = Flask(__name__)



@app.route('/')
@app.route('/index.html')
def hello_world():
   return render_template('index.html')




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


      
def writeOrReadWordsFound(writeOrRead, towrite=None):
    filepath = "wordsFound.txt"
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
        print(towrite)
        print("Kirjoitettu tiedostoon")
        file.close()



if __name__ == '__main__':
   app.run(debug=True)

