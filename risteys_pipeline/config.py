import os
from pathlib import Path

root_dir = os.path.realpath(os.path.join(os.path.dirname(__file__), '..'))
finngen_data_path = os.path.join(root_dir, 'data', 'lung.csv')
finregistry_data_path = os.path.join(root_dir, 'data', 'lung.csv')
