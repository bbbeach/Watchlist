from  flask import Flask,render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, ForeignKey, String, Boolean, Column
import click

app = Flask(__name__, )
app.config['DEBUG'] = True
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+cymysql://root:mima@localhost:3306/movie'
db = SQLAlchemy(app)


class User(db.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(20))

class Movie(db.Model):
    id = Column(Integer, primary_key=True)
    title = Column(String(60))
    year = Column(String(4))

@app.route('/')
def index():
    user = User.query.first()
    movies = Movie.query.all()
    return render_template('index.html', name=user.name, movies=movies)

@app.errorhandler(404)
def page_not_found(e):
    user = User.query.first()
    return render_template('404.html'), 404

@app.context_processor
def load_user():
    user = User.query.first()
    return dict(user=user)

if __name__ == '__main__':
    db.create_all()
    app.run()

@app.cli.command()
def forge():

    name = 'Feng Jian'
    movies = [
        {'title': 'My Neighbor Totoro', 'year': '1988'},
        {'title': 'Dead Poets Society', 'year': '1989'},
        {'title': 'A Perfect World', 'year': '1993'},
        {'title': 'Leon', 'year': '1994'},
        {'title': 'Mahjong', 'year': '1996'},
        {'title': 'Swallowtail Butterfly', 'year': '1996'},
        {'title': 'King of Comedy', 'year': '1999'},
        {'title': 'Devils on the Doorstep', 'year': '1999'},
        {'title': 'WALL-E', 'year': '2008'},
        {'title': 'The Pork of Music', 'year': '2012'},
    ]
    user = User(name=name)
    db.session.add(user)
    for m in movies:
        movie = Movie(title=m['title'], year=m['year'])
        db.session.add(movie)
    db.session.commit()
    click.echo()