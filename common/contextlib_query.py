class Query(object):
    def __init__(self, name):
        self.name = name
    
    def __enter__(self):
        print('Bean')
        return self

    def __exit__(self, exec_type, exec_value, traceback):
        if exec_type:
            print('Error')
        else:
            print('End')
    def query(self):
        print('query info about %s...' % self.name)

with Query('Bob') as q:
    q.query()
	
	

