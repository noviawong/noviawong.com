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


@app.route('/UX')
def UX():
    return render_temp('UX')


@app.route('/resume')
def resume():
    return render_temp('resume')

@app.route('/design')
def design():
    return render_temp('design')

@app.route('/contact')
def contact():
    return render_temp('contact')

@app.route('/UX/class')
def classprojects():
    return render_temp('classprojects')

@app.route('/UX/independent')
def independent():
    return render_temp('independent')

@app.route('/UX/independent/thesis')
def thesis():
    return render_temp('thesis')

@app.route('/UX/independent/mealspace')
def mealspace():
    return render_temp('mealspace')

@app.route('/UX/class/somethingblue')
def somethingblue():
    return render_temp('somethingblue')

@app.route('/UX/class/RHCA')
def RHCA():
    return render_temp('RHCA')

@app.route('/UX/independent/VECTR')
def VECTR():
    return render_temp('VECTR')

@app.route('/UX/independent/VM')
def VM():
    return render_temp('VM')

@app.route('/UX/class/ferndale')
def ferndale():
    return render_temp('ferndale')

@app.route('/UX/class/Cengage')
def Cengage():
    return render_temp('Cengage')

@app.route('/UX/class/ARVR')
def ARVR():
    return render_temp('ARVR')

@app.route('/UX/independent/plateforward')
def plateforward():
    return render_temp('plateforward')

@app.route('/UX/techsmith')
def techsmith():
    return render_temp('techsmith')

@app.route('/about')
def about():
    return render_temp('aboutwebsite')

@app.route('/challenge1')
def challenge1():
    return render_temp('challenge1')

@app.route('/challenge2')
def challenge2():
    return render_temp('challenge2')

@app.route('/challenge3')
def challenge3():
    return render_temp('challenge3')

@app.route('/challenge4')
def challenge4():
    return render_temp('challenge4')

@app.route('/challenge5')
def challenge5():
    return render_temp('challenge5')


if __name__ == '__main__':
    app.run(debug=True)
    