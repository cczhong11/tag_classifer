import yaml

class GeneralFilter(object):
    data = None
    def __init__(self, filepath):
        
        with open(filepath) as f:
            self.data = yaml.load(f, Loader=yaml.FullLoader)
    
    def filter(self, text):
        for tag, matches in self.data.items():
            if any(x in text for x in matches):
                return tag
        return None
