from flask import Flask
from flask import request
import json

app = Flask(__name__)

users = []

# Method that "calculate" the sign based in the day and month
def set_sign(day, month):
    astro_sign = ""
    int_day = int(day)
    int_month = int(month)

    if int_month == 12:
    	astro_sign = 'Sagittarius' if (int_day < 22) else 'Capricorn'
    elif int_month == 1:
	    astro_sign = 'Capricorn' if (int_day < 20) else 'Aquarius'
    elif int_month == 2:
	    astro_sign = 'Aquarius' if (int_day < 19) else 'Pisces'
    elif int_month == 3:
	    astro_sign = 'Pisces' if (int_day < 21) else 'Aries'
    elif int_month == 4:
	    astro_sign = 'Aries' if (int_day < 20) else 'Taurus'
    elif int_month == 5:
	    astro_sign = 'Taurus' if (int_day < 21) else 'Gemini'
    elif int_month == 6:
	    astro_sign = 'Gemini' if (int_day < 21) else 'Cancer'
    elif int_month == 7:
	    astro_sign = 'Cancer' if (int_day < 23) else 'Leo'
    elif int_month == 8:
	    astro_sign = 'Leo' if (int_day < 23) else 'Virgo'
    elif int_month == 9:
	    astro_sign = 'Virgo' if (int_day < 23) else 'Libra'
    elif int_month == 10:
	    astro_sign = 'Libra' if (int_day < 23) else 'Scorpio'
    elif int_month == 11:
	    astro_sign = 'Scorpio' if (int_day < 22) else 'Sagittarius'
    
    print(astro_sign)
    return astro_sign

#################################

@app.route('/')
def hello():
    return "Hello World!"

@app.route('/users/<name>', methods=['GET', 'POST'])

def register_user(name):
    if request.method == 'POST':
        json_user = request.get_json()

        name = json_user['name']

        users.append(json_user)

        return f"o usuario {name} foi salvo"


@app.route('/users', methods=['GET', 'POST'])

def load_users():
    if request.method == 'GET':
        return json.dumps(users)


@app.route('/sign/<name>', methods=['GET', 'POST'])

def view_user_sign(name):
    if request.method == 'GET':
        user_json = request.get_json()
    
        user_sign_johnson = {
            "name": user_json['name'],
            "birth_day": user_json['birth_day'],
            "birth_month": user_json['birth_month'],
            "birth_year": user_json['birth_year'],
            "sign": set_sign(user_json['birth_day'], user_json['birth_month'])
        }

        return user_sign_johnson


if __name__ == '__main__':
    app.run()