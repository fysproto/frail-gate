import os
from flask import Flask, render_template, request

# 引数なしの Flask(__name__) で、自動的に templates フォルダを探します
app = Flask(__name__)

@app.route('/')
def index():
    # URLから値を抜き出す
    eid = request.args.get('eid', '')
    uid = request.args.get('uid', '')
    # templates/index.html を表示し、値を渡す
    return render_template('index.html', eid=eid, uid=uid)

if __name__ == "__main__":
    app.run(debug=False, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))