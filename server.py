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


@app.route('/research')
def research():
    return render_temp('research')


@app.route('/paper')
def paper():
    return render_temp('paper')

@app.route('/design')
def design():
    return render_temp('design')

@app.route('/contact')
def contact():
    return render_temp('contact')

@app.route('/research/class')
def classprojects():
    return render_temp('classprojects')

@app.route('/research/independent')
def independent():
    return render_temp('independent')

@app.route('/research/independent/thesis')
def thesis():
    return render_temp('thesis')

@app.route('/research/independent/mealspace')
def mealspace():
    return render_temp('mealspace')

@app.route('/research/class/somethingblue')
def somethingblue():
    return render_temp('somethingblue')

@app.route('/research/class/RHCA')
def RHCA():
    return render_temp('RHCA')

@app.route('/research/independent/VECTR')
def VECTR():
    return render_temp('VECTR')

@app.route('/research/independent/VM')
def VM():
    return render_temp('VM')

@app.route('/research/class/Ferndale')
def Ferndale():
    return render_temp('Ferndale')

@app.route('/research/class/Cengage')
def Cengage():
    return render_temp('Cengage')

@app.route('/about')
def about():
    return render_temp('aboutwebsite')

if __name__ == '__main__':
    app.run(debug=True)
    