import os
for root, dirs, files in os.walk(".",True):
    print("path:" + root)
    print("directories:" + str(dirs))
    print("files:" + str(files))
    print("########")
