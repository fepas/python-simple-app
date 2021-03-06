from flask import Flask
from flask import request
import json

app = Flask(__name__)

users = []

def post_user(user):
    
    if user not in users:
        users.append(user)
        return f"o usuário {user['name']} foi adicionado."
    else:
        return f"o usuário {user['name']} já existe."
    
def get_user(user):
    if user in users:
        return user
    else:
        return 'erro, usuario nao encontrado'

#################################

@app.route('/')
def hello():
    return "Lyra!"

@app.route('/jsonrequest', methods=['GET', 'POST'])
def jsonrequest():
    if request.method == 'POST':
        json = request.get_json()
        print(json)
        return json

@app.route('/set_user', methods=['GET', 'POST'])
def set_user():
    #Exemplo de json de usuário
    # {
    # "name":"Felipe Campos",
    # "birth_day": "14",
    # "birth_month": "05",
    # "birth_year": "1998"
    # }
    if request.method == 'POST':
        json = request.get_json()
        return post_user(json)
        

@app.route('/get_all_users', methods=['GET', 'POST'])
def get_all_users():
    if request.method == 'GET':
        return json.dumps(users)

@app.route('/sign/<name>', methods=['GET', 'POST'])
def get_user_sign(name):
    if request.method == 'GET':
        json = request.get_json()

        for u in users:
            if name == u["name"]:
                day = int(u["birth_day"])
                month = int(u["birth_month"])
                sign = get_sign(day,month)

                u["sign"] = sign

                return u

        return 'Nenhum usuário encontrado, por favor, adicione esse usuário utilizando o dominio set_user'

def get_sign(day, month):
    s = ''
    print(day)
    print(month)
    print(month == 1 and day <= 20)

    #aries 21/03 a 20/04
    if (month == 3 and day >= 21) or (month == 4 and day <= 20):
        s ='Aries'
    #touro 21/04 a 20/05
    elif (month == 4 and day >= 21) or (month == 5 and day <= 20):
        s = 'Touro'
    #gemeos 21/05 a 20/06
    elif (month == 5 and day >= 21) or (month == 6 and day <= 20):
        s = 'Gemeos'
    #cancer 22/06 a 21/07
    elif (month == 6 and day >= 22) or (month == 7 and day <= 21):
        s = 'Cancer'
    #leao 22/07 a 22/08
    elif (month == 7 and day >= 22) or (month == 8 and day <= 22):
        s = 'Leao'
    #virgem 23/08 a 22/09
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        s = 'Virgem'
    #libra 23/09 a 22/10
    elif (month == 9 and day >= 23) or (month == 10 and day <= 22):
        s = 'Libra'
    #escorpiao 23/10 a 21/11
    elif (month == 10 and day >= 23) or (month == 11 and day <= 21):
        s = 'Escorpiao'
    #sagitario 22/11 a 21/12
    elif (month == 11 and day >= 22) or (month == 12 and day <= 21):
        s = 'Sagitario'
    #capricorinio 22/12 a 20/01
    elif (month == 12 and day >= 22) or (month == 1 and day <= 20):
        s = 'Capricornio'
    #aquario 21/01 a 19/02
    elif (month == 1 and day >= 21) or (month == 2 and day <= 19):
        s = 'Aquario'
    #peixes 20/02 a 20/03
    elif (month == 2 and day >= 20) or (month == 3 and day <= 20):
        s = 'Peixes'
    else:
        s = 'Data inválida'

    print(s)
    return s

if __name__ == '__main__':
    app.run()