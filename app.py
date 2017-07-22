from flask import Flask
from redis import Redis

app = Flask(__name__)
redis = Redis(host='redis', port=6379)

@app.route('/')
def get():
    info = redis.info(section=None)
    return 'Total commands processed : {} \n'.format(info['total_commands_processed'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
