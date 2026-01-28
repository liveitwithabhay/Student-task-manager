from flask import Flask, jsonify, request, render_template
import json
import os

app = Flask(__name__)
TASKS_FILE = 'tasks.json'

if not os.path.exists(TASKS_FILE):
    with open(TASKS_FILE, 'w') as f:
        json.dump([], f)

def load_tasks():
    with open(TASKS_FILE, 'r') as f:
        return json.load(f)

def save_tasks(tasks):
    with open(TASKS_FILE, 'w') as f:
        json.dump(tasks, f, indent=2)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/tasks', methods=['GET'])
def list_tasks():
    return jsonify(load_tasks())


@app.route('/api/tasks', methods=['POST'])
def add_task():
    data = request.get_json()
    task = {'id': len(load_tasks()) + 1, 'title': data['title']}
    tasks = load_tasks()
    tasks.append(task)
    save_tasks(tasks)
    return jsonify(task), 201

if __name__ == '__main__':
    app.run(debug=True, port=5000)
