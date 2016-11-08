from flask import Flask,render_template,request,redirect
import ulysses

app = Flask(__name__)

app.vars={}
urls=""
#app.vars={}


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

	#title variable here ulysses.title

	#title = 



	return render_template('result.html',ptitle=title)
	#return render_template('result.html')





  

if __name__ == "__main__":
    app.run()