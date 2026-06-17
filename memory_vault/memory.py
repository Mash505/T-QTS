import json
import time

class MemoryVault:

    def __init__(self):
        self.memory = []

    def save_event(self, event_type, data):
        record = {
            "type": event_type,
            "data": data,
            "timestamp": time.time()
        }
        self.memory.append(record)
        return record

    def get_all(self):
        return self.memory

    def find_by_type(self, event_type):
        return [
            m for m in self.memory
            if m["type"] == event_type
        ]
