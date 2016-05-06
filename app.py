import logger
import textfile
import time
import directmove
import xmlhelper
import os

log = logger.getlogger('mylogger')
rootdir = "/alfresco_content/OneSearch/Physical_Resources/LMS"

# rootdir = raw_input("Enter Path:")
# if len(rootdir) <= 0:
#     rootdir = "/alfresco_content/OneSearch/Physical_Resources/LMS"

print ("1. Move by Textfile")
print ("2. Move directly")
print ("3. Generate sample metadata files")
choice = raw_input("enter choice:")

if choice == "1":
    txtfile = raw_input("Enter text file:")
    if len(txtfile) <= 0:
        txtfile = "textfiles/alf_path.txt"

    start = time.time()
    counter = textfile.move_by_textfile(txtfile, rootdir)
    end = time.time()
    speed = counter / (end - start)
    log.info(txtfile + " processed :" + str(counter) + " Speed: " + str(int(speed)) + "/second")
elif choice == "2":
    start = time.time()
    counter = directmove.move_by_path(rootdir)
    end = time.time()
    speed = counter / (end - start)
    log.info(str(counter) + " Speed: " + str(int(speed)) + "/second")
elif choice == "3":
    ext = ".metadata.properties.xml"
    for y in range(1, 10):
        folder = "folder" + str(y);
        if not os.path.exists(folder):
            os.makedirs(folder)
        for x in range(1, 10):
            filename = "IMG_"+str(x)+".jpg"
            metadata_filename = filename+ext
            metadata_filepath = os.path.join(folder, metadata_filename)
            xmlhelper.write_metadata_xml(metadata_filepath)
            try:
                filepath = os.path.join(folder, filename)
                file = open(filepath, 'a')
                file.close()
            except:
                print("error occured")
    end = time.time()








