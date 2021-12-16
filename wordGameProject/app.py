from os import name
from flask import Flask, render_template, request, session

from data_utills import process_logs, save_the_data, process_data, save_the_logs

import random
from collections import Counter
import datetime

app = Flask(__name__)
app.secret_key = "happiness"

words = "words.txt"
smallWords = "smallWords.txt"
bigWords = "bigWords.txt"


with open(words) as wf:
    wordData = wf.read()
with open(smallWords) as sf:
    smallWordData = sf.read()
with open(bigWords) as bf:
    bigWordData = bf.read()
wordData = wordData.lower()

wordData = wordData.split("\n")
smallWordData = []
bigWordData = []
with open("smallWords.txt", "w") as sf:
    with open("bigwords.txt", "w") as bf:
        for row in wordData:
            if row.endswith("s"):
                continue
            else:
                if len(row) > 7:
                    bigWordData.append(row)

                elif len(row) > 3:
                    smallWordData.append(row)


RangeWords = len(bigWordData)
smallRangeWords = len(smallWordData)

sourceWord=""
guessedWords = ""
if_correct=""
userName=""
didPlayerWin=False


@app.get("/")
@app.get("/home")
def home_Page():
    
    return render_template("home.html", title=" welcome to the home")




@app.route("/game")
def game():
    
    session["userName"]=request.args.get("playerName")
    startTime=datetime.datetime.now()
    session["start_time"]=startTime
    sourceWord = bigWordData[random.randint(0, RangeWords)]
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


@app.route("/results")
def results():
    
    ##doing the time
    endTime=datetime.datetime.now()
    session["end_time"]=endTime
    sessionStarttime=session["start_time"]
    sessionEndTime= session["end_time"]
   
    myGuess = request.args.get("seven_words").split()
    session["myGuess"] = myGuess
    print("This is my word", myGuess)
    currentTime=sessionEndTime.timestamp()-sessionStarttime.timestamp()
    currentTime=round(currentTime,2)
    
   
    
 
    
    if len(sourceWord) > 3:
        print(sourceWord)
    elif len(sourceWord) < 3:
        print("error word is invalid")
        didPlayerWin=False
 
    guessedWords = session["myGuess"]
    
    
    
    for row in guessedWords:
        
        if len(row) < 4:
             wordToSmall()
        else:
            print("word is long enough")
            didPlayerWin=False
        
    letterCount =0;   
    gwc = Counter(guessedWords[0])
    swc = Counter(sourceWord)
    for letter in gwc:
        if gwc[letter.lower()] <= swc[letter.lower()]:
           print("word okay")
           
        else:
          wrongLetter()
          letterCount=1
    
    
        
        
        
    if row in guessedWords:
        if smallWordData.count(row) == 0:
            print("word is invalid")
            letterCount=1
        else:
            print("word is valid")

    if len(guessedWords) > 7:
        print("please enter 7 words ")
    elif len(guessedWords) < 7:
        lackOfwords()
    else:
        print("prefect amount of words")
        
   
         
    name="player name here :"
    score = 2
    ##date_played =120
    players_browser = request.user_agent.string
    players_ip = request.environ.get('HTTP_X_REAL_IP',request.remote_addr)
    players_word = guessedWords
    word_given = sourceWord
    playerTime = currentTime
    myGuess = (" ".join(myGuess))
    
    if(letterCount==1):
            
       if_correct="one or more of the words is wrong :("
    
    else:
         if_correct="Congrats you have won"
         didPlayerWin=True

    save_the_logs(name, score, players_browser, players_ip, players_word, word_given, playerTime)
    if didPlayerWin==True:
        
        save_the_data(name, score, players_browser, players_ip, players_word, word_given, playerTime)
    
    ##where, how_many, ordered= process_data(name , currentTime,guessedWords, sourceWord)
    # gets the session value for the current browser.
    return render_template(
        "results.html",
        guessed_words=myGuess,
        userName=session.get("userName"),
        title="results",
        
        ifCorrect=if_correct,
        time=currentTime
    )



def lackOfwords():
    print("please input 7 words thanks :)")
    Counter=1
    return 

def wrongLetter():
      print("wrong letter")
      letterCount=1
      return
  
def wordToSmall():
    print("the word is to small")
    letterCount=1
    return

    
@app.get("/top10")
def displayTable():
    
    database = []
    database = process_data()
    print(database)
    
    return render_template(
        "topTen.html",
        data_base=database
        
    )

@app.get("/logs")
def userLog():
    database = []
    database = process_logs()
    print(database)
    return render_template(
        "logs.html",
        data_base=database
    )
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
