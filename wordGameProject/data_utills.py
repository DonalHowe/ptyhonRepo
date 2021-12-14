import DBcm


config ={
    'host': '127.0.0.1',
    'database': 'wordgame',
    'user': 'wordUser ',
    'password' :'gamesDev'
}

def save_the_data(name,score,players_browser,players_ip,players_word, word_given,playerTime):
    guessStr="#".join(players_word)
    SQL = """
        insert into player
        (name,score,players_browser,players_ip,players_words, word_given,player_time)
        values
        ( %s,%s, %s,%s, %s,%s, %s)
    """
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL, (name,score,players_browser,players_ip,guessStr, word_given,playerTime))


def process_data(name , timeTaken,guessedWords, sourceWord):
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select guessedWord, SourceWord
            from player
            order by ssourceWord desc
        """
        db.execute(SQL)
        scores = db.fetchall()
    where = scores.index((name, timeTaken,guessedWords, sourceWord)) + 1
    how_many = len(scores)

    return where, how_many, scores[:10]
