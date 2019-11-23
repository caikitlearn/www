from www import app # init file

from flask import render_template

##==================================================##
##   HOME PAGE                                      ##
##==================================================##
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

##==================================================##
##   BLOG                                           ##
##==================================================##
@app.route('/blog')
def blog():
    return render_template('blog/blog.html')

@app.route('/basketball-reference-hall-of-fame-probabilities')
def basketball_reference_hall_of_fame_probabilities():
    return render_template('blog/basketball-reference-hall-of-fame-probabilities.html')

@app.route('/stirlings-pogs')
def stirlings_pogs():
    return render_template('blog/stirlings-pogs.html')

@app.route('/stephen-ai-smith')
def stephen_ai_smith():
    return render_template('blog/stephen-ai-smith.html')

##==================================================##
##   MISC                                           ##
##==================================================##
@app.route('/misc')
def misc():
    return render_template('misc/misc.html')

@app.route('/tractor')
def tractor():
    return render_template('misc/tractor.html')
