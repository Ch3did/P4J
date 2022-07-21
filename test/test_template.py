from p4j.template import Template
import mock
from unittest.mock import patch
import os
import pytest

def mock_load_file_method(filename, max_retries=5):
    file = os.path.dirname(os.path.abspath(__file__)) +'/config_test_cases/'+ filename
    with open(file) as f:
        return eval(f.read())

def test_template_with_config_file():
    with mock.patch.object(Template, '_Template__filename', new_callable=mock.PropertyMock) as obj_mock:
        obj_mock.return_value = 'test-p4j-config.json'
        mock_load_file = patch('p4j.template.load_file', new=mock_load_file_method).start()
        mock_load_file = mock_load_file_method
        template = Template()
        assert template.template == {'a': "1:1", 'b': "2-2"}

@pytest.mark.parametrize("filename", [
    ('test-error-1-p4j-config.json'),
    ('test-error-2-p4j-config.json'),
    ('test-error-3-p4j-config.json'),
    ('test-error-4-p4j-config.json'),
    ('test-error-5-p4j-config.json'),
    ('test-error-6-p4j-config.json'),
    ('test-error-7-p4j-config.json'),  
])
def test_template_with_config_file_repeatable_values(filename): #raise exception test
    with pytest.raises(ValueError) as e_info:
        with mock.patch.object(Template, '_Template__filename', new_callable=mock.PropertyMock) as obj_mock:
            obj_mock.return_value = filename
            mock_load_file = patch('p4j.template.load_file', new=mock_load_file_method).start()
            mock_load_file = mock_load_file_method
            template = Template()
