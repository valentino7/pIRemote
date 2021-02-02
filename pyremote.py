#!/usr/bin/env python3

from flask import Flask, request, jsonify
import subprocess

app = Flask(__name__)
ir_ctl = "/usr/bin/ir-ctl"

# Not very extensible, not really modular, nor particularly flexible. Will improve in the future
@app.route('/object', methods=['POST'])
def switch():
    query = request.json.get('obj',"NA")

    ir_action = "--send="
    ventilatore = "/home/pi/button.txt"
    action = ""

    print("received:", query)
    if query == "acceso":
        action = "button.txt"

    if len(action) > 1:
        cmd = [ir_ctl, ir_action + ventilatore ]
        print(cmd)
        if subprocess.call(cmd) == 0:
            return "success"

    return "error with query: " + query

if __name__ == '__main__':
    app.run(host= '0.0.0.0',debug=False,port=8000)
