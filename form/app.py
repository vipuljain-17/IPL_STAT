from flask import Flask, request, flash, url_for, redirect, render_template
from model import db,PlayerModel


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)


@app.before_first_request
def create_tables():
    db.create_all()

@app.route('/data/create' , methods = ['GET','POST'])
def create():
    if request.method == 'GET':
        return render_template('createpage.html')
 
    if request.method == 'POST':
        fav_player_name = request.form['fav_player_name']
        predicted_team_for_cup = request.form['predicted_team_for_cup']
        player = PlayerModel(fav_player_name= fav_player_name,predicted_team_for_cup= predicted_team_for_cup)
        db.session.add(player)
        db.session.commit()
        return redirect('/data')

@app.route('/data')
def show_all():
    players = PlayerModel.query.all()
    return render_template('show_all.html',players = players)

if __name__ == '__main__':
   app.run(debug = False)
