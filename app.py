import json
from flask import Flask
from flask import request

app = Flask(__name__)

users = []

def post_user(user):
    
    if user not in users:
        users.append(user)
        return f"o usuário {user['name']} foi adicionado."
    else:
        return f"o usuário {user['name']} já existe."
    
def get_user(user_name):
    for u in users:
        if u['name'] == user_name:
            u["sign"] = get_sign(u)
            return u

def get_sign(user):
    day = int(user['birth_day'])
    month = int(user['birth_month'])

    print(day)
    print(month)

    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return 'Aries'
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return 'Touro'
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        return 'Gêmeos'
    elif (month == 6 and day >= 21) or (month == 7 and day <= 22):
        return 'Câncer'
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return 'Leão'
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return 'Virgem'
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        return 'Libra'
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        return 'Escorpião'
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        return 'Sagitário'
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return 'Capricórnio'
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return 'Aquário'
    elif (month == 2 and day >= 19) or (month == 3 and day <= 20):
        return 'Peixes'     

#################################

@app.route('/register', methods=['POST'])
def register():
    if request.method == 'POST':
        json = request.get_json()
        return post_user(json)

@app.route('/users')
def list_users():
        return json.dumps(users)

@app.route('/sign/<name>')
def sign(name):
        return get_user(name)

@app.route('/jsonrequest', methods=['GET', 'POST'])
def jsonrequest():
    if request.method == 'POST':
        json = request.get_json()
        print(json)
        return json

if __name__ == '__main__':
    app.run()