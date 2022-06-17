import os

def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def load_file(filename, max_retries=5):
    current_path = get_project_root() + '/'
    for i in range(max_retries):
        try:
            with open(os.path.join(current_path, filename)) as f:
                return f.read()
        except FileNotFoundError:
            current_path = os.path.dirname(current_path)
    raise FileNotFoundError(filename)
