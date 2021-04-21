from flask import Flask, render_template,request, flash, url_for, redirect
from model import db,PlayerModel

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite3'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

import pandas as pd

data = pd.read_csv("IPL_CSK_dataSheet.csv")
cols = data.columns
all_players_name = ['MS Dhoni', 'Ambati Rayudu', 'KM Asif', 'Dwayne Bravo', 'Deepak Chahar', 'Faf du Plessis', 'Imran Tahir', 'Narayan Jagadeesan', 
    'Karn Sharma', 'Lungi Ngidi', 'Michtell Santner', 'R Sai Kishore', 'Ravindra Jadeja', 'Robin Uthappa', 'Ruturaj Gaikwad', 'Sam Curran', 'Shardul Takhur',
    'Suresh Raina', 'Moeen Ali', 'Krishnappa Gowtham', 'Cheteshwar Pujara', 'Harishankar Reddy', 'C Hari Nishaanth', 'Bhagath Varma', 'Jason Behrendroff']

def return_stats(selected_name):
	values = data.loc[data.Player_Name == selected_name].fillna("-").values.ravel().tolist()
	d = dict(zip(cols, values))
	if d['IPL_Debut'] != "-":
		d['IPL_Debut'] = int(d['IPL_Debut'])
	if d['Matches_played'] != "-":
		d['Matches_played'] = int(d['Matches_played'])
	if d['Runs_Scored'] != "-":
		d['Runs_Scored'] = int(d['Runs_Scored'])
	if d['50s'] != "-":
		d['50s'] = int(d['50s'])
	if d['100s'] != "-":
		d['100s'] = int(d['100s'])
	if d['Wickets_Taken'] != "-":
		d['Wickets_Taken'] = int(d['Wickets_Taken'])

	
	return d

@app.route('/')
def hello_world():
	return render_template('home.html', len = len(all_players_name),players_list = all_players_name)

@app.route('/players/<playername>')
def show_user_profile(playername):
	return render_template('profile.html', player_name = playername, stats=return_stats(playername))

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
	app.run(debug=True)