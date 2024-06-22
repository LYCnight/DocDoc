from flask import Flask, request, jsonify
import pandas as pd
import os
from flask_cors import CORS

from pathlib import Path		
import sys
root_path = Path(__file__).parent.parent    # 项目根目录    DocDoc
cur_path = Path(__file__).parent    # 当前目录    DocDoc/Evaluation
sys.path.append(str(cur_path))
sys.path.append(str(root_path))


app = Flask(__name__)
CORS(app)

# Path to the folder containing user tables
DATA_FOLDER = str(cur_path) + "/data/"

# Example of loading data for a specific user
def load_user_data(group, user):
    filename = f'group_{group}_user_{user}.xlsx'
    filepath = os.path.join(DATA_FOLDER, filename)
    if os.path.exists(filepath):
        return pd.read_excel(filepath)
    else:
        return None

# User authentication
users = {
    'user_1': 'password1',
    'user_2': 'password2',
    'user_3': 'password3',
    'user_4': 'password4',
    'user_5': 'password5',
    'user_6': 'password6',
    'user_7': 'password7',
    'user_8': 'password8',
    'user_9': 'password9',
}

# Route for user login
@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get('username')
    password = data.get('password')

    if users.get(username) == password:
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "failure", "message": "Invalid credentials"}), 401

# Route to get articles for a user
@app.route('/articles/<group>/<user>', methods=['GET'])
def get_articles(group, user):
    df = load_user_data(group, user)
    if df is not None:
        articles = df.to_dict(orient='records')
        return jsonify(articles), 200
    else:
        return jsonify({"status": "failure", "message": "Data not found"}), 404


# Route to update evaluation
@app.route('/evaluate/<group>/<user>/<article_id>', methods=['POST'])
def evaluate_article(group, user, article_id):
    df = load_user_data(group, user)
    if df is not None:
        data = request.json
        for key in ['Fluency', 'Coherence', 'Consistency', 'Relevance', 'Length', 'Structure', 'Text_style', 'Adversarial_success']:
            df.loc[df['shuffled_id'] == int(article_id), key] = data.get(key)
        filename = f'group_{group}_user_{user}.xlsx'
        filepath = os.path.join(DATA_FOLDER, filename)
        df.to_excel(filepath, index=False)
        return jsonify({"status": "success"}), 200
    else:
        return jsonify({"status": "failure", "message": "Data not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)