import redis

# redis_instance = redis.Redis(host="localhost", port=6379, db=0)
redis_instance = redis.Redis(host="192.168.1.188", port=6379, db=0)

subscriber = redis_instance.pubsub()
subscriber.subscribe('apollo')

# import ipdb; ipdb.set_trace()
while True:
    message = subscriber.get_message()
    if message:
        print (message['data'])
    else:
        print ("No message received")
