Questo repository lo sto utilizzando per poter esercitarmi su Flask, python , jinjia.

jinjia:

si ha la possibilità di estendere dei file html

quindi si crea un file base.html
esso può essere esteso con i comandi jinjia:
Si ha un filebase e dei file che lo estendono 

<!--file esteso -->
{%extends 'filebase.html' %}

{% block head%}
        <!-- qui si può scrivee ciò che si vuole, e vale solo per il file 2 -->
{% endblock%}
il blocco vale sia per head che per body

può essere utilizzato anche per poter fare un ciclo for all'interno di una struttura.
Ad esempio:
se nel file .py è stata definita una lista di elementi
elements=[
	{
		'name': 'Scatolo',
		'type': 'Oggetto',
		'color': 'Rosso'
	},
	{
		'name': 'Pistola',
		'type': 'Arma',
		'color': 'Nero'
	},
    {
		'name': 'Iphone X',
		'type': 'Smartphone',
	}
]

tale lista può essere richiamata all'interno del file esteso utilizzando un ciclo for:
nb si nota che gli elementi possono anche on essere tutti completi di tutti gli attributi.
 {% for el in elements %}
        <p>{{ el.name}}</p>
        <p>{{ el.type}}</p>
        {% if el.color%}
            <p>The color is {{ el.color}}</p>
        {% else%} 
            <p>it is uncolored</hp>
        {%endif%}

    {% endfor %}
{% endblock%}


per poter includere un file esterno, al posto di utilizzare href e il path
si utilizza href={{url_for('prima cartella del path','rimanente parte del path/nomefile + estensione')}}"
    <!--link rel="stylesheet" href="{{url_for('static',filename='css/main.css')}}">
############################################################
DATABASE:::::
[https://stackoverflow.com/questions/4371/how-do-i-retrieve-my-mysql-username-and-password]
[https://stackoverflow.com/questions/11657829/error-2002-hy000-cant-connect-to-local-mysql-server-through-socket-var-run]

pip install flask-sqlalchemy
riparti da 50.20
Una volta creata la classe BlogPost(db.Model) bisogna dover importare il database direttamente nel progetto.
Dalla directory principale in cui c'e' anche app.py
	python (Attenzione bisogna utilizzare python3!!!)
>>	from app import db
>>  db.create_all()
>>  from app import BlogPost (penso voglai dire che da nomefiele(.py) devo importare il nome della classe [class BlogPost(db.Model)])

>> BlogPost.query.all() [in questo modo si dovrebbe poter vedere tutto]
>> []
>>  db.session.add(BlogPost(title='Blog Post 1', content='Content of Blog Post 1 aajajaajajajja', author='Gianni'))

>>BlogPost.query.all()  
>>[Blog Post 1]  #questo perchè viene richiamata la funzione __repr__(self) e quindi ritorna 'Blog Post' + str(self.id)


>>> db.session.add(BlogPost(title='Blog Post 1', content='Questo è il ballo del quaqua', author='Gianni Colella'));
>>> db.session.add(BlogPost(title='La donna immobile', content="mai più malvento, muta d'accento e di pensiero"))
si ha la possibilità di visualizzare che i dati inseriti siano tutti:
>>> BlogPost.query.all()[2]
Blog post 3
>>> BlogPost.query.all()[2].content
"mai più malvento, muta d'accento e di pensiero"
>>> BlogPost.query.all()[2].author
'N/A'
>>> BlogPost.query.all()[2].date_posted
datetime.datetime(2020, 3, 21, 12, 54, 47, 982978)
vedi [https://www.w3schools.com/python/python_datetime.asp]
>>> 

>>> from app import db, BlogPost ##<----
	#if request.method=='POST':
	#	#insert dati from post into post.db
	#	post_title=request.form['title'] <----------------!!!!!! nella request.form ci vogliono le parentesi quadre!!!!!!
	#	post_content=request.form['content']
	#	new_post =BlogPost(title=post_title, content=post_content, author='Gianni')
	#	db.session.add(new_post)
	#	db.session.commit()
	#	return redirect('/posts')
	#else:



Quando si utilizza SQLAlchemy bisogna non tenere alcun altro processo che utilizza il db, altrimenti SQLAlchemy lo setta a locked!


si possono utilizzare delle direttivr del tipo
BlogPost.query.get(2) ..
db.session.delete(BlogPost.query.get(2))
una volta che un post è stato eliminato dal db, bisogna eseguire db.session.commit()
db.session.commit()


da terminale si può anche effettuare una modifica ad uno specifico row in tabella.
Ad esempio se si volesse modificare il nome dell'autore del secondo post.
BlogPost.query.get(2).author='Gigi'
e appena effettuato il commit 
db.session.commit() a


#####################
learn about javascript!!!!!!


