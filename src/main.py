from flask import Flask, redirect, url_for, request,render_template
from function import *
import re

app = Flask(__name__)

@app.route('/home')
def upload_file():
   return render_template('login.html')

@app.route('/upload',methods = ['POST', 'GET'])
def login():
    if request.method == 'POST':
        print("halo")
        # menerima algoritman mana yang digunakan dari radio button
        language = request.form['language']
        method = request.form['method']
        # menerima kalimat
        kword = request.form['kw']
        print(language)
        print(method)
        return output(kword,language,method)

def output(words,language,method):
    words = words.lower()

    # membaca tiap file tiap baris
    db = database('txt/sunda.txt','txt/indonesia.txt')
   
    #parsing kalimat inputan jadi kata
    kata = words.split(' ')
    
    #cocokkan tiap kata dengan dictionary yang sudah ada
    if (language == '0'):
        x = 0
        y = 1
        a = "Sundanese"
        b = "Indonesian"
    else :
        x = 1
        y = 0
        b = "Sundanese"
        a = "Indonesian"
    print("halo")
    answ = []
    answ = translate(kata,db,method,x,y)
    #pengecekan penggunaan kata teh jika translate indo-sunda
    if(language == '1'):
        # menggunakan regex
        i = 0
        while (i < len(answ)):
            # menambahkan teh di sebelah kiri kata
            if (useTehLeft(answ[i])):
                if (KMPalgo(answ[i-1],"teh") == -1):
                    j = len(answ) - 1
                    answ.append(' ')
                    while (j >= i):
                        answ[j+1] = answ[j]
                        j -= 1
                    answ[i] = "teh"
            # menambahkan teh di sebelah kanan kata
            if (useTehRight(answ[i]) and i != len(answ) - 1):
                if (BMAlgo(answ[i+1],"teh") == -1):
                    j = len(answ) - 1
                    answ.append(' ')
                    while (j > i):
                        answ[j+1] = answ[j]
                        j -= 1
                    answ[i+1] = "teh"
            i+=1
    if (answ == []):
        return "Tidak ada jawaban"
    else :
        ans = ' '.join(answ)
        return render_template("answer.html",ans=ans,words=words,a=a,b=b)


if __name__ == '__main__':
   app.run(debug = True)