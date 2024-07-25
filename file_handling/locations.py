import os

# current file
print('File name:', os.path.basename(__file__))  # locations.py

# current file directory
print('Current Directory:', os.path.dirname(__file__))  # C:\Users\Lenovo\PycharmProjects\Python_ZeroToMastery\file_handling
dir1 = os.path.dirname(os.path.abspath('...'))
print('Current Directory:', dir1)  # C:\Users\Lenovo\PycharmProjects\Python_ZeroToMastery\file_handling
loc1 = os.path.abspath('.')
print('Current Directory:', loc1)  # C:\Users\Lenovo\PycharmProjects\Python_ZeroToMastery\file_handling

# project directory
ll = os.path.dirname(os.path.abspath('.'))
print('Project Location:', ll)  # C:\Users\Lenovo\PycharmProjects\Python_ZeroToMastery
loc = os.path.abspath('..')
print('Project Location:', loc)  # C:\Users\Lenovo\PycharmProjects\Python_ZeroToMastery

# other
pathLoc = os.path.join(os.path.dirname(__file__), "file\\dummy.png")
print('Concatenated Path:', pathLoc)  # C:\Users\Lenovo\PycharmProjects\Python_ZeroToMastery\file_handling\file\dummy.png
directory = os.path.dirname(os.path.abspath('..'))
print(directory)  # C:\Users\Lenovo\PycharmProjects
