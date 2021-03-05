from flask import Flask
from flask import request
import json

app = Flask(__name__)

users = []

def post_user(user):
    
    if user not in users:
        users.append(user)
        return f"o usuário {user} foi salvo."
    else:
        return f"o usuário {user} já existe."
    
def get_user(user):
    if user in users:
        return user
    else:
        return 'erro, usuario nao encontrado'

@app.route('/get_users')
def get_users():
        return json.dumps(users)

@app.route('/user', methods=['POST'])
def user():
        user = request.get_json()
        return post_user(user)

def get_sign(birth_day, birth_month):
    
        birth_day = int(birth_day) 
        birth_month = int(birth_month)

        if 21 <= birth_day  and birth_month == 1 or birth_day <= 19 and birth_month == 2:
            return 'Aquario'
        elif 20 <= birth_day  and birth_month == 2 or birth_day <= 20 and birth_month == 3:
            return 'Peixes'
        elif 21 <= birth_day  and birth_month == 3 or birth_day <= 20 and birth_month == 4:
            return 'Aries'
        elif 21 <= birth_day  and birth_month == 4 or birth_day <= 20 and birth_month == 5:
            return 'Touro'
        elif 21 <= birth_day  and birth_month == 5 or birth_day <= 20 and birth_month == 6:
            return 'sign: Gemeos'
        elif 21 <= birth_day  and birth_month == 6 or birth_day <= 21 and birth_month == 7:
            return 'Cancer'
        elif 22 <= birth_day  and birth_month == 7 or birth_day <= 22 and birth_month == 8:
            return 'Leao'
        elif 23 <= birth_day  and birth_month == 8 or birth_day <= 22 and birth_month == 9:
            return 'Virgem'   
        elif 23 <= birth_day  and birth_month == 9 or birth_day <= 22 and birth_month == 10:
            return 'Libra'
        elif 23 <= birth_day  and birth_month == 10 or birth_day <= 21 and birth_month == 11:
            return 'Escorpião'
        elif 22 <= birth_day  and birth_month == 11 or birth_day <= 21 and birth_month == 12:
            return 'Sagitario'
        elif 22 <= birth_day  and birth_month == 12 or birth_day <= 20 and birth_month == 1:
            return 'Capricornio'
        else:
            return 'erro, signo nao encontrado'


@app.route('/sign/<name>')
def sign(name):

    for user in users: 
        if name == user['name']:
            birth_day = user['birth_day']
            birth_month = user['birth_month']
            signo = get_sign(birth_day, birth_month) 
            user['sign'] = signo
            return user
            
        else:
            return 'erro, usuario nao encontrado'

if __name__ == '__main__':
    app.run()