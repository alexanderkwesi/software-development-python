import jinja2
from jinja2 import Environment, PackageLoader, select_autoescape, Template
import csv
import pandas as pd
import importlib
import sqlite3
import main_python_file

class allitems():

    def itemlist():
        list_info = []
        #with open("file.csv", newline='') as newfile:
        #files = csv.reader(newfile) 
        #listinfo = list(files)
        main_python_file.con #= sqlite3.connect("SHELFIE.db")
        main_python_file.cursor # con.cursor()
        main_python_file.cursor.execute(""" SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id > 0 ORDER BY Item_Id ASC """)
        list_info =  main_python_file.cursor.fetchall()
        main_python_file.con.commit()
        print(list_info)
        return list_info
        #env = Environment(
        #loader=PackageLoader("items","templates"),
        #autoescape=select_autoescape())
        #templateloader = jinja2.FileSystemLoader(searchpath='./')
        #env = jinja2.Environment(loader=templateloader)
        #templates = env.get_template('items.html')
        #for data in listinfo:
            #result = templates.render( imp0rt = importlib.import_module, data=data)
            #result = templates.render(data=listinfo)
            #return datasuc