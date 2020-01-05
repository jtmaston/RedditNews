import praw
from sqlalchemy import create_engine
from models import create_db
from template import Signup


def redditCrawler():
    reddit = praw.Reddit(
        client_id='Rp_-mEAi447joQ',
        client_secret='_lKBadeG2H9fVUg-LYhkUj81Uhg',
        user_agent='script:NewsGetter:0.0.1 (by /u/Thalos_the_true_god)')

    for index, submission in enumerate(reddit.subreddit('news').top('day', limit=20)):
        print(str(index + 1) + '. ' + submission.title)


sth = None


def main():
    Signup()
    engine = create_engine('sqlite:///news.db')
    engine.connect()
    create_db(engine)
    # while True:
    #     now = datetime.datetime.now()
    #     refTime = now.replace(hour=12, minute=0, second=0, microsecond=0)
    #     if now == refTime:
    #         pass


if __name__ == '__main__':
    main()
