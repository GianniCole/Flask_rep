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
_________________________________________________
DATABASE:::::
[https://stackoverflow.com/questions/4371/how-do-i-retrieve-my-mysql-username-and-password]
https://stackoverflow.com/questions/11657829/error-2002-hy000-cant-connect-to-local-mysql-server-through-socket-var-run

pip install flask-sqlalchemy
riparti da 50.20
from flask_sql 