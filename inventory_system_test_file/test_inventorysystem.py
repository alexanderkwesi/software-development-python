import sqlite3
from flask import Flask, render_template, request, flash, session, url_for, redirect
from datetime import date
import requests
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, IntegerField
import random
from diskcache import Cache
from flask_caching import Cache
import os







config = {
    "DEBUG": True,          # some Flask specific configs
    "CACHE_TYPE": "SimpleCache",  # Flask-Caching related configs
    "CACHE_DEFAULT_TIMEOUT": 300
}

app = Flask(__name__, static_folder='static', static_url_path="/Users/alexanderkwesi/Desktop/software development python/static",  template_folder="templates/inventory-system/")
app.secret_key = "Alexander Oluwaseun Kwesi Test Web Application"
session = requests.Session()
session = {"Owner":"PowerUser"}

# tell Flask to use the above defined config
app.config.from_mapping(config)
cache = Cache(app)




conn = sqlite3.connect("SHELFIE.db", check_same_thread=False)
cursor = conn.cursor()

today = date.today()



def createtable():
    cursor.execute("CREATE TABLE IF NOT EXISTS UploadItems (Item_Id INTEGER NOT NULL, ItemImage TEXT, ItemDetail TEXT, ItemBarCode REAL, ItemCost NUMERIC, connSTRAINT Item_Id_PK PRIMARY KEY (Item_Id))") 
    conn.commit()

def sql_data():
    item_list = []
    sql_data_query = """ SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id > 0 ORDER BY Item_Id ASC LIMIT 4"""
    cursor.execute(sql_data_query)
    item_list = cursor.fetchall()
    conn.commit()
    return item_list


def create_table():
    query = "DROP TABLE IF EXISTS login"
    cursor.execute(query)
    conn.commit()
    query = "CREATE TABLE login(Username VARCHAR UNIQUE, Password VARCHAR)"
    cursor.execute(query)
    conn.commit()

def null_images():
    sql = (""" UPDATE UploadItems SET ItemImage = ? WHERE ItemImage = 'NULL' """)
    data_tuple = (str("noimage.jpeg"),)
    cursor.execute(sql, data_tuple) 
    conn.commit()

class page_default():
    
    def __init__(self, previous:int, nexts:int):
        self.previous = previous
        self.nexts = nexts
    def previous_default_page(self):
        
        count, fetch_items = 0, []

        cursor.execute(""" SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id BETWEEN  ? AND ?  ORDER BY Item_Id ASC LIMIT 4 """, (self.previous,self.nexts))
        fetch_items =  cursor.fetchall()
        conn.commit()
        count = count + 1
        if count == 1:
            return fetch_items 
        count = 0    
        exit()
        
class PForm(FlaskForm):
    #username = StringField('first_row', validators=[DataRequired()])
    #password = PasswordField('Password', validators=[DataRequired()])
    first_row = IntegerField('first_row')
    last_row = IntegerField('last_row')
    total_rows = StringField('total_rows')
    #remember_me = BooleanField('Remember Me')
    submit_previous = SubmitField('< previous')
    submit_next = SubmitField('next >')
        
class allitems():

    def itemlist():
        list_info = []
        cursor.execute(""" SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id > 0 ORDER BY Item_Id ASC LIMIT 4""")
        list_info =  cursor.fetchall()
        conn.commit()
        print(list_info)
        return list_info

def selectfirstfourdb():
    query = 'SELECT * FROM UploadItems ORDER BY Item_Id ASC LIMIT 4'
    cursor.execute(query)
    result = cursor.fetchall()
    conn.commit()
    return result
 
@app.route('/dashboard', methods=['GET','POST'])
@cache.cached(timeout=50)
def dashboard():
    if request.method == 'GET':
        null_images()
        all_item_list, itemcollection = [], []
        
        all_item_list = sql_data()
        form = PForm()
        form.total_rows = all_item_list
        form.first_row = 1
        form.last_row = 5
        itemcollection = page_default(form.first_row, form.last_row).previous_default_page()
        return render_template('uploaditem.html', today=today, itemcollection=itemcollection, all_item_list=all_item_list)      


