from os import name
from flask import Flask, render_template, request, session

from data_utills import save_the_data, process_data

import random
from collections import Counter 
from datetime import datetime, timedelta

app = Flask(__name__)


words="words.txt"
smallWords="smallWords.txt"
bigWords="bigWords.txt"


with open(words) as wf:
        wordData=wf.read()
with open(smallWords) as sf:
        smallWordData=sf.read()
with open(bigWords) as bf:
         bigWordData=bf.read()
wordData=wordData.lower()

wordData=wordData.split("\n")
smallWordData= []
bigWordData= []
with open("smallWords.txt","w") as sf:
    with open("bigwords.txt","w") as bf:
        for row in wordData:
            if(row.endswith("s")):
                continue
            else:
                if len(row)>7:
                    bigWordData.append(row)
                    print(row,file=bf)
                elif len(row)>3:
                    smallWordData.append(row)
                    print(row,file=sf)

RangeWords=len(bigWordData)
smallRangeWords=len(smallWordData)
sourceWord=bigWordData[random.randint(0,RangeWords)]

guessedWords=""


@app.get("/")
@app.get("/home")
def home_Page():
    return render_template(
        "home.html",title=" welcome to the home"
    )
    

    
@app.post("/processGame")
def processGame():
    
    timeTaken = datetime.now()
   ## ini_time_for_finished = datetime.now()

    ##ini_time_for_total = ini_time_for_finished - ini_time_start

    ##totaltimeSeconds = ini_time_for_total.total_seconds()
    ##print(totaltimeSeconds)
    
    if len(sourceWord)>3:
        print(sourceWord)
    elif len(sourceWord)<3:
            print("error word is invalid")
   
    
    for row in guessedWords:
        if len(row)<4:
           print("word is invalid" )
           print(row)
    gwc=Counter(guessedWords[0])
    swc=Counter(sourceWord)
    for letter in gwc:
        if gwc[letter] <= swc[letter]:
            print("player word is valid")
        else:
            print("player word is not valid")
        ## mark current word as invalid 
    ## checks to see if the word is in the list of words
    
    
    if row in guessedWords:
        if smallWordData.count(row)==0:
                print("word is invalid")
        else:
                print("word is valid")
                
    if len(guessedWords) >7:
        print("please enter 7 words ")
    elif len(guessedWords) <7:
            print("please enter 7 words")
    else:
         print("prefect amount of words")
    name = "john"
    score= 2
    ##date_played =120
    players_browser=8347
    players_ip=127
    players_word=guessedWords
    word_given=sourceWord   
    playerTime=10.04 



    save_the_data(name,score,players_browser,players_ip,players_word, word_given,playerTime)
   ## process_data(name , ini_time_start,guessedWords, sourceWord)
    ##where, how_many, ordered= process_data(name , ini_time_start,guessedWords, sourceWord)
    # gets the session value for the current browser.
    
    
  
    return render_template(
        "results.html",
        guessed_words=guessedWords,
        name="john",
        title="results"
      
    )
@app.get("/game")
def game():
    
    return render_template(
        "game.html",
        title="lets  play",
        name=name,
       ## time=timeTaken,
        source_word=sourceWord
        ##position=where,
       ## length=how_many,
       ## topten=ordered[:10],
    )
    

    
@app.route('/processGame', methods=['POST'])
def my_form_post():
    guessedWords = request.form['seven_words']
    return 
    
    
    
@app.post("/results")
def results():
    
     return render_template(
        "results.html",
        guessed_words=guessedWords,
        name="john",
        title="results"
      
    )





app.secret_key = "fhfho;dsi8 iergo;ireaj 90eru goerij 0re9uirae90eua gerg9eraugaer 9re"


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
