from flask import Flask, request, jsonify, render_template, redirect, url_for
from datetime import datetime

app = Flask(__name__, template_folder='templates')


def generate_password():
    currentTime = datetime.now()
    hours = currentTime.hour
    minutes = currentTime.minute

    existing_values = [11, 36, 66, 48]
    combined_values = [str(int(value) + hours + minutes) for value in existing_values]

    password = ''.join(combined_values)
    return password

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    if not request.json or 'password' not in request.json:
        return jsonify({'success': False}), 400


    # debuging
    submitted_password = request.json['password']
    print('Submitted password:', submitted_password)
    # generate the current valid password
    current_password = generate_password()
    print('Current password:',current_password)

    # compare the submitted password with the current valid one
    if submitted_password == current_password:
        #redirect to success page
        return redirect(url_for('LoginSuccessful'))
    else:
        # redirect to error page
        return redirect(url_for('error'))
        
    
@app.route('/LoginSuccessful')
def LoginSuccessful():
    return render_template('LoginSuccessful.html')

@app.route('/error')
def error():
    return render_template('error.html')

if __name__ == '__main__':
    app.run(debug=True, port=5000)
