""" Take an archive file downloaded from NCDC HAS and rename the files to what
 GEMPAK wants """
import glob
import shutil
import os
import sys
import time
import subprocess
import mx.DateTime
prods = ['EET', 'N0R', 'N0Q', 'NET']

os.chdir("ncdc")
for filegz in glob.glob("*.tar.gz"):
    cnt = 0
    print 'Processing', filegz
    subprocess.call("tar -xzf %s" % (filegz,), shell=True)
    for file in glob.glob("*_*_*_[0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]"):
        parts = file.split("_") # KABR_SDUS33_PTAABR_201212231126
        # STL_20121230_2137_TV0
        # nexrad/NIDS/DMX/N0Q/N0Q_20140801_1304
        if parts[2][:3] in prods:
            mydir = "/chinook/ldm/nexrad/NIDS/%s/%s" % (parts[0][1:], parts[2][:3])
            if not os.path.isdir(mydir):
                os.makedirs(mydir)
            newfn = "%s_%s_%s" % (parts[2][:3], parts[3][:8], parts[3][8:12])
            shutil.copyfile(file, mydir +"/"+ newfn)
        os.remove(file)
        cnt += 1
    #os.remove(filegz)
    print 'did', cnt
