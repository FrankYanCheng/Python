from flask import Flask,url_for
from flask import abort
from flask import redirect
from flask import render_template

app=Flask(__name__)

@app.route('/test')
def test():
	#return  url_for('login')
	return '<h1>Hello World!</h1>'

@app.route('/user/<name>')
def sayHello(name):
	if name=='baidu':
		return redirect('www.baidu.com')
	elif name=='no':
		return abort(404)
	return '<h1>Hello,%s</h1>' % name

@app.route('/hello')
@app.route('/hello/<name>')
def hello(name=None):
	return render_template('hello.html',name=name)


if __name__=='__main__':
	app.run(host='fyc.pub')
