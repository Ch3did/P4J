from p4j.parser import Parser


def test_parser(template, positional_string):
    formated_dict = Parser(positional_string).decode(**template)
    assert formated_dict["a"] == "abc"
    assert formated_dict["b"] == "defgh"
    assert formated_dict['c'] == {
        'x': 'ij',
        'y': 'kl',
        'z': {
            "w": 'mnopqrstuvx',
            "u": 'yw',
            "v": ''
        }
    }
