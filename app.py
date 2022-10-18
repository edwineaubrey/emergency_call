from flask import Flask, render_template
from gpiozero import LED
from time import sleep

app=Flask(__name__)
blue_led=LED(18)

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html')

@app.route('/emergency_page')
def blue_on():
    for blink in range(10):
        blue_led.on()
        sleep(10)
        blue_led.off()
        return blink
    return render_template('emergency_page.html')

@app.blue_off('/blue_off')
def blue_off():
    blue_led.off()
    return render_template('emergency_page.html')


