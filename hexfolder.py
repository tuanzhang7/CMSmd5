import os


def create_dir(path):
    for x in range(256):
        directory = os.path.join(path, chr(x).encode("hex"))
        if not os.path.exists(directory):
            os.makedirs(directory)
        for y in range(16):
            directory = os.path.join(path, chr(x).encode("hex"),chr(y).encode("hex")[1])
            if not os.path.exists(directory):
                os.makedirs(directory)
            print chr(x).encode("hex"), chr(y).encode("hex")[1]


create_dir("Z:\projects\TEST\LMS")
