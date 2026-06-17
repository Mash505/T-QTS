import json
import redis

class EventBus:

    def __init__(self, host="redis", port=6379):
        self.client = redis.Redis(host=host, port=6379, decode_responses=True)

    def publish(self, channel, event):
        self.client.publish(channel, json.dumps(event))

    def subscribe(self, channel):
        pubsub = self.client.pubsub()
        pubsub.subscribe(channel)
        return pubsub

    def push_stream(self, stream, data):
        self.client.xadd(stream, data)