@app.route('/enter')
@app.route('/', methods=['POST', 'GET'])
@cache.cached(timeout=50)
def enter():

    if request.method == 'POST':
        user, pwd = '',''
        user = username = request.form.get('username')
        pwd = password = request.form.get('password')
        result = []
        query = 'WITH RECURSIVE checkuser(x) AS (VALUES|(1) UNION ALL SELECT x+1 FROM login WHERE x<10000000000000) SELECT * FROM login WHERE Username = ? AND Password = ?'
        #query = "SELECT * FROM login WHERE Username = ? AND Password = ?"
        cursor.execute(query, (user, pwd))
        result = cursor.fetchone()
        conn.commit()

           
        if not result:
            queries = "INSERT INTO login (Username, Password) VALUES (?, ?)"
            cursor.execute(queries, (str(username), str(password)))
            conn.commit()
            flash("Username created! Password created Account Created.....", 'success')
            return render_template('loginpage.html', date=today)
        else:
            flash("The user already exit in our db", 'error')
            return render_template('error_page.html', date=today)      
    elif request.method == 'GET':
        session.get("http://127.0.0.1:5000")
        requests.get("http://127.0.0.1:5000")
        if session and requests.status_codes == 200:
                flash('Request was successful.', 'success')
                return render_template('enter.html', today=today)
        elif requests.status_codes == 400:
                flash('The requested resource could not be found.', 'error')
                return render_template('error_page.html', today=today)       
        elif requests.status_codes == 500:
                flash('The requested resource could not be found.', 'error')
        return render_template('error_page_500.html', today=today) 


def checklogin():
    user, pwd = '',''
    result = []
    query = 'WITH RECURSIVE loginpagepage(x) AS (VALUES|(1) UNION ALL SELECT x+1 FROM login WHERE x<10000000000000) SELECT * FROM login WHERE Username = ? AND Password = ?'
    cursor.execute(query, (user, pwd))
    result = cursor.fetchone()
    conn.commit()
    print('[DEBUG][check] result:', result)
    return result



def check(username, password):
    result = []
    query = 'WITH RECURSIVE loginpagepage(x) AS (VALUES|(1) UNION ALL SELECT x+1 FROM login WHERE x<10000000000000) SELECT * FROM login WHERE Username = ? AND Password = ?'
    cursor.execute(query, (username, password))
    result = cursor.fetchone()
    conn.commit()
    print('[DEBUG][check] result:', result)
    return result


@app.route('/loginpage', methods=['POST','GET'])
@cache.cached(timeout=50)
def loginpage():
    #response = requests.post(url, data=data)#
   
    
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('passowrd')
        answer = request.form['btnsubmit']
        result = []
        query = 'WITH RECURSIVE login(x) AS (VALUES|(1) UNION ALL SELECT x+1 FROM login WHERE x<10000000000000) SELECT * FROM login WHERE Username = ? AND Password = ?'
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        conn.commit()
        
        if answer and result:
                flash('Request was successful. You succcessfully logged in', 'success')
                return render_template('uploaditem.html', today=today )
                #return redirect(url_for('dashboard'))
                #return render_template('uploaditem.html', today=today, height=height, color=color, price=price)
        elif not result:
            
            flash("The requested resource could not be found.", 'error')
        return render_template('error_page.html', today=today)
    elif request.method == 'GET':
        session.get("http://127.0.0.1:5000/loginpage")
        requests.get("http://127.0.0.1:5000/loginpage")
        if session and requests.status_codes == 200:
                flash('Request was successful.', 'success')
                return render_template('loginpage.html', today=today)
        elif requests.status_codes == 400:
                flash('The requested resource could not be found.', 'error')
                return render_template('error_page.html', today=today)
        elif requests.status_codes == 500:
                flash('The requested resource could not be found.', 'error')
        return render_template('error_page_500.html', today=today)     
    
    
    
@app.route('/edit', methods=['POST'])
@cache.cached(timeout=50)
def edit():
    item_id, image, detail, cost, itemcollection = 0, '', '', 0, []
    
    all_item_list = sql_data()
    
    if request.method == 'POST' and request.form['editbtn']:
        
        item_id = request.form.get('item_id')
        image = request.form.get('imagetxt')
        detail = request.form.get('detailtxt')
        cost = request.form.get('costtxt')
        
        
        if image.__contains__(".jpeg") or image.__contains__(".jpg") or image.__contains__(".png"):
            sql = (""" UPDATE UploadItems SET ItemImage = ?, ItemDetail = ?, ItemCost = ?  WHERE Item_Id = ?  and ItemImage = 'noimage.jpeg' """)
            data_tuple = (str(image),str(detail),int(cost), str(item_id),)
            cursor.execute(sql, data_tuple) 
            conn.commit()
            sql_query = """ SELECT * FROM UploadItems LIMIT 4"""
            cursor.execute(sql_query)
            itemcollection=cursor.fetchall()
            conn.commit()
            
            flash('Success_Message: Details Edited Successfully', 'success')
            return render_template("uploaditem.html", today=today, itemcollection=itemcollection, all_item_list=all_item_list)
        else:
            flash('Error_Message: Details Edited UnSuccessfully', 'error')
            return render_template("uploaditem.html", today=today, itemcollection=itemcollection, all_item_list=all_item_list)
        

