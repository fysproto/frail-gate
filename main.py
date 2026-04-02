import os
from flask import Flask, render_template, request

app = Flask(__name__, template_folder='.')

@app.route('/')
def index():
    # URLパラメータを取得（表示用）
    eid = request.args.get('eid', '')
    uid = request.args.get('uid', '')
    return render_template('index.html', eid=eid, uid=uid)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))