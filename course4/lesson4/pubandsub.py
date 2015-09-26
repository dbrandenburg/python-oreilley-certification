#!/usr/bin/env python3
class Publisher:
    def __init__(self):
        self.subscribers  = []
    def subscribe(self, subscriber):
        if subscriber in self.subscribers:
            raise ValueError("Multiple subscriptions are not allowed")
        self.subscribers.append(subscriber)
    def unsubscribe(self, subscriber):
        if subscriber not in self.subscribers:
            raise ValueError("Can only unsubscribe subscribers")
        self.subscribers.remove(subscriber)
    def publish(self, s):
        # Create a copy of self.subscribers to avoid index shifting during
        # ineration
        subscribers = self.subscribers.copy()
        for subscriber in subscribers:
            subscriber(s)

if __name__ == '__main__':
    def multiplier(s):
        print(2*s)

    class SimpleSubscriber:
        def __init__(self, name, publisher):
            self.name = name
            self.publisher = publisher
            self.process_calls_count = 0
            publisher.subscribe(self.process)
        def process(self, s):
            # Incrementing calls of this method
            self.process_calls_count += 1
            print(self, ":", s.upper())
            # Unsubscribing in case method has been called 3 times
            if self.process_calls_count == 3:
                self.publisher.unsubscribe(self.process)
                # Reset process_calls count
                self.process_calls_count = 0
        def __repr__(self):
            return self.name

    publisher = Publisher()
    publisher.subscribe(multiplier)
    for i in range(6):
        newsub = SimpleSubscriber("Sub" + str(i), publisher)
        line = input("Input {}: ".format(i))
        publisher.publish(line)
