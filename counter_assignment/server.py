from crypt import methods
from flask import Flask, render_template, redirect, request, session # Import Flask to allow us to create our app 
app = Flask(__name__) # Create a new instance of the Flask class called "app" 
app.secret_key= 'supersecretkey'

@app.route('/')
def visits():
    if 'visitCount' in session:
        session['visitCount'] += 1
    else:
        session['visitCount'] = 0
    return render_template('index.html')

@app.route('/add2')
def add2():
    if 'visitCount' in session:
        session['visitCount'] += 2
    else:
        session['visitCount'] = 0
    return render_template('index.html')

@app.route('/destroy_session')
def reset():
    session.clear()
    return redirect('/')

@app.route('/custom_increase', methods=['POST'])
def customIncrease():
    print(request.form)
    session['incrementAmount'] = int(request.form['incrementAmount'])
    if 'visitCount' in session:
        session['visitCount'] += (session['incrementAmount'] -1)
    else:
        session['visitCount'] = 0
    return redirect('/')


if __name__=="__main__": # Ensure this file is being run directly and not from a different module  
    app.run(debug=True, port=5001) # Run the app in debug mode. 