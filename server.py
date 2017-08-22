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


@app.route('/research')
def research():
    return render_temp('research')

@app.route('/contact')
def contact():
    return render_temp('contact')

@app.route('/project/class')
def classprojects():
    return render_temp('classprojects')

@app.route('/project/independent')
def independent():
    return render_temp('independent')

@app.route('/about')
def about():
    return render_temp('aboutwebsite')

if __name__ == '__main__':
    app.run(debug=True)
    