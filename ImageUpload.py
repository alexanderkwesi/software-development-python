from flask import request
import os
import sqlite3
from webbrowser import pycopy



fileitem = request.form['filetoupload']

#check if the file has been uploaded
if fileitem.filetoupload:
    #strip the leading path from the file name
    fn = os.path.basename(fileitem.filetoupload)
    
    #store the file in database
    con = sqlite3.connect("SHELFIE.db")
    cursor = con.cursor()
    fb = "NULL"
    cursor.execute("INSERT INTO UploadItems (Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost) VALUES (?,?,?,?,?)", (4,fn,fb,fb,fb)) 
    con.commit()
webbrowser.open('http://192.168.1.29:5000')