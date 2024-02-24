import os
import sqlite3



fileitem = form['filename']

#check if the file has been uploaded
if fileitem.filename:
    #strip the leading path from the file name
    fn = os.path.basename(fileitem.filename)
    
    #store the file in database
    con = sqlite3.connect("SHELFIE.db")
    cursor = con.cursor()
    cursor.execute("INSERT INTO UploadItems (ItemImage, ItemDetail, ItemBarCode, ItemCost) VALUES ({fn}, NULL, NULL, NULL)") 
    con.commit()