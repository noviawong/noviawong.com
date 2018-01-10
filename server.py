#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

def render_temp(name):

    def pageclass(pgname):
        if pgname == name:
            return 'current'
        else:
            return 'other'

    return render_template(
        name + '.html',
        page=name,
        pageclass=pageclass
    )

@app.route('/')
def index():
    return render_temp('index')


@app.route('/project')
def project():
    return render_temp('project')


@app.route('/paper')
def paper():
    return render_temp('paper')

@app.route('/contact')
def contact():
    return render_temp('contact')

@app.route('/project/class')
def classprojects():
    return render_temp('classprojects')

@app.route('/project/independent')
def independent():
    return render_temp('independent')

@app.route('/project/independent/thesis')
def thesis():
    return render_temp('thesis')

@app.route('/project/independent/mealspace')
def mealspace():
    return render_temp('mealspace')

@app.route('/project/independent/somethingblue')
def somethingblue():
    return render_temp('somethingblue')

@app.route('/project/independent/RHCA')
def RHCA():
    return render_temp('RHCA')

@app.route('/about')
def about():
    return render_temp('aboutwebsite')

if __name__ == '__main__':
    app.run(debug=True)
    