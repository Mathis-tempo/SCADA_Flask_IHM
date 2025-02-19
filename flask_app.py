from flask import Flask, render_template, request
from threading import Thread
import driver  
import os
import time

app = Flask(__name__)

def start_flask():
    app.run(debug=True, host='0.0.0.0', use_reloader=False)

def start_driver():
    time.sleep(5)  
    try:
        driver.run()
    except Exception as e:
        print(f"Erreur dans le driver: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/start_entry')
def start_entry():
    driver.start_entry_conveyor()
    return 'Entry Conveyor Started'

@app.route('/stop_entry')
def stop_entry():
    driver.stop_entry_conveyor()
    return 'Entry Conveyor Stopped'

@app.route('/start_exit')
def start_exit():
    driver.start_exit_conveyor()
    return 'Exit Conveyor Started'

@app.route('/stop_exit')
def stop_exit():
    driver.stop_exit_conveyor()
    return 'Exit Conveyor Stopped'

@app.route('/start_sorter1')
def start_sorter1():
    driver.start_sorter1()
    return 'Sorter 1 Started'

@app.route('/stop_sorter1')
def stop_sorter1():
    driver.stop_sorter1()
    return 'Sorter 1 Stopped'

if __name__ == '__main__':
    flask_thread = Thread(target=start_flask)
    flask_thread.daemon = True  
    flask_thread.start()

    driver_thread = Thread(target=start_driver)
    driver_thread.daemon = True
    driver_thread.start()
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Application terminée")