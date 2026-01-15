from flask import Flask, render_template
import csv
application = Flask(__name__)
@application.route('/')
def dashboard():
    return render_template('index.html')

@application.route('/ohioState')
def ohioState():
    team_id=1
    ohioStatePlayers = []
        with open('data/players.csv') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["teamID"] == str(team_id):
                ohioStatePlayers.append(row)
    return render_template('ohioState.html', players=ohioStatePlayers)

@application.route('/houston')
def houston():
    teamID=2
    houstonPlayers = []
        with open('data/players.csv') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["teamID"] == str(team_id):
                houstonPlayers.append(row)
    return render_template('houston.html', players=houstonPlayers)

@application.route('/georgia')
def georgia():
    teamID=3
    georgiaPlayers = []
        with open('data/players.csv') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["teamID"] == str(team_id):
                georgiaPlayers.append(row)
    return render_template('georgia.html', players=georgiaPlayers)

@application.route('/lsu')
def lsu():
    teamID=4
    lsuPlayers = []
        with open('data/players.csv') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["teamID"] == str(team_id):
                lsuPlayers.append(row)
    return render_template('lsu.html', players=lsuPlayers)

@application.route('/tennessee')
def tennessee():
    teamID=5
    tennesseePlayers = []
        with open('data/players.csv') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["teamID"] == str(team_id):
                tennesseePlayers.append(row)
    return render_template('tennessee.html', players=tennesseePlayers)

if __name__ == '__main__':
    application.run(debug=True)
