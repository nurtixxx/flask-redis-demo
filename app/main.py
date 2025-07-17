from flask import Flask
import redis
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
r = redis.Redis(
    host=os.getenv("REDIS_HOST", "localhost"),
    port=int(os.getenv("REDIS_PORT", 6379)),
    decode_responses=True
)

@app.route('/ping')
def ping():
    return "pong"

@app.route('/')
def index():
    count = r.incr('hits')
    return f'сосал  {count} раз(а).'

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
