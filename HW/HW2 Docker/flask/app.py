import os
from flask import Flask, make_response, request

app = Flask(__name__)

@app.route('/')
def hello():
    response = make_response(
        {
            'response': 'Hello, World!',
            'status': 200
        }
    )
    return response

@app.route('/repeat', methods=['GET'])
def handle_repeat():
    if request.method == 'GET':
        # if we wanted to be more careful we could validate that our response is not some default value and return some sort of error message
        value = request.args['input']
        response = make_response(
            {
                'body': value,
                'status': 200
            }
        )
        return response

if __name__ == '__main__':
    # By default flask is only accessible from localhost.
    # Set this to '0.0.0.0' to make it accessible from any IP address
    # on your network (not recommended for production use)
    port_number = int(os.getenv("PORT"))
    app.run(host='0.0.0.0', port=port_number,  debug=True)
