from os import environ
from FlaskExercise import app

if __name__ == '__main__':
    HOST = environ.get('SERVER_HOST', 'localhost')
    try:
        PORT = int(environ.get('SERVER_PORT', '4444'))
    except ValueError:
        PORT = 4444
    app.run(HOST, PORT, debug=True)
