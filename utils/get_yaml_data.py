import os
import yaml

current_path = os.path.dirname(__file__)
file_path = os.path.join(current_path, '..', 'data\\desired_caps.yaml')


def get_yaml(node):
    file = open(file_path, 'r')
    result = file.read()
    yaml_file = yaml.full_load(result)
    return yaml_file[node]


print(get_yaml('first'))
