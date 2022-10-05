from p4j.template import Template


class Parser:
    def __init__(self, string):
        self.string = string
        self.new_encode = {}

    def _make_positional_coordinates(self, template, item):
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

    def encode(self):
        pass

    def decode(self, **kwargs):
        self.template = Template(**kwargs).template
        def recurssive(template=None):
            recursive_encode = {}
            response_encode = {}
            dict_keys = []
            for chave in template:
                if type(template[chave]) == dict:
                    dict_keys.append(chave)
                else:
                    response_encode[chave] = self._make_positional_coordinates(template, chave)
            for item in dict_keys:
                new_template = template[item]
                recursive_encode[item] = recurssive(template=new_template)
            recursive_encode.update(response_encode)
            return recursive_encode

        try:
            template = self.template
            
            return recurssive(template)
        except Exception as error:
            return error
