from flask import Flask, render_template, jsonify
from threading import Thread
import driver
import time
from state import system_state

app = Flask(__name__)

def start_flask():
    app.run(debug=True, host='0.0.0.0', use_reloader=False)

def start_driver():
    time.sleep(5)
    try:
        driver.run()
    except Exception as e:
        print(f"Error while launching driver: {e}")

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_state')
def get_state():
    return jsonify({
        'entry_state': system_state.entry_conveyor_state,
        'exit_state': system_state.exit_conveyor_state,
        'sorter1_state': system_state.sorter1_state,
        'sorter2_state': system_state.sorter2_state,
        'sorter3_state': system_state.sorter3_state,
        'entry_controlled_by_flask': system_state.entry_controlled_by_flask,
        'exit_controlled_by_flask': system_state.exit_controlled_by_flask,
        'sorter1_controlled_by_flask': system_state.sorter1_controlled_by_flask,
        'sorter2_controlled_by_flask': system_state.sorter2_controlled_by_flask,
        'sorter3_controlled_by_flask': system_state.sorter3_controlled_by_flask,
    })

@app.route('/toggle_entry')
def toggle_entry():
    try:
        if not system_state.entry_controlled_by_flask:
            system_state.entry_controlled_by_flask = True
        else:
            driver.toggle_entry_conveyor()
        
        return jsonify({
            'entry_state': system_state.entry_conveyor_state,
            'entry_controlled_by_flask': system_state.entry_controlled_by_flask,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/toggle_exit')
def toggle_exit():
    try:
        if not system_state.exit_controlled_by_flask:
            system_state.exit_controlled_by_flask = True
        else:
            driver.toggle_exit_conveyor()
        
        return jsonify({
            'exit_state': system_state.exit_conveyor_state,
            'exit_controlled_by_flask': system_state.exit_controlled_by_flask,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/toggle_sorter1')
def toggle_sorter1():
    try:
        if not system_state.sorter1_controlled_by_flask:
            system_state.sorter1_controlled_by_flask = True
        else:
            driver.toggle_sorter1()
        
        return jsonify({
            'sorter1_state': system_state.sorter1_state,
            'sorter1_controlled_by_flask': system_state.sorter1_controlled_by_flask,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/toggle_sorter2')
def toggle_sorter2():
    try:
        if not system_state.sorter2_controlled_by_flask:
            system_state.sorter2_controlled_by_flask = True
        else:
            driver.toggle_sorter2()
        
        return jsonify({
            'sorter2_state': system_state.sorter2_state,
            'sorter2_controlled_by_flask': system_state.sorter2_controlled_by_flask,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
@app.route('/toggle_sorter3')
def toggle_sorter3():
    try:
        if not system_state.sorter3_controlled_by_flask:
            system_state.sorter3_controlled_by_flask = True
        else:
            driver.toggle_sorter3()
        
        return jsonify({
            'sorter3_state': system_state.sorter3_state,
            'sorter3_controlled_by_flask': system_state.sorter3_controlled_by_flask,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/release_entry')
def release_entry():
    try:
        system_state.entry_controlled_by_flask = False
        return jsonify({
            'entry_state': system_state.entry_conveyor_state,
            'entry_controlled_by_flask': False,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/release_exit')
def release_exit():
    try:
        system_state.exit_controlled_by_flask = False
        return jsonify({
            'exit_state': system_state.exit_conveyor_state,
            'exit_controlled_by_flask': False,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/release_sorter1')
def release_sorter1():
    try:
        system_state.sorter1_controlled_by_flask = False
        return jsonify({
            'sorter1_state': system_state.sorter1_state,
            'sorter1_controlled_by_flask': False,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/release_sorter2')
def release_sorter2():
    try:
        system_state.sorter2_controlled_by_flask = False
        return jsonify({
            'sorter2_state': system_state.sorter2_state,
            'sorter2_controlled_by_flask': False,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/release_sorter3')
def release_sorter3():
    try:
        system_state.sorter3_controlled_by_flask = False
        return jsonify({
            'sorter3_state': system_state.sorter3_state,
            'sorter3_controlled_by_flask': False,
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    flask_thread = Thread(target=start_flask)
    flask_thread.daemon = True
    flask_thread.start()

    driver_thread = Thread(target=start_driver)
    driver_thread.daemon = True
    driver_thread.start()
    
    try:
        while True:
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Application ended")