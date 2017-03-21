from flask import Flask, current_app
app = Flask(__name__)

@app.route('/')
def main():
    return current_app.send_static_file('drinkPage.html')

@app.route('/config')
def drinks():
    return current_app.send_static_file('config.json')

if __name__ == '__main__':
	app.run()