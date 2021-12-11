import os
import random
import sqlite3
from time import time


STATS_FILE = 'stats.db'


calendar_days = [f"{n}日" for n in range(1, 32)]
calendar_days = [
    ('一日', '1'),
    ('二日', '2'),
    ('三日', '3'),
    ('四日', '4'),
    ('五日', '5'),
    ('六日', '6'),
    ('七日', '7'),
    ('八日', '8'),
    ('九日', '9'),
    ('十日', '10'),
    ('十一日', '11'),
    ('十二日', '12'),
    ('十三日', '13'),
    ('十四日', '14'),
    ('十五日', '15'),
    ('十六日', '16'),
    ('十七日', '17'),
    ('十八日', '18'),
    ('十九日', '19'),
    ('二十日', '20'),
    ('二十一日', '21'),
    ('二十二日', '22'),
    ('二十三日', '23'),
    ('二十四日', '24'),
    ('二十五日', '25'),
    ('二十六日', '26'),
    ('にじゅうしちにち', '27'),
    ('二十八日', '28'),
    ('二十九日', '29'),
    ('三十日', '30'),
    ('三十一日', '31'),
]


def setup_stats_db():
    con = sqlite3.connect(STATS_FILE)
    cur = con.cursor()

    cur.execute(
        '''CREATE TABLE IF NOT EXISTS stats
        (question text, answer text, response text, is_correct bool, time real)
        '''
    )
    con.commit()
    return con
    



def say(phrase):
    os.system(f"say {phrase} -v Otoya --quality=127")


def quiz(items, stats_con):
    while True:
        item = random.choice(items)
        quiz_item(item, stats_con)


def quiz_item(item, stats_con):
    question, answer = item
    say(question)

    start_time = time()
    response = input()
    time_taken = time() - start_time

    is_correct = response == answer
    if is_correct:
        print('Correct!')
    else:
        print(f"Incorrect: the answer is {answer}")
    log_stats(stats_con, question, answer, response, is_correct, time_taken)


def log_stats(stats_con, question, answer, response, is_correct, time_taken):
    cur = stats_con.cursor()
    stats_con.execute(f"INSERT INTO stats VALUES ('{question}', '{answer}', '{response}', '{is_correct}', '{time_taken}')")
    stats_con.commit()
	

def main():
    stats_con = setup_stats_db()
    quiz(calendar_days, stats_con)


if __name__ == '__main__':
    main()
