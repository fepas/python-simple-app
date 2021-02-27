from flask import Flask
from flask import request

app = Flask(__name__)

users = []

def post_user(user):
    
    if user not in users:
        users.append(user)
        return f"o usuário {user} foi adicionado."
    else:
        return f"o usuário {user} já existe."
    
def get_user(user):
    if user in users:
        return user
    else:
        return 'erro, usuario nao encontrado'

#################################

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/user/<username>', methods=['GET', 'POST'])
def user(username):
    if request.method == 'POST':
        return post_user(username)
    else:
        return get_user(username)

@app.route('/jsonrequest', methods=['GET', 'POST'])
def jsonrequest():
    if request.method == 'POST':
        json = request.get_json()
        print(json)
        return json

if __name__ == '__main__':
    app.run()