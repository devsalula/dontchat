from Flask import Blueprint
from flask_socketio import SocketIO

app = Blueprint('socket', __name__)
socketio = SocketIO(app)

@socketio.on('join_chat')
def join_chat_event(data):
    app.logger.info("{} joined in the chat {}".format(data['username'], data['chatId']))