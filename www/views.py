from www import app # init file

from flask import render_template, jsonify, request
import pandas as pd
import numpy as np

##==================================================##
##   HOME PAGE                                      ##
##==================================================##
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

##==================================================##
##   DATA SCIENCE                                   ##
##==================================================##
@app.route('/datascience')
def datascience():
    return render_template('datascience/datascience.html')

@app.route('/hot-hub-time-machine')
def hot_hub_time_machine():
    return render_template('datascience/hot-hub-time-machine.html')

@app.route('/the-making-of-hot-hub-time-machine')
def the_making_of_hot_hub_time_machine():
    return render_template('datascience/the-making-of-hot-hub-time-machine.html')

@app.route('/scraping-data-from-basketball-reference')
def scraping_data_from_basketball_reference():
    return render_template('datascience/scraping-data-from-basketball-reference.html')

@app.route('/basketball-reference-hall-of-fame-probabilities')
def basketball_reference_hall_of_fame_probabilities():
    return render_template('datascience/basketball-reference-hall-of-fame-probabilities.html')

##==================================================##
##   STATISTICS                                     ##
##==================================================##
@app.route('/statistics')
def statistics():
    return render_template('statistics/statistics.html')

@app.route('/stirlings-pogs')
def pogs():
    return render_template('statistics/stirlings-pogs.html')

##==================================================##
##   MISC                                           ##
##==================================================##
@app.route('/misc')
def misc():
    return render_template('misc/misc.html')

@app.route('/tractor')
def tractor():
    return render_template('misc/tractor.html')

##==================================================##
##   HOT HUB TIME MACHINE BGP                       ##
##==================================================##
