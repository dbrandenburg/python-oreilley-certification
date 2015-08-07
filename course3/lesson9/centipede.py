class Centipede(object):
    """Centipede Attriubte maintanance"""
    def __init__(self):
        self.__dict__['stomach'] = []
        self.__dict__['legs'] = []
            
    def __call__(self, *args, **kwargs):
        self.__setattr__(args, None)

    def __setattr__(self, key, value):
        
        if key in ('stomach', 'legs'):
            raise AttributeError
        
        if key and not value:
            self.__dict__['stomach'] += list(key)
        
        if key and value:
            self.__dict__[key] = value
            self.__dict__['legs'].append(key)
     
    def __repr__(self):
        return str(",".join(self.legs))

    def __str__(self):
        return str(",".join(self.stomach))