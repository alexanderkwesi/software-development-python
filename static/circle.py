import math
from browser import document, html
from browser.html import TABLE, TR, TH, TD
import browser
import main

price = document['prices'].innerHTML
color = document['color']
canvas = document["zone5"]

browser.alert(price)

ctx = canvas.getContext("2d")

x = 360

def draw(event):
    global x
    ctx.beginPath()
    ctx.arc(x, 25, 15, 0, 2 * math.pi)
    x += 15
    ctx.degrees(price)
    ctx.stroke()
    style = canvas.style
    color = style.color
    style.color = "black"
    style.backgroundColor = color
    style.marginTop: "-30%"
    style.left = "50%"
    
    
    
document.window.bind("mouseover", draw)