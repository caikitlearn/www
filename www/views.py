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

@app.route('/scraping-data-from-basketball-reference')
def scraping_data_from_basketball_reference():
    return render_template('blog/scraping-data-from-basketball-reference.html')

@app.route('/basketball-reference-hall-of-fame-probabilities')
def basketball_reference_hall_of_fame_probabilities():
    return render_template('blog/basketball-reference-hall-of-fame-probabilities.html')

@app.route('/stirlings-pogs')
def stirlings_pogs():
    return render_template('blog/stirlings-pogs.html')

##==================================================##
##   MISC                                           ##
##==================================================##
@app.route('/misc')
def misc():
    return render_template('misc/misc.html')

@app.route('/tractor')
def tractor():
    return render_template('misc/tractor.html')
