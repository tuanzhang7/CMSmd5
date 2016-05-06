LMSEXT="LMS"


def md5name(lms_file_name):
    md5filename = lms_file_name.replace(".mrc", "") + LMSEXT
    return md5filename
