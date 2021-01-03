from bs4 import BeautifulSoup
from time import sleep
from selenium import webdriver
from PIL import Image


import sqlite3 as sql
import pytesseract
import requests
import sqlite3 as sql

class DataBase:
    con = ''

    def __init__(self,dataBaseName):

        self.dataBaseName = dataBaseName

    def __new__(self):

        if self.dateBase == 'links':
            self.con = sql.connect('links.db')
            self.cur = con.cursor()

        else:
            self.con = sql.connect('phones.db')
            self.cur = con.cursor()

    def checking_link(self):
        pass

    def checking_for_record(self, link):
        try:

            self.cur.execute(f"INSERT INTO `used_links` VALUES ('{link}')")
                                        #проверяет использовалась ли ссылка, если нет записывает её в базу и возвращает TRUE                 
            con.commit()
        
            return True
        except:
            
            return Fals

    def rocord_phones(self,id, phone):
        pass

    


class AvitoParser:
    pass()




def main():
    pass



if __name__ == "__main__":
    main() 