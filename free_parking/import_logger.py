import sys

name = str(__file__)
index = name.index('\\free_parking\imports.py') + 1
sys.path.append(name[:index])
