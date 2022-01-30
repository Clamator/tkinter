from pathlib import *

current_dir = Path.cwd()
home_dir = Path.home()

print(current_dir, home_dir)

file = current_dir / 'fiio2.txt'

print(file.read_text())