# Simple Sundanese Translator
Simple Sundanese to Bahasa Indonesia translator using Pattern Matching

## Latar Belakang
Pada suatu hari, ada mahasiswa bernama Riyugan yang baru pindah ke Bandung. Pada awalnya dia mengalami kesulitan untuk bersosialisai dengan lingkungan sekitar karena orang-orang di lingkungannya yang baru hanya berbicara dalam bahasa Sunda. Beruntungnya Riyugan punya teman dari kampung halamannya, yaitu Anda, untuk diminta membuat penerjemah sederhana dari Bahasa Sunda ke Bahasa Indonesia begitu pula sebaliknya untuk memudahkan dirinya bersosialisasi dengan lingkungan barunya di Bandung.

## Spesifikasi
Buatlah dalam bahasa pemrograman Python, program penerjemah sederhana yang memanfaatkan algoritma String Matching (Knuth-Morris-Pratt(KMP), Boyer-Moore(BM), dan Regex), dengan spesifikasi sebagai berikut.
1. Program mampu membaca kata atau kalimat yang akan diterjemahkan.
2. Program akan membaca file eksternal yang berisi vocabulary Bahasa Sunda - Bahasa Indonesia (file sudah disiapkan dalam repository).
3. Program akan melakukan penerjemahan secara perkata (untuk contoh akan ditampilkan di bawah).
4. Program dapat memilih mau "Bahasa Sunda ke Bahasa Indonesia" atau "Bahasa Indonesia ke Bahasa Sunda".
5. Pada saat penerjemahan "Bahasa Sunda ke Bahasa Indonesia", program mampu mengenali kata yang tidak memiliki arti (stopwords), seperti "teh" sehingga dapat diabaikan saat penerjemahan.
6. Pada saat penerjemahan "Bahasa Indonesia ke Bahasa Sunda", program mampu menambahkan kata untuk penekanan kalimat, seperti "teh".
7. Program dapat menampilkan hasil terjemahan.
8. Program dibuat secara individu.
9. Peserta akan mendapatkan nilai bonus jika mengimplementasikan dalam web (untuk bahasanya dibebaskan).
10. Dilarang meng-copy source code program yang sudah jadi, untuk source code algoritma string matching dipersilahkan menggunakan source code dari tugas yang sudah pernah dibuat (Tugas Kecil 4).
11. Batas pengerjaannya adalah 6 Juni 2020.

## Contoh Kasus Uji
```
Sunda - Indonesia
Sunda : nami abdi Riyugan
Indonesia : nama saya Riyugan
```

```
Sunda - Indonesia
Sunda : abdi teh sanes jalma Bandung
Indonesia : saya bukan orang Bandung
```

```
Sunda - Indonesia
Sunda : anjeun sumping ti mana?
Indonesia : kamu tiba dari mana?
```

```
Indonesia - Sunda
Indonesia : nama saya Riyugan
Sunda : nami abdi Riyugan
```

```
Indonesia - Sunda
Indonesia : nama adik kamu siapa?
Sunda : nami rai anjeun teh saha?
```

```
Indonesia - Sunda
Indonesia : saya tidak bisa bahasa Sunda
Sunda : abdi henteu tiasa bahasa Sunda
```


## Author
Felicia Gojali NIM 13518101

## Prerequisites
To compile and run this program, there're some prerequisites that're needed to be completed. I assume that python 2.6 or higher and pip has been installed in your OS. 

1. Install virtualenv for development environment

The following command installs virtualenv

```
pip install virtualenv
```

This command needs administrator privileges. Add sudo before pip on Linux/Mac OS. If you are on Windows, log in as Administrator. On Ubuntu virtualenv may be installed using its package manager.

```
Sudo apt-get install virtualenv
```

Once installed, new virtual environment is created in my src folder

```
virualenv venv
```

To activate corresponding environment, on Linux/OS X, use the following −

```
venv/bin/activate
```

On Windows, following can be used

```
venv\scripts\activate

```
We are now ready to install Flask in this environment.

```
pip install Flask
```
and Done!




## Compiling & Running

After completing all the prerequisites above, you should be able to compile and run the program main.py

1. Enter the src folder
2. Open terminal
```
python main.py
```
3. After it finished, there should be a local host address in the terminal
4. Open it in browser and don't forget to put '/home' at the end
5. Done!

## How To Use

The program is made to read the database from the 'txt' folder, so if you in any case want to change the database or update it, please change inside the indonesia.txt and sunda.txt without renaming the files.

1. Choose which translation you want to do, either Indonesian-Sundanese or Sundanese-Indonesian
2. Choose which algorithm method you want to use for the translation, there are three methods available: KMP, BM, and regex
3. Enter the words or sentences you want to translate in the provided box, then enter submit
4. Voila!

## Video
Youtube video link : 
https://youtu.be/m84x6dOKK0Y

## Screenshot program



