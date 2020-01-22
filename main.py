import webbrowser
from datetime import datetime

from PyQt5 import QtWidgets, QtGui
import praw
from PyQt5.QtWidgets import QTableWidgetItem, QHeaderView, QPushButton
from sqlite3 import connect
from News import Ui_MainWindow  # importing our generated file

import sys

db = connect('news.db')


class deleted:
    name = 'Deleted'


class myWindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(myWindow, self).__init__()
        self.links = []
        self.lastRendered = ()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.ui.NewsTable.setColumnCount()
        self.ui.comboBox.currentTextChanged.connect(self.on_combobox_changed)
        self.refresh('day')

    def on_combobox_changed(self, value):
        check = {'Today': 'day', 'This week': 'week', 'This month': 'month', 'This year': 'year', 'All time': 'all'}
        self.refresh(check[value])

    def linkOut(self, item):
        if (item.column(), item.row()) != self.lastRendered:
            if item.column() == 1:
                webbrowser.open(self.links[item.row()])
                self.lastRendered = (item.column(), item.row())

    def refresh(self, sort_by):
        c = db.cursor()
        c.execute('delete from articles;')
        c.execute("UPDATE SQLITE_SEQUENCE SET SEQ=0 WHERE NAME='articles';")
        db.commit()
        reddit = praw.Reddit(
            client_id='Rp_-mEAi447joQ',
            client_secret='_lKBadeG2H9fVUg-LYhkUj81Uhg',
            user_agent='script:NewsGetter:0.0.1 (by /u/Thalos_the_true_god)')

        for entry in reddit.subreddit('news').top(sort_by, limit=10):
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
            self.renderTable()
        db.commit()

    def renderTable(self):
        self.ui.NewsTable.setColumnCount(3)
        self.ui.NewsTable.setRowCount(10)
        self.ui.NewsTable.setHorizontalHeaderLabels(('Title', 'Url', 'Posted at'))
        header = self.ui.NewsTable.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)
        self.ui.NewsTable.verticalHeader().setVisible(False)
        c = db.cursor()
        c.execute('select * from articles')
        data = c.fetchall()
        self.ui.NewsTable.itemDoubleClicked.connect(self.linkOut)
        for index, i in enumerate(data):
            pubTimestamp = datetime.utcfromtimestamp(int(i[3])).strftime('%Y-%m-%d %H:%M:%S')
            self.ui.NewsTable.setItem(index, 0, QTableWidgetItem(i[1].strip('\n').strip()))
            self.links.append(i[5])
            self.ui.NewsTable.setItem(index, 1, QTableWidgetItem("Link"))
            self.ui.NewsTable.setItem(index, 2, QTableWidgetItem(pubTimestamp))


app = QtWidgets.QApplication([])

application = myWindow()
app.setWindowIcon(QtGui.QIcon("Reddit.ico"))
application.show()

app.exec()
