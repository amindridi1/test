# app.py

from flask import Flask, render_template, request, redirect, url_for
from devices import Light, Thermostat
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

# Create smart devices
living_room_light = Light("Living Room Light")
thermostat = Thermostat("Living Room Thermostat")

@app.route('/')
def index():
    return render_template('index.html', light=living_room_light, thermostat=thermostat)

@app.route('/toggle_light', methods=['POST'])
def toggle_light():
    living_room_light.toggle()
    return redirect(url_for('index'))

@app.route('/set_temperature', methods=['POST'])
def set_temperature():
    temp = float(request.form['temperature'])
    thermostat.set_temperature(temp)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
