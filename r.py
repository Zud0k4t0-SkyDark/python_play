#!/usr/bin/python
import requests,sys ,signal, random, subprocess, time, os
from bs4 import BeautifulSoup
from rich import print

def def_handler(sig, frame):
    print ("\n\n[red][!][/red] Saliendo...\n\n")
    sys.exit(1)

# CTRL + C

signal.signal(signal.SIGINT, def_handler)

# Petición a la pagina Web
r = requests.get("https://www.palabrasaleatorias.com/?fs=4&fs2=0&Submit=Nueva+palabra")
words = r.text
def get_words():
    soup = BeautifulSoup(words, 'html.parser')
    word_list = []
    for word in soup.td.find_all('div'):
        word_list.append(word.get_text(strip=True))
    word_list.pop()
    return word_list

def banner(x,y):
    # Mostrando la palabra a Adivinar
    print ("[red][*][/red] Palabra a adivinar...\n\n\t[blue]==> [/blue]%s\n" % x)
    # Palabra Secreta
    #print (y) 
def words_s(x, w, y_w):
    word=""
    for letter in w:
        if letter.lower() in y_w.lower():
            word+=letter+" "
        else:
            word +="_ "
            x+=1
    return word, x

def game(x):
    lifes = 6
    your_word = ""
    word = random.choice(x)
    letters_bad = ""
    while lifes > 0:
        errors = 0
        word_storage, errors = words_s(errors, word, your_word)
        banner(word_storage, word)
        if errors == 0:
            print("[yellow][*][/yellow] Ganaste...")
            break
        print ("[yellow][*][/yellow] Introduce una letra:\n==> ", end="")
        os.system("tput cnorm")
        letter = input("")
        letter = letter.strip()
        if letter not in word:
            letters_bad += letter+" " 
            lifes-=1
            print ("\n\n[[red]*[/red]] Fallaste !!")
            print ("Te quedan {} vidas\n".format(lifes))
            print ("Letras ya introducidas\n", end="")
            print (*letters_bad, sep="-")
            os.system("tput civis")
            time.sleep(3)
            s = subprocess.run("clear")
        if len(letter) > 1:
            letter = ""
            s = subprocess.run("clear")
            print ("No escribas demasiadas letras")
            print ("Suspendido por 5s")
            time.sleep(5)
            s = subprocess.run("clear")
        your_word+=letter
        if lifes == 0:
            print("\n\n[[red]![/red]] [cyan]Perdiste...[/cyan]\n")
    else:
        print ("[[green]*[/green]] Bien jugado !!\n")
if __name__=='__main__':
    words = get_words()
    game(words)