@app.route('/nnext', methods=['POST'])  
@cache.cached(timeout=50)
def nnext():
    
    all_item_list, itemcollection, form_first_id, form_last_id, row_id = [], [],  0, 0, 0

    btnsubmit_pre, btnsubmit_nex = '', ''
    
    all_item_list = sql_data()

    
    if request.method == 'POST':
        
        if request.form['btnsubmit_next']:
        
            btnsubmit_nex = request.form['btnsubmit_next']
            btnsubmit_pre = request.form['btnsubmit_previous']
            print|(btnsubmit_nex, btnsubmit_pre)
            form_first_id = request.form.get('txt_id')
            form_last_id = request.form.get('txt_2_id')

            row_id = int(form_last_id)
            print(row_id)
        
            if int(row_id) < int(len(all_item_list)):
                form_first_id = row_id
                form_last_id = row_id + 5
                cursor.execute(""" SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id BETWEEN  ? AND ?  ORDER BY Item_Id ASC LIMIT 4 """, (form_first_id, form_last_id))
                
                itemcollection =  cursor.fetchall()
                conn.commit()
                    
            return render_template("uploaditem.html", today=today, itemcollection=itemcollection, all_item_list=all_item_list) 

    
    if request.method == 'POST' and request.form['btnsubmit_previous']:
    
            
        if int(row_id) < int(len(all_item_list)):
            form_first_id = int(form_first_id) - 5
            form_last_id = form_last_id - 5
            cursor.execute(""" SELECT Item_Id, ItemImage, ItemDetail, ItemBarCode, ItemCost FROM UploadItems WHERE Item_Id BETWEEN  ? AND ?  ORDER BY Item_Id ASC LIMIT 4 """, (form_first_id, form_last_id))
            itemcollection =  cursor.fetchall()
            conn.commit()
        return render_template('uploaditem.html', today=today, itemcollection=itemcollection, all_item_list=all_item_list) 
    
 

        
@app.route('/uploaditem', methods=['GET','POST'])
@cache.cached(timeout=50)
def uploaditem():
    
    all_item_list = sql_data()
    fileitem = ''
    fileitem = str(request.files['filetoupload']).lstrip("<FileStorage:").rstrip("\'('image/jpeg')>'").rstrip("('image/jpg')>'").rstrip("('image/png')>'").rstrip("('image/svg+xml')>")
    #fileitem = str(request.files['filetoupload'])
    
    
    if request.method == 'POST':
        
        if fileitem.__contains__('.jpeg') or fileitem.__contains__('.jpg') or fileitem.__contains__('.png'):

            #insert image if not exist
            testentry = str(fileitem).lstrip("<FileStorage:").rstrip("\'('image/jpeg')>").replace("('image/jpg')>", "").rstrip("('image/png')>").rstrip("('image/svg+xml')>").lstrip('"').rstrip('"').lstrip(' ').rstrip(' ').lstrip("'").rstrip("'")
            #testentry = str(fileitem)
            #.replace("['", "").replace("']", "").replace('"', "").replace("[","").replace("]","")
            #new_s_list.append(str("'('") +testentry+ str(",')'"))
            #print(str(new_s_list[0]))
            print(testentry)
            sqll = """ SELECT ItemImage FROM UploadItems WHERE ItemImage LIKE ? LIMIT 4"""
        
            cursor.execute(sqll, ('%'+testentry+'%',))
            #cursor.execute(sqll)
            databaseretrieval = cursor.fetchone()
            conn.commit()
            print(databaseretrieval)


            if not databaseretrieval:
                
                sql = ("""INSERT INTO UploadItems (ItemImage, ItemDetail, ItemBarCode, ItemCost) VALUES (?,?,?,?)""")
                data_tuple = (str(testentry), str('NULL'), str('NULL'), str('NULL'),)
                itemcollection = cursor.execute(sql,data_tuple) 
                conn.commit()
                path = "/Users/alexanderkwesi/Desktop/software development python/static/images/" + testentry
                isExisting = os.path.exists(path)
                if not isExisting:
                    sql = (""" UPDATE UploadItems SET ItemImage = ? WHERE ItemImage = ? """)
                    data_tuple = (str("noimage.jpeg"),str(testentry))
                    cursor.execute(sql, data_tuple) 
                    conn.commit()

                    flash('Success_Message: Image Uploaded Successfully', 'success')
                    return redirect(url_for('dashboard'))
                #return render_template('uploaditem.html', today=today, itemcollection=itemcollection, all_item_list=all_item_list) 
                
                
                        
            if databaseretrieval:
                # if image already exist
                sqll = """SELECT * FROM UploadItems LIMIT 4"""
                cursor.execute(sqll)
                itemcollection  = cursor.fetchall()
                conn.commit()
                flash('Success_Message: Image Already Uploaded Successfully Chose a different Image"', 'success')
                return render_template('uploaditem.html', today=today, itemcollection=itemcollection, all_item_list=all_item_list)
        else:
        
                sqll = """SELECT * FROM UploadItems LIMIT 4"""
                cursor.execute(sqll)
                itemcollection = cursor.fetchall()
                conn.commit()
                flash('Error_Message: Image format not found', 'error')
                return render_template('uploaditem.html', today=today, itemcollection=itemcollection, all_item_list=all_item_list)  
            
    elif request.method == "GET":
        flash('Success_Message: Image Uploaded Successfully', 'success')
        return redirect(url_for('dashboard'))
    
    elif requests.status_codes == 500:
            flash('The requested resource could not be found.', 'error')
            return render_template('error_page_500.html', today=today) 
    elif requests.status_codes == 400:
            flash('The requested resource could not be found.', 'error')
            return render_template('error_page.html', today=today) 
        
        
