from flask import Flask,render_template,request,redirect
import ulysses
from ulysses import ithica 

app = Flask(__name__)

app.vars={}
urls=""

@app.route('/index',methods=['GET'])
def index():
    	return render_template('tool.html')

@app.route('/index',methods=['POST'])
def index2():
	app.vars['url'] = request.form['url']
	urls = str(app.vars['url'])
	ulysses.ithaca(urls)

	title = ulysses.title
	wcount = ulysses.wcount

	return render_template('result.html',ptitle=title)

if __name__ == "__main__":
    app.run()