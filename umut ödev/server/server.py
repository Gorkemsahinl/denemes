from flask import Flask , jsonify
from datetime import datetime

app = Flask(__name__)

son_post_zamani = None
@app.route('/health-check', methods=['GET'])
def health_check():
    return {'status': 'Sistem çalışıyor'}

@app.route('/post-zamani' ,methods=['GET'])
def post_zaman():

    global son_post_zamani

    suankizaman = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    son_post_zamani = suankizaman

    return jsonify({'zaman' : son_post_zamani})



if __name__ == '__main__':
    app.run(debug=True)
