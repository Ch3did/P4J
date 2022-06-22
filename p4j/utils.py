import bisect
import os


def get_project_root():
    return os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_file(filename, max_retries=5):
    current_path = get_project_root() + "/"
    for i in range(max_retries):
        try:
            with open(os.path.join(current_path, filename)) as f:
                return eval(f.read())
        except FileNotFoundError:
            current_path = os.path.dirname(current_path)
    raise FileNotFoundError(filename)


def validate(
    target_dict, allowed_separators=["-", ":"], integer_only=True, non_repeatable=True
):
    """
    allowed_separators: list of allowed separators for values. Default is ["-", ","]
    integer_only: if True, only integers are allowed for values.
    """
    already_seen = []
    for k, v in target_dict.items():
        if isinstance(v, dict):
            validate(v, allowed_separators, integer_only, non_repeatable)
            continue
        if not v:
            raise ValueError("Value for key '{}' is empty".format(k))
        if not isinstance(v, str):
            raise ValueError("Value for key '{}' is not a string".format(k))
        values = try_split(v, allowed_separators)
        for value in values:
            if integer_only:
                try:
                    int(value)
                except ValueError:
                    raise ValueError("Value '{}' is not an integer.".format(value))
            if non_repeatable:
                if len(already_seen) > 1:
                    if value >= already_seen[0] and value <= already_seen[-1]:
                        raise ValueError("Value '{}' is not unique.".format(value))
                bisect.insort(already_seen, value)


def try_split(string, separators):
    for separator in separators:
        if string.find(separator) != -1:
            return string.split(separator)
    raise ValueError(
        "Could not split string '{}' with separators {}".format(string, separators)
    )
