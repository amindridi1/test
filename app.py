from flask import Flask, jsonify, request

app = Flask(__name__)

# Sample route for getting device status
@app.route('/api/devices', methods=['GET'])
def get_devices():
    devices = [
        {'id': 1, 'name': 'Living Room Light', 'status': 'off'},
        {'id': 2, 'name': 'Thermostat', 'status': 'on'},
    ]
    return jsonify(devices)

# Sample route for controlling devices
@app.route('/api/devices/<int:device_id>', methods=['POST'])
def control_device(device_id):
    data = request.json
    # Here you would add logic to control your device based on the ID and data
    return jsonify({'message': f'Device {device_id} status changed to {data["status"]}'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
