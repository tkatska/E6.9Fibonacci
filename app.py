from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

def fib(n):
    a, b = 1, 1
    for x in range(n):
        a, b = b, a + b
    return a

# @app.route('/')
# def hello():
#     count = 4
#     return 'Hello World! I have been seen {} times.\n'.format(count)

@app.route('/fib/<int:n>')
def fib_handler(n):
    redisNum = redis.get(n)
    if redisNum is not None:
        return (redisNum)
    result = fib(n)
    redis.set(n, result)
    return str((result))

if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)