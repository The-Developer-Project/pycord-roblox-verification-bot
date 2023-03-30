from flask import Flask, request, abort
from replit import db
from threading import Thread
import time, os
app = Flask('')
@app.route('/')
def main():
    return "Your bot is alive!"


def run():
    app.run(host="0.0.0.0", port=8080)


def keep_alive():
    server = Thread(target=run)
    server.start()

@app.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST':
        token = str(request.data)
        token = token.replace("'", '')
        token = token[1:]
        token = token.split('+')
        if not token[2] == os.environ['roauth']:
          return 'access denied'
        dbname = token[0] + '+temp'
        dbvalue = token[1]
        db[dbname] = dbvalue
        return 'success', 200
    else:
        abort(400)
