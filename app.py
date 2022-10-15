from ast import If
from flask import Flask, render_template,request
from gpiozero import LED
from time import sleep

app=Flask(__name__)
blue_led=LED(18)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/emergency_page')
def emergency_page():
    blue_led.on()
    sleep(10)
    return render_template('emergency_page.html')


