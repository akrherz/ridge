import glob
import shutil
import os
import sys
import time
import subprocess
import mx.DateTime
prods = ['DPA','N1P','NTP']

os.chdir("ncdc")
for filegz in glob.glob("*.tar.Z"):
    cnt = 0
    print 'Processing', filegz
    subprocess.call("tar -xzf %s" % (filegz,), shell=True)
    for file in glob.glob("*_*_*_201006[0-9][0-9][0-9][0-9][0-9][0-9]"):
        parts = file.split("_") # KABR_SDUS33_PTAABR_201212231126
        # STL_20121230_2137_TV0
        newfp = "%s_%s_%s_%s" % (parts[0][1:], parts[3][:8], parts[3][8:12],
                                 parts[2][:3])
        if parts[2][:3] in prods:
            print file, newfp
            shutil.copyfile(file, "/mesonet/ridge/input/"+ newfp)
        os.remove(file)
        cnt += 1
    while len(glob.glob("/mesonet/ridge/input/*")) > 10:
        print 'Sleeping!',
        time.sleep(30)
    print 'did', cnt
