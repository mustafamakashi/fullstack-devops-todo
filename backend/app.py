from flask import Flask, request, jsonify
from flask_cors import CORS
import database

app = Flask(__name__)
CORS(app)

database.init_db()

@app.route("/todos", methods=["GET"])
def get_todos():
    conn = database.get_connection()
    cur = conn.cursor()
    cur.execute("SELECT id, task FROM todos;")
    todos = cur.fetchall()
    cur.close()
    conn.close()
    return jsonify([{"id": row[0], "task": row[1]} for row in todos])

@app.route("/todos", methods=["POST"])
def add_todo():
    task = request.json.get("task")
    conn = database.get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO todos (task) VALUES (%s) RETURNING id;", (task,))
    new_id = cur.fetchone()[0]
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"id": new_id, "task": task}), 201

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
