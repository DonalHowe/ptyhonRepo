import DBcm


config ={
    'host': '127.0.0.1',
    'database': 'wordgame',
    'user': 'wordUser ',
    'password' :'gamesDev'
}

def save_the_data(time_taken,guessedWords, sourceWord):
    SQL = """
        insert into board
        (guessedWords, sourceWord)
        values
        (%s, %s)
    """
    with DBcm.UseDatabase(config) as db:
        db.execute(SQL, (time_taken,guessedWords, sourceWord))


def process_data(name , time_taken,guessedWords, sourceWord):
    with DBcm.UseDatabase(config) as db:
        SQL = """
            select guessedWord, SourceWord
            from board
            order by ssourceWord desc
        """
        db.execute(SQL)
        scores = db.fetchall()
    where = scores.index((name, time_taken,guessedWords, sourceWord)) + 1
    how_many = len(scores)

    return where, how_many, scores[:10]
