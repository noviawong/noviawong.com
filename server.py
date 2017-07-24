#!/usr/bin/env python3

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/project')
def project():
    return render_template('project.html')


@app.route('/research')
def research():
    return render_template('research.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/classprojects')
def classprojects():
    return render_template('classprojects.html')

@app.route('/independent')
def independent():
    return render_template('independent.html')

if __name__ == '__main__':
    app.run(debug=True)