@app.route('/insertitemdetail', methods=['GET','POST'])
@cache.cached(timeout=50)
def insertitemdetail():
    all_item_list = sql_data()
    itemcollection, item_id = [], ''
    #driver = webdriver.Chrome()
    #driver.get('http://localhost:5000/')
    if request.method == 'POST':
        my_form_itemdetails = ""
        my_form_itemcost = ""
        itemid = request.form.get('selected_item_id')
        my_form_itemimage = request.form.get('itemimage')
        my_form_itemdetails = request.form.get('itemdetail')
        my_form_itemcost = request.form.get('itemcost')
        if my_form_itemimage or my_form_itemdetails or my_form_itemcost:
            my_data_one = my_form_itemdetails
            my_data_two = my_form_itemcost
            print(my_data_one, my_data_two)
            item_id = itemid
            print(item_id)
            sql = (""" UPDATE UploadItems SET ItemImage  = ? , ItemDetail = ? , ItemBarCode = ? ,  ItemCost = ? WHERE Item_Id = ? """)
            data_tuple = (str(my_form_itemimage), str(my_form_itemdetails), str('NULL'), str(my_form_itemcost), int(item_id))
            cursor.execute(sql, data_tuple) 
            conn.commit()
            itemcollection = allitems.itemlist()
            flash('Success_Message: Details Inserted Successfully', 'success')
        return render_template("uploaditem.html", today=today, itemcollection=itemcollection, item_id=item_id, all_item_list=all_item_list)
    if not request.method == 'POST':
            itemcollection = allitems.itemlist()
            flash('Error_Message: Details Not Inserted Successfully', 'error')
    return render_template("uploaditem.html", today=today, itemcollection=itemcollection, all_item_list=all_item_list)        



@app.route("/deleteitem", methods=['POST'])
@cache.cached(timeout=50)
def deleteitem():
    all_item_list = sql_data()
    item_id, itemcollection = 0, []
    
    if request.method == 'POST' :
        item_id = request.form.get('item_number')
        second_item_id = request.form.get('item_number_two')
        print(item_id, second_item_id)
        if not item_id == "" and not second_item_id == "":
            
            sql = """ DELETE FROM UploadItems WHERE Item_Id BETWEEN ? AND ? """
            cursor.execute(sql, (int(item_id), int(second_item_id),))
            cursor.fetchall()
            conn.commit()
            sqll = """SELECT * FROM UploadItems LIMIT 4"""
            cursor.execute(sqll)
            itemcollection = cursor.fetchall()
            conn.commit()
            flash('Success_Message: Data Record Deleted Successfully', 'success')
        elif not item_id == "" :
            
            sql = """ DELETE FROM UploadItems WHERE Item_Id = ? """
            cursor.execute(sql, (int(item_id),))
            cursor.fetchall()
            conn.commit()
            sqll = """SELECT * FROM UploadItems LIMIT 4"""
            cursor.execute(sqll)
            itemcollection = cursor.fetchall()
            conn.commit()
            flash('Success_Message: Data Record Deleted Successfully', 'success')
    return render_template("uploaditem.html", today=today,  itemcollection=itemcollection, all_item_list=all_item_list)


