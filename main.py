from sqlite3 import connect
from tkinter import StringVar, Label, Tk, ttk
from tkinter.ttk import Combobox
import praw


class deleted:
    name = 'Deleted'


db = connect('news.db')


def refresh(sort_by):
    c = db.cursor()
    c.execute('delete from articles;')
    c.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='articles';")
    db.commit()
    reddit = praw.Reddit(
        client_id='Rp_-mEAi447joQ',
        client_secret='_lKBadeG2H9fVUg-LYhkUj81Uhg',
        user_agent='script:NewsGetter:0.0.1 (by /u/Thalos_the_true_god)')

    for entry in reddit.subreddit('news').top(sort_by, limit=200):
        print(entry.title)
        if entry.author is None:
            author = deleted()
        else:
            author = entry.author
        c.execute(
            f"""INSERT INTO articles (title, author, posted, score, url) 
            VALUES ("
            {entry.title.replace('"', "'")}",
            "{author}",
            {entry.created_utc},
            {entry.score},
            "{entry.url}");""")
    db.commit()


def GUI():
    def choice_updated(index, value, op):
        check = {'Today': 'day', 'This week': 'week', 'This month': 'month', 'This year': 'year', 'All time': 'all'}
        refresh(check[timePicker.get()])

    window = Tk()
    # window.resizable(False, False)
    window.title("Login prompt")
    # window.geometry('700x150')
    title = Label(window, text='Breaking news!', font=("Arial", 50))
    title.grid(row='0', column='0')
    v = StringVar()
    v.trace('w', choice_updated)
    timePicker = Combobox(window, textvar=v, values=('Today', 'This week', 'This month', 'This year', 'All time'))
    timePicker.current(0)
    timePicker.grid(column=0, row=1)
    newsTable = ttk.Treeview(window, columns=[0, 1, 2, 3])
    # newsTable["columns"] = ["Member ID", "Full Name"]
    # newsTable["show"] = "headings"
    # newsTable.heading("Member ID", text="Member ID")
    # newsTable.heading("Full Name", text="Full Name")
    widths = [5, 500, 500, 100]
    newsTable.delete(*newsTable.get_children())
    for index, name in enumerate(['/', 'Title', 'Link', 'Published date']):
        newsTable.column(index, width=widths[index], stretch=0)
        newsTable.heading(index, text=f"{name}")

    c = db.cursor()
    newsReel = c.execute('select * from articles')
    data = c.fetchall()
    for i in data:
        newsTable.insert("", "end", values=(i[0], i[1].strip(), i[5], i[2], i[4], i[3]))

    newsTable.grid(row=2, sticky='NSEW')
    window.mainloop()


def main():
    c = db.cursor()
    c.execute(" SELECT count(name) FROM sqlite_master WHERE type='table' AND name='articles'")
    if c.fetchone()[0] == 0:
        c.execute("CREATE TABLE articles (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, author VARCHAR(100), "
                  "posted timestamp, score INTEGER, url VARCHAR(100))")
        db.commit()
    GUI()


if __name__ == '__main__':
    main()
