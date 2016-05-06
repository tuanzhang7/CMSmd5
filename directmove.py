import logging
import md5helper
import lms
import os

logger = logging.getLogger('mylogger')


def move_by_path(rootdir):
    folder_counter = 0
    file_counter = 0
    dirlist = os.listdir(rootdir)
    dirlist.sort()
    for dir1 in dirlist:
        if os.path.isdir(os.path.join(rootdir, dir1)):
            # /LMS/00,ff
            path_level1 = os.path.join(rootdir, dir1)
            if folder_counter >= 10: break
            logger.info("processing...." + path_level1)
            folder_counter += 1
            dirlist1 = os.listdir(path_level1)
            first = True
            for dir2 in dirlist1:
                if first:
                    logger.info("moving....")
                    first = False
                source = os.path.join(rootdir, dir1, dir2)
                if os.path.isfile(source):
                    if source.endswith(".mrc"):
                        filename = lms.md5name(dir2)
                        # LMS/00/f/1231234.mrc
                        digit2 = md5helper.get_first2digit(filename)
                        digit1 = md5helper.get_third_digit(filename)
                        target = os.path.join(rootdir, digit2, digit1, dir2)

                        # if not os.path.exists(os.path.dirname(target)):
                        #     try:
                        #         os.makedirs(os.path.dirname(target))
                        #     except OSError as exc:  # Guard against race condition
                        #         raise
                        os.rename(source, target)
                        file_counter += 1
                        print ("moving:" + source + " " + target)

    logger.info("Total Folder:" + str(folder_counter))
    logger.info("Total Files:" + str(file_counter))
    return file_counter
