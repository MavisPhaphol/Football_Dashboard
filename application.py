from flask import Flask, render_template

application = Flask(__name__)
@application.route('/')
def dashboard():
    return render_template('index.html')

@application.route('/ohioState')
def ohioState():
    return render_template('ohioState.html')

@application.route('/houston')
def houston():
    return render_template('houston.html')

@application.route('/georgia')
def georgia():
    return render_template('georgia.html')

@application.route('/lsu')
def lsu():
    return render_template('lsu.html')

@application.route('/tennessee')
def tennessee():
    return render_template('tennessee.html')

if __name__ == '__main__':
    application.run(debug=True)
