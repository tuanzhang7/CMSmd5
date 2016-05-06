import os
import lms
import md5helper
import logging

logger = logging.getLogger('root')


def move_by_textfile(textfile, rootdir):
    counter = 0
    fil = open(textfile)
    for line in fil:
        line = line.strip()
        filename = line[line.rindex("\\")+1:]
        # dir1 = line[line.rindex("\\") - 2:line.rindex("\\")]
        # dir2 = line[line.rindex("\\") - 2:line.rindex("\\")]

        md5name = lms.md5name(filename)
        # LMS/00/f/1231234.mrc
        digit2 = md5helper.get_first2digit(md5name)
        digit1 = md5helper.get_third_digit(md5name)
        target = os.path.join(rootdir, digit2, digit1, filename)
        source = os.path.join(rootdir, digit2, filename)
        try:
            os.rename(source, target)
        except OSError as exc:  # Guard against race condition
            logger.error("File Not Exist: " + source)

        counter += 1
        print source, target
    return counter
