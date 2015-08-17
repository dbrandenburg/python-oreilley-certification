import redis
import subprocess
import threading


class rdColClient:
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        
    def subscribe_node(self, node_name):
        self.r.srem('nodeslist', node_name) # For testing
        self.r.sadd('nodeslist',node_name)
        
    def process_node_queue(self, node):
        """Pulls the latest command from the node queue and splits it into arguments (needed by subprocess)
        before executing and redirecting the output to the output queue"""
        cmd = self.r.rpop(node)
        cmd = cmd.split()
        out = subprocess.Popen(cmd, stdout=subprocess.PIPE)
        while True:
            line = out.stdout.readline()
            if line:
                self.r.publish('outputCommandQueue', line)
            else:
                break
        self.r.publish('outputCommandQueue', 'bla')
        #r.lpush('outputCommandQueue', 'Output of ' + node + ' :' + str(output))
        
    def print_all_members(self):
        print(self.r.smembers('nodeslist'))

class rdColServer:
    def __init__(self):
        self.r = redis.StrictRedis(host='localhost', port=6379, db=0)
        
    def send_command_to_node_queues(self, cmd):
        for node in self.r.smembers('nodeslist'):
            self.r.lpush(node,cmd)
    
    def pull_output_queue(self):
        threading.Thread.__init__(self)
        pubsub = self.r.pubsub()
        pubsub.subscribe('outputCommandQueue')
        while True:
            for message in pubsub.listen():
                print(message)
        
    def clear_expired_queues(self):
        pass
    
client = rdColClient()
client.subscribe_node('testnode01')

server = rdColServer()
server.send_command_to_node_queues('ls -la')
server.pull_output_queue()

client.process_node_queue('testnode01')


