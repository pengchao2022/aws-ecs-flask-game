from flask import Flask, render_template, request, jsonify
import psycopg2
import os
import json

app = Flask(__name__)

# 数据库配置
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_NAME = os.getenv('DB_NAME', 'flask_game')
DB_USER = os.getenv('DB_USER', 'postgres')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_PORT = os.getenv('DB_PORT', '5432')

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT
    )

def init_db():
    conn = get_db_connection()
    cur = conn.cursor()
    
    # 创建游戏分数表
    cur.execute('''
        CREATE TABLE IF NOT EXISTS scores (
            id SERIAL PRIMARY KEY,
            player_name VARCHAR(100) NOT NULL,
            score INTEGER NOT NULL,
            created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    conn.commit()
    cur.close()
    conn.close()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/scores', methods=['GET'])
def get_scores():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT player_name, score FROM scores ORDER BY score DESC LIMIT 10')
        scores = cur.fetchall()
        cur.close()
        conn.close()
        
        return jsonify([{'player_name': row[0], 'score': row[1]} for row in scores])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/scores', methods=['POST'])
def add_score():
    try:
        data = request.get_json()
        player_name = data.get('player_name')
        score = data.get('score')
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            'INSERT INTO scores (player_name, score) VALUES (%s, %s)',
            (player_name, score)
        )
        conn.commit()
        cur.close()
        conn.close()
        
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    init_db()
    app.run(host='0.0.0.0', port=5000, debug=False)