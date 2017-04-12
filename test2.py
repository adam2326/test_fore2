#import python non standard libraries
from flask import Flask, render_template

# import python standard lib
import json
import datetime

# GAE imports
from google.appengine.api import urlfetch


app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == "GET":
		return render_template("index.html")
	if request.method == "POST":
		# set some query params
		today = datetime.date.today()
	    end_date = str(today - datetime.timedelta(days=1))
	    start_date = str(today - datetime.timedelta(days=60))
	    ticker = request.form['ticker']
	    # create the url to call
	    url = 'https://www.quandl.com/api/v3/datasets/WIKI/' + ticker + '.json?&start_date=' + start_date + '&end_date=' + end_date + '&column_index=4&api_key=NryMyVQ2MHgRxhxKbq6W'
	    #url = 'http://www.google.com/humans.txt'
	    # make the API call to Quandl
	    result = urlfetch.fetch(url)
	    #response = urlfetch.fetch(url, validate_certificate=true)
	    if result.status_code == 200:
	        stock_data = [i for i in json.loads(result.content)['dataset']['data'] ]
	        stock_data.sort(key=lambda x: x[0])
	        return render_template("goog_production.html", stock_data = stock_data)
	    else:
	        return "<html><body> {} </body></html>".format( "fuck")