# import os

# def write_file(name, content):
#     ROOT_DIR = os.path.realpath(os.path.join(os.path.dirname(__file__)))
#     relative_directory = os.path.join(ROOT_DIR, 'data', 'results')
#     f = open(relative_directory +'/' + "{}.txt".format(name), "w+")
#     f.write(content)
#     f.close()
#     return

# import shutil
# shutil.move("path/to/current/file.foo", "path/to/new/destination/for/file.foo")

def write_file(name, content):
    filename = "{}.txt".format(name)
    f = open(filename, "w")
    f.write(content)
    f.close()
    return