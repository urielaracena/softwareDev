'''Uriel Aracena
Lab 13 Flask application
'''

from flask import Flask, render_template, redirect, url_for

'''create an object 'app' from the Flask module
    __name__ set to __main__ if the script is running from the main file
'''

app =  Flask(__name__)

# set the routing to the main page
# 'route' decorator is used to access the root URL
@app.route('/')
def index():
    name = "Uriel"
    fruits = ['apple', 'orange', 'grapes']
    checkfruit = 'apple'
    return render_template('index.html', username=name, listfruits=fruits, checkedfruit=checkfruit)

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/users')
def users():
    return render_template('users.html')

@app.route('/quotes')
def quotes():
    return redirect(url_for("index"))


# set the 'app' to run f you execute the file directly(not when its imported)
if __name__ == '__main__':
    app.run(debug=True)