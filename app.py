from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

def get_db():
    return psycopg2.connect(
        host="db",
        database="library",
        user="postgres",
        password="postgres"
    )

@app.route("/books")
def books():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, status FROM books")
    rows = cur.fetchall()
    return jsonify(rows)

@app.route("/available")
def available():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE status='available'")
    return jsonify(cur.fetchall())

@app.route("/taken")
def taken():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE status='taken'")
    return jsonify(cur.fetchall())

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)