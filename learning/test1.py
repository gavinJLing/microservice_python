#!/usr/local/bin/python3

from flask import Flask, jsonify, abort, make_response

app = Flask(__name__)

id = ""

tasks = [
    {
        'id': 1,
        'title': u'Buy groceries',
        'description': u'Milk, Cheese, Pizza, Fruit, Tylenol',
        'done': False
    },
    {
        'id': 2,
        'title': u'Learn Python',
        'description': u'Need to find a good Python tutorial on the web',
        'done': False
    }
]

@app.route('/tasks/<int:task_id>', methods=['GET'])
def get_tasks(task_id):
    tasks = []
    task = [task for task in tasks if task['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})

@app.route('/task/<int:task_id>', methods=['GET'])
def get_task(task_id):
    the_task = []
    id = task_id
    for task in tasks:
        if task['id'] == task_id:
            the_task = task
            print('found: ', the_task)

    if len(the_task) == 0:
        print('not found: {0}'.format(id) )
        abort(404)

    return the_task
    #return jsonify({'task': the_task})




@app.errorhandler(404)
def not_found(error):
    print('Errorhandler not found: {0}'.format(id) )
    return make_response(jsonify({'error': 'Id: {0} Not found'.format(id) }), 404)


if __name__ == '__main__':
    app.run(debug=True)