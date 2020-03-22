#app.py
from flask import Flask, render_template,request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime #per poter utilizzare datetime.iutcnow nel database (BlogPost . date_posted!

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///posts.db'


#bisogna definire il db
#creare il database
db=SQLAlchemy(app)

class BlogPost(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(100),nullable=False) #questo campo e' obbligatorio!
	content= db.Column(db.Text, nullable=False)
	author= db.Column(db.String(20), nullable=False, default='N/A') #in questo modo si specifica che nel caso in cui l'auore non esiste, esso viene posto di default a 'N/A'
	date_posted= db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

	#questa repr viene chiamata ogni qualvolta aggiungiamo un blogpost  
	def __repr__(self):
		return 'Blog post ' + str(self.id )		 


#Define structures, dictionary
all_posts=[
	{
		'title': 'Post 1',
		'content': 'This is the content of post 1. Lalalalalallalalalalla.',
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

@app.route('/posts', methods=['GET','POST'])
def posts():
	#read from database
	if request.method=='POST':
		#insert dati from form into post.db
		post_title=request.form['title']
		post_content=request.form['content']
		new_post =BlogPost(title=post_title, content=post_content, author='GianniForm')
		db.session.add(new_post)
		db.session.commit()
		return redirect('/posts')
	else:
		#	si va a sovrascrivere la variabile all_posts, ma stavolta si va a caricare da db!
		all_posts= BlogPost.query.order_by(BlogPost.date_posted).all()
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
