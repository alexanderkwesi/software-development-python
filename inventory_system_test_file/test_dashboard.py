import pytest
import sqlite3
from flask import Flask, render_template, request, flash, session, url_for, redirect
from datetime import date
from diskcache import Cache
from flask_caching import Cache
import os
import requests


#TEST DASHBOARD WITH DATASETS#


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




returned_item_list = 4
@pytest.mark.parametrize("returned_item_list", int(4)) 
def sql_data(returned_item_list):
    if returned_item_list == int(4):
        pytest.success("good lucck")
    else:
        pytest.fail("bad lucck")
        
        
no_image = "noimage.jpg"
@pytest.mark.parametrize("no_image", str("noimage.jpeg")) 
def null_images(no_image):
    if no_image == str("noimage.jpeg"):
        pytest.success("good lucck")
    else:
        pytest.fail("bad lucck")
        
        
        
        
@pytest.mark.parametrize()        
@app.route('/loginpage', endpoint = "loginpage1" )
@cache.cached(timeout=50)
def loginpage1():
    return "Loginpage1"  
    
        
        
        
itemcollection = []
@pytest.mark.parametrize("itemcollection", list)
@app.route('/dashboard', endpoint = "dashboard")
@cache.cached(timeout=50)
def dashboard():
    if itemcollection == list:
        pytest.success("good lucck")
    else:
        pytest.fail("bad lucck")

        
        
    
@pytest.mark.parametrize() 
@app.route('/dashboard2', endpoint="dashboard2")
@cache.cached(timeout=50)
def dashboard2():
   return "Dashboard2"  
        
        
        
        

page = "uploaditem.html"
page_found = "uploaditem.html"
@pytest.mark.parametrize("page", page_found) 
@app.route('/dashboard3', endpoint = "dashboard3")
@cache.cached(timeout=50)
def dashboard3(page):
    if page == page_found:
        pytest.success("good lucck")
    else:
        pytest.fail("bad lucck")
        
        
        
        
        
today = today
@pytest.mark.parametrize("today", date.today()) 
@app.route('/dashboard4', endpoint = "dashboard4")
@cache.cached(timeout=50)
def dashboard4(today):
    if today == date.today:
        pytest.success("good lucck")
    else:
        pytest.fail("bad lucck")
        
        
        
        
        
        