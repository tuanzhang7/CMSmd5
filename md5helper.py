import hashlib


def get_first2digit(filename):
    md5 = hashlib.md5(filename).hexdigest()
    # print md5
    return md5[:2]


def get_third_digit(filename):
    md5 = hashlib.md5(filename).hexdigest()
    # print md5
    return md5[2:3]


