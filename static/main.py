from browser import document, html, browser
import browser

browser.alert("dfasdasda Hi!")



color = document['color'].text
val1  = document["zone1"]
val2  = document["zone2"]
val3  = document["zone3"]
val4  = document["zone4"]

def change(event):
    
    S = "400px"
    style = val1.style
    color = style.color
    style.color = "black" 
    style.backgroundColor = color 
    style.fontWeight = "bold" 
    style.fontSize = "10px" 
    style.width = S
    style.height = "70px"
    
    
    C = "300px"
    style = val2.style
    color = style.color
    style.color = "black"
    style.backgroundColor = color 
    style.fontWeight = "bold" 
    style.fontSize = "10px" 
    style.width = C
    style.height = "70px"
    
    A = "700px"
    style = val3.style
    color = style.color
    style.color = "black" 
    style.backgroundColor = color 
    style.fontWeight = "bold" 
    style.fontSize = "10px" 
    style.width = A
    style.height = "70px"
    
    B = "100px"
    style = val4.style
    color = style.color
    style.color = "black" 
    style.backgroundColor = color
    style.fontWeight = "bold" 
    style.fontSize = "10px" 
    style.width = B
    style.height = "70px"
    
    document["dashboard"].bind("mouseover", change)




