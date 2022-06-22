from p4j.parser import Parser


def test_parser(template, positional_string):
    p = Parser(string=positional_string, template=template).encode()

    assert p.data["a"] == "abc"
    assert p.data["b"] == "defgh"
    assert p.data['c'] == {
        'x': 'ij',
        'y': 'kl',
        'z': {
            "w": 'mnopqrstuvx',
            "u": 'yw',
            "v": ''
        }
    }
