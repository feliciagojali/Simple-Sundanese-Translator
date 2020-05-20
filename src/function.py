import re

def translate(kata,db,method,x,y):
    i = 0
    answ = []
    td = []
    while (i < len(kata)):
   
        #cek dengan string matching di dictionary
        j = 0
        if (i == len(kata) - 1):
            boolean,td,rest = contains(kata[i])
            if (boolean):
                kata[i] = rest
            
        while (j < len(db)):

            if (algo(kata[i],db[j][x],method) == 0 and len(kata[i])==len(db[j][x])):
                # menggunakan kmp algorithm
                print(kata[i])
                answ.append(db[j][y])
                break
            j += 1

        if (j == len(db)):
            # tidak ketemu di keduanya
            if (i == 0 or algo(kata[i],"teh",method) == -1 or i == len(kata)-1):
                answ.append(kata[i])

           
            else :
                if(not useTehLeft(kata[i+1]) and not useTehRight(kata[i-1])):
                    answ.append(kata[i])
        if (td!=[]):
            answ.append(td)
        
        i+=1
    
    return answ

def algo(kata,db,method):
    if (method == '0'):
        return KMPalgo(kata,db)
    elif (method == '1'):
        return BMAlgo(kata,db)
    else :
        x = re.search(kata,db)
        if (x):
            return x.span()[0]
        else :
            return -1

def database(sunda,indo):
    
    word_sunda = []
    word_indo = []
    db = []
    with open(sunda,'r') as file:
        word_sunda = file.readlines()

    with open(indo,'r') as file:
        word_indo = file.readlines()

     # split into dictionary
    i = 0
    j = 0
    while (i < len(word_sunda) or j < len(word_indo)) :
        if (i != len(word_sunda)):
            sentence = re.split("\n",word_sunda[i])
            word = sentence[0].split(' = ')
            db.append(word)
            i+=1
        if (j != len(word_indo)):
            sentence = re.split("\n",word_indo[j])
            word = sentence[0].split(' = ')
            temp = word[0]
            word[0] = word[1]
            word[1] = temp
            db.append(word)
            j+=1
    
    return db
    

def contains(text):
    x = re.search("[.]|[?]|[!]",text)

    if (x):
        y = re.split("[.]|[?]|[!]",text)
        td = text[x.span()[0]]
        return True,td,y[0]
    else:
        return False,[],[]


def useTehRight(text):
    x = re.findall("abdi|urang|anjeun|manehna|aranjeun|maranehna",text)
    if (x != []):
        return True
    else :
        return False
    


def useTehLeft(text):
    x = re.findall("naon|saha|timanten|sabaraha|mana|kunaon|kumaha",text)
    if (x != []):
        return True
    else:
        return False
        

def min (a,b):
    if (a < b):
        return a
    else:
        return b 


def KMPalgo(text,pattern):
    n = len(text)
    m = len(pattern)
    array = computeArray(pattern)
    i = 0
    j = 0

    while ( i < n ):
        
        if (text[i] == pattern[j]):
            if (j == m-1):
                return i - m + 1
            i += 1
            j += 1
        elif (j > 0):
            j = array[j-1]
        else :
            i += 1

    return -1

def BMAlgo(text,pattern):
    array = buildArray(pattern)
    n = len(text)
    m = len(pattern)
    i = m - 1

    if (i > n-1 ):
        return -1

    j = m - 1

    if (pattern[j] == text[i]):
        if (j == 0):
            return i
        else :
            i -= 1
            j -= 1
    else :
        x = array[ord(text[i])]
        i = i + m - min(j,1+x)
        j = m - 1
    
    while(i <= n-1):
        if (pattern[j] == text[i]):
            if (j == 0):
                return i
            else :
                i -= 1
                j -= 1
        else :
            x = array[ord(text[i])]
            i = i + m - min(j,1+x)
            j = m - 1

    return -1

def buildArray(pattern):
    array = [-1] * 128
    i = 0
    while( i < len(pattern)):
        array[ord(pattern[i])] = i
        i += 1

    return array

def computeArray(pattern):
    array = [0] * len(pattern)

    x = len(pattern)
    i = 0
    j = 1
    while ( j < x ):
        if(pattern[j] == pattern[i]) :
            array[j] = i+1
            i += 1
            j += 1
        elif(i>0):
            i = array[i-1]
        else :
            array[j] = 0
            j += 1
    
    return array


