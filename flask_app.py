from flask import Flask, render_template, jsonify
import time
from state import system_state

app = Flask(__name__)

def start_flask():
    app.run(debug=True, host='0.0.0.0', use_reloader=False)

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


@app.route('/get_counters')
def get_counters():
    return jsonify({
        'Blue_Counter': system_state.BlueCounter,
        'Green_Counter': system_state.GreenCounter,
        'Metal_Counter': system_state.MetalCounter,

    })

@app.route('/toggle_entry')
def toggle_entry():
    try:
        import driver  
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
        import driver  
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
        import driver  
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
        import driver  
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
        import driver  
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
    start_flask()