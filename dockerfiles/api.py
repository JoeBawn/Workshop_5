import redis
import json
from flask import jsonify, Flask

r = redis.StrictRedis(
host='localhost',
port='6379',
charset="utf-8",
decode_responses=True)

def lambda_handler(event, context):
	counter = r.incr('counter')

	return {
		"statusCode": 200,
		"body": json.dumps({
			"counter": counter,
	    }),
	}

hkey = 'redisobject:all_hour'
dict_from_redis = r.get('all_hour')

app = Flask(__name__)
@app.route('/')
def json():
    return jsonify(data=dict_from_redis, success=True, error={})

app.run(host='127.0.0.1', port=9999, debug=True)