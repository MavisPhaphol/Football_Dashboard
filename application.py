from flask import Flask, render_template

application = Flask(__name__)
@application.route('/')
def dashboard():
    return render_template('index.html')

@application.route('/ohioState')
def ohioState():
    teamID=1
    return render_template('ohioState.html')

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
