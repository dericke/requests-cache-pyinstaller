#!/usr/bin/env python3

import sys
from datetime import timedelta
from pathlib import Path
from pprint import pprint

import appdirs
import requests_cache
from PySide6.QtWidgets import (
    QApplication,
    QMainWindow,
)

from . import mainwindow

URL = "https://jsonplaceholder.typicode.com/posts/1/comments"
CACHE_LOCATION = Path(appdirs.user_cache_dir("requests cache pyinstaller"))


class MainApp(QMainWindow, mainwindow.Ui_MainWindow):
    def __init__(self, parent=None):
        """
        Loads history file path, establish event handling with signal/slot
        connection.
        """
        super().__init__()
        self.setupUi(self)

        self.setup_cache()

        self.getButton.clicked.connect(self.get_request)

    def setup_cache(self) -> None:
        CACHE_LOCATION.mkdir(exist_ok=True, parents=True)
        expiry = timedelta(hours=12)
        requests_cache.remove_expired_responses(expiry)
        self.session = requests_cache.CachedSession(
            backend=requests_cache.backends.sqlite.SQLiteCache(
                db_path=CACHE_LOCATION / "cache.sqlite",
                use_cache_dir=True,
            )
        )
        print("Request caching enabled")

    def get_request(self) -> None:
        r = self.session.get(URL)

        comments = r.json()

        for comment in comments:
            pprint(comment)


def main():
    app = QApplication(sys.argv)
    form = MainApp()
    form.show()
    app.exec()


if __name__ == "__main__":
    main()
