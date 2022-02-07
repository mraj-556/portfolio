from flask import Flask, request, render_template, url_for, redirect

app=Flask(__name__)

@app.route('/')
def prehome():
    return render_template('prehome.html')
@app.route('/homepage')
def homepage():
    return render_template('homepage.html')
@app.route('/project')
def project():
    return render_template('myproject.html')
@app.route('/blog')
def blog():
    return render_template('blog.html')
@app.route('/about')
def about():
    return render_template('about.html')
@app.route('/contact')
def contact():
    return render_template('contact.html')
@app.route('/feed')
def feed():
    return render_template('feedback.html')

@app.route('/bio')
def bio():
    return render_template('biohome.html')
@app.route('/address')
def address():
    return render_template('address.html')
@app.route('/education')
def education():
    return render_template('education.html')
@app.route('/achieve')
def achieve():
    return render_template('Achievement.html')
@app.route('/skill')
def skill():
    return render_template('skill.html')
@app.route('/hobby')
def hobby():
    return render_template('hobby.html')


if __name__=='__main__':
    app.run(debug=True)