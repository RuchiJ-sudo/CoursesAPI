from flask import Flask, jsonify

app = Flask(__name__)


courses = [{'name': "Python programming",
            'course_id': "0",
            'Description': "hello",
            'price': "55000"
            },
           {'name': "Python programming",
            'course_id': "1",
            'Description': "hello",
            'price': "55000"
            },
           {'name': "Python programming",
            'course_id': "2",
            'Description': "hello",
            'price': "55000"
            },
           {'name': "Python programming",
            'course_id': "3",
            'Description': "hello",
            'price': "55000"}
           ]


@app.route('/')
def index():
    return 'Welcome to the course API'


@app.route("/courses", methods=['GET'])
def get():
    return jsonify({'Courses': courses})


@app.route("/courses/<int:course_id>", methods=['GET'])
def get_course(course_id):
    return jsonify({'course': courses[course_id]})


@app.route("/courses", methods=['POST'])
def create():
    course = {'name': "Python programming",
              'course_id': "5",
              'Description': "hello",
              'price': "55000"
              }
    courses.append(course)
    return jsonify({'Created': course})


@app.route("/courses/<int:course_id>", methods=['DELETE'])
def delete(course_id):
    courses.remove(courses[course_id])
    return jsonify({'result': True})


@app.route("/courses/<int:course_id>", methods=['PUT'])
def course_update(course_id):
    courses[course_id]['Description'] = "XYZ"
    return jsonify({'course': courses[course_id]})


if __name__ == '__main__':
    app.run(debug=True)
 
 