


class Parser:
    def __init__(self, string, template):
        self.string = string
        self.templates = template
    
    def decode(self):
        # template to str
        pass
    
    def encode(self, template=None):
        #str to template
        if not self.template:
            template = self.template
        new_encode = {}
        for item in self.template:
            if type(item) ==  'dict':
                self.encode(template=template[item], )
    