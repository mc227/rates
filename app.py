"""
This API mocks the data
"""
import random
import threading
import time
from flask_cors import CORS
from flask import Flask, jsonify

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "http://127.0.0.1:5500"}})

data = {
    'x': 50,
    'y': 50,
    'z': 50
}

def update_data():
    """
    updated data
    """
    global data
    while True:
        # Update the values of the data object with random values
        data['x'] = random.randint(0, 100)
        data['y'] = random.randint(0, 100)
        data['z'] = random.randint(0, 100)
        time.sleep(10)  # Wait for 1 seconds before updating again

# Start the timer to update the data object
timer = threading.Thread(target=update_data)
timer.start()

@app.route('/api/data', methods=['GET'])
def get_data():
    """
    get data
    """
    # Return the data object as JSON
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
