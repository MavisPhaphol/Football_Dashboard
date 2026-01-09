from flask import Flask, render_template
import csv
application = Flask(__name__)
@application.route('/')
def dashboard():
    return render_template('index.html')

@application.route('/ohioState')
def ohioState():
    team_id=1
    players = []
        with open('data/players.csv') as file:
        reader = csv.DictReader(file)

        for row in reader:
            if row["teamID"] == str(team_id):
                players.append(row)
    return render_template('ohioState.html', players=players)

@application.route('/houston')
def houston():
    teamID=2
    return render_template('houston.html')

@application.route('/georgia')
def georgia():
    teamID=3
    return render_template('georgia.html')

@application.route('/lsu')
def lsu():
    teamID=4
    return render_template('lsu.html')

@application.route('/tennessee')
def tennessee():
    teamID=5
    return render_template('tennessee.html')

if __name__ == '__main__':
    application.run(debug=True)
