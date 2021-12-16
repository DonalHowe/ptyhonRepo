import DBcm


config ={
    'host': '127.0.0.1',
    'database': 'wordgame',
    'user': 'wordUser ',
    'password' :'gamesDev'
}

def save_the_data(name,score,players_browser,players_ip,players_word, word_given,playerTime):
    guessStr=" ".join(players_word)
    SQL = """
        insert into player
        (name,score,players_browser,players_ip,players_words,word_given,player_time)
        values
        (%s,%s,%s,%s,%s,%s,%s)
    """
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL,(name,score,players_browser,players_ip,guessStr, word_given,playerTime))


def process_data():
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select name, players_words, word_given,player_time from player order by player_time desc
        """
        db.execute(SQL)
        scores = []
        scores = db.fetchall()
        non_null=lambda x : "  "
        for row in SQL:
            list=map(non_null,row)
            next=tuple(list)
            scores.append(next)
    ##where = scores.index((name , currentTime,players_word, sourceWord)) + 1
   ## how_many = len(scores)

    return scores[:10]




def save_the_logs(name,score,players_browser,players_ip,players_word, word_given,playerTime):
    guessStr=" ".join(players_word)
    SQL = """
        insert into userlogs
        (name,score,players_browser,players_ip,players_words,word_given,player_time)
        values
        (%s,%s,%s,%s,%s,%s,%s)
    """
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL,(name,score,players_browser,players_ip,guessStr, word_given,playerTime))


def process_logs():
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select * from userlogs order by date_played desc
        """
        db.execute(SQL)
        logs = []
        logs = db.fetchall()
        
    

    return logs
