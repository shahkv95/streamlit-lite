def write_file(name, content):
    f = open("{}.txt".format(name), "w")
    f.write(content)
    f.close()
    return