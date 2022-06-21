class Parser:
    def __init__(self, string, template):
        self.string = string
        self.template = template
        self.new_encode = {}
        
    def _make_positional(self, template, item):
        position_one = (
            0
            if not template[item][: template[item].find(":")]
            else int(template[item][: template[item].find(":")])
        )
        position_two = (
            0
            if not template[item][template[item].find(":") + 1 :]
            else int(template[item][template[item].find(":") + 1 :])
        )
        return self.string[position_one:position_two]
        
    def save_data(self):
        pass   
        
    def decode(self):
        # template to str
        pass

    def encode(self, template=None):
        # str to template
        template = self.template

        def recurssive(template=None):
            
            recursive_encode = {}
            for item in template:
                if type(template[item]) == dict:
                    recursive_encode[item] = recurssive(
                        template=template[item],
                    )
                    self.new_encode.update(recursive_encode)
                else:
                    recursive_encode[item] = self._make_positional(template, item)
            
            return recursive_encode
        
        recurssive(template)
        return self.new_encode

