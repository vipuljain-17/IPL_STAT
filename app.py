from flask import Flask, render_template
app = Flask(__name__)

import pandas as pd

data = pd.read_csv("IPL_CSK_dataSheet.csv")
cols = data.columns
all_players_name = ['MS Dhoni', 'Ambati Rayudu', 'KM Asif', 'Dwayne Bravo', 'Deepak Chahar', 'Faf du Plessis', 'Imran Tahir', 'Narayan Jagadeesan', 
    'Karn Sharma', 'Lungi Ngidi', 'Michtell Santner', 'R Sai Kishore', 'Ravindra Jadeja', 'Robin Uthappa', 'Ruturaj Gaikwad', 'Sam Curran', 'Shardul Takhur',
    'Suresh Raina', 'Moeen Ali', 'Krishnappa Gowtham', 'Cheteshwar Pujara', 'Harishankar Reddy', 'C Hari Nishaanth', 'Bhagath Varma', 'Jason Behrendroff']

def return_stats(selected_name):
	values = data.loc[data.Player_Name == selected_name].values.ravel().tolist()
	d = dict(zip(cols, values))
	return d

@app.route('/')
def hello_world():
	return render_template('home.html', len = len(all_players_name),players_list = all_players_name)

@app.route('/players/<playername>')
def show_user_profile(playername):
	return render_template('profile.html', player_name = playername)

if __name__ == '__main__':
	app.run(debug=True)