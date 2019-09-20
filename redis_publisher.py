import redis
import random
messages = ['Hi apollo', 'How you doing', 'This is a test']

# redis_instance = redis.Redis(host='localhost', port=6379, db=0)
redis_instance = redis.Redis(host='192.168.1.188', port=6379, db=0)

while True:
    message_id = random.randrange(0, 2)
    redis_instance.publish('apollo', messages[message_id])


