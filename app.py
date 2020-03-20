#app.py
from flask import Flask, render_template

app=Flask(__name__)

all_posts=[
	{
		#structures, dictionary
		'title': 'Post 1',
		'content': 'This is the content of post 1. Lalalalalallalalalalla.'
		'author': 'Gianni'
	},
{
		'title': 'Post 2',
		'content': 'This  post 2. Lihihihhiihlalalalallalalalalla.'
	}
]




@app.route('/')
def index():
	return render_template('index.html')

@app.route('/posts')
def posts():
	return render_template('/posts.html', posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name,id):
	return "Hello, "+ name + "your id is " + str(id)

@app.route('/onlyget', methods=['GET','POST'])
#si possono specificare anche i metodi permessi per un particolare path
#in questo caso funzionano sia la GET che la POST.
#ma se togo GET, significa che non c sara' la possibilita' di potersi connettere con una get da browser.
def get_req():
	return 'you can only get this webpage 3.'

if __name__=="__main__":
	app.run(debug=True)
