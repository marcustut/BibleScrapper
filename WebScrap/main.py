import requests
from bs4 import BeautifulSoup
import re


class webscrap:
    URL = None

    def __init__(self, lang, ver, book, chapter, verse):
        # Default values
        self.lang = lang
        self.ver = ver
        self.book = book
        self.chapter = chapter
        self.verse = verse

    def createHTMLObject(self):
        if self.lang == "EN":
            # sampleURL = https://my.bible.com/en-GB/bible/111/ACT.23.niv
            URL = "https://my.bible.com/en-GB/bible/" + "111/" + \
                self.book + "." + self.chapter + "." + self.ver.lower()
        elif self.lang == "CN":
            # sampleURL = https://my.bible.com/en-GB/bible/41/ACT.24.CNVS
            URL = "https://my.bible.com/en-GB/bible/" + "41/" + \
                self.book + "." + self.chapter + "." + self.ver.upper()

        page = requests.get(URL)

        return page


if __name__ == "__main__":
    # taking input
    print("Welcome to the Bible Scrapper\n")
    lang = input("Select a language(CN/EN): ")

    if lang == "CN":
        ver = input("Select a ver(CNVS/CNUPSS): ")
    else:
        ver = input("Select a ver(NIV/NKJV): ")

    book = input("Select a book: ")
    chapter = input("Select a chapter: ")
    verse = input("Select a verse: ")

    # Creating objects
    webscrap = webscrap(lang, ver, book, chapter, verse)

    htmlObject = webscrap.createHTMLObject()
    parsedHTML = BeautifulSoup(htmlObject.content, 'html.parser')

    # taking every verse
    className_Book = "book bk" + webscrap.book
    className_Chap = "chapter ch" + webscrap.chapter
    className_Verse = "verse v" + webscrap.verse

    class_reader = parsedHTML.find(class_="reader")
    class_book = class_reader.find(class_=className_Book)
    class_chapter = class_book.find(class_=className_Chap)

    list_verse = class_chapter.find_all(class_=re.compile("verse"))

    list_verse_text = [sublist.get_text().strip()
                       for sublist in list_verse if sublist.get_text().strip()]

    print(list_verse_text)
    print(type(list_verse_text))
    print(len(list_verse_text))
