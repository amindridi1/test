from flask import Flask, render_template
from flask_socketio import SocketIO, send

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
socketio = SocketIO(app, cors_allowed_origins="*")

@app.route('/')
def index():
    return render_template('index.html')  # Frontend page

@socketio.on('message')
def handle_message(msg):
    send(msg, broadcast=True)  # Broadcast to all clients

if __name__ == '__main__':
    socketio.run(app, debug=True)