@app.route('/ascending')
@cache.cached(timeout=50)
def ascending():
    all_item_list = sql_data()
    sqll = """SELECT * FROM UploadItems ORDER BY Item_Id ASC LIMIT 4 """
    cursor.execute(sqll)
    itemcollection  = cursor.fetchall()
    conn.commit()
    
    return render_template('uploaditem.html', today=today, itemcollection=itemcollection, all_item_list=all_item_list)


@app.route('/descending')
@cache.cached(timeout=50)
def descending():
    all_item_list = sql_data()
    sqll = """SELECT * FROM UploadItems ORDER BY Item_Id DESC LIMIT 4"""
    cursor.execute(sqll)
    itemcollection  = cursor.fetchall()
    conn.commit()
    
    return render_template('uploaditem.html', today=today, itemcollection=itemcollection, all_item_list=all_item_list)

@app.route('/searchdb', methods=['POST'])
@cache.cached(timeout=50)
def searchdb():
    all_item_list = sql_data()
    if request.method == 'POST':
        item = request.form.get("searchItem")
        sqll = """SELECT * FROM UploadItems WHERE Item_Id LIKE ? OR ItemDetail LIKE ? OR ItemImage LIKE ? OR ItemCost LIKE ? ORDER BY Item_Id DESC LIMIT 4"""
        cursor.execute(sqll, ("%"+item+"%","%"+item+"%","%"+item+"%","%"+item+"%",) )
        itemcollection  = cursor.fetchall()
        conn.commit()
    return render_template('uploaditem.html', today=today, itemcollection=itemcollection, all_item_list=all_item_list)


@app.route('/analytics_dashboard')
@cache.cached(timeout=50)
def analytics_dashboard():
    import os
    if request.method == 'GET':

        #db_name = os.path.dirname(os.path.abspath("sqlite3.py"))
        #filename = os.path.abspath(__file__)
        #dbdir = filename.rstrip('main.py')
        path = "/Users/alexanderkwesi/Desktop/Built-Up-Areas/software development python/"
        dbpath = os.path.join(path, "SHELFIE.db")
        paths = os.chdir(r"/Users/alexanderkwesi/Desktop/Built-Up-Areas/software development python/")
        sqliteConnection = sqlite3.connect(dbpath)
        cursor = sqliteConnection.cursor() 
        print(paths)

        prices = []
        color_list = [["red", "blue", "green", "yellow"], ["brown", "orange", "azure", "black"],  ["grey", "snow", "almond", "cyan"]]
        color = random.choice(color_list)
        color = color
        
        colors = str(color).strip('[]').strip('"').strip(',').replace(',', '').replace(' ', '')
        colors = "".join(colors).splitlines(keepends="False")
        
        for col in colors:
           colors=  print(col, sep="\n")
           print(colors)

        sql = """SELECT COUNT(*), ItemImage FROM UploadItems WHERE Item_Id > 0 GROUP BY ItemImage ORDER BY Item_Id ASC LIMIT 4"""
        cursor.execute(sql)
        height  = cursor.fetchall()
        conn.commit()

        print(height)

        sql_query = """SELECT COUNT(*), ItemCost FROM UploadItems WHERE Item_Id > 0 GROUP BY ItemCost ORDER BY Item_Id ASC LIMIT 4 """
        cursor.execute(sql_query)
        price  = cursor.fetchall()
        conn.commit()
        for eachprice in price:
            print(eachprice)
            if len(eachprice) == len(price):
                prices.append(str(eachprice).strip('()"'))
                print(prices)
             
       
        return render_template('analytics_dashboard.html', today=today, height=height, price=price, color=col)

        

def page_not_found():
    return render_template('error_page.html'), 404


def create_app():
    app = Flask(__name__)
    app.register_error_handler(404,  page_not_found)
    return app

@app.route('/error_page')
@cache.cached(timeout=50)
def error_page():
    return render_template("error_page.html", today=today)

@app.route('/error_page_500')
@cache.cached(timeout=50)
def error_page_500():
    return render_template("error_page_500.html", today=today), 500

# --- main ---#
if __name__ == '__main__':

    create_table()
    null_images()
    cursor.close()
    conn.close()