from flask_sqlalchemy import SQLAlchemy
 
db =SQLAlchemy()
 
class PlayerModel(db.Model):
    __tablename__ = "players"
 
    id = db.Column(db.Integer, primary_key=True)
    fav_player_name = db.Column(db.String(100))
    predicted_team_for_cup = db.Column(db.String(100))
 
    def __init__(self, fav_player_name, predicted_team_for_cup):
        self.fav_player_name = fav_player_name
        self.predicted_team_for_cup = predicted_team_for_cup
 
    def __repr__(self):
        return f"{self.fav_player_name}:{self.predicted_team_for_cup}"