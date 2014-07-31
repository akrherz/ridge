import glob
import shutil
import os
import sys
import time
import mx.DateTime
prods = ['TR0','TV0','N0Q','N0S','N0Z','N0U','NET']

os.chdir("/data/gempak/nexrad/NIDS")
for nexrad in glob.glob("???"):
    print 'Processing', nexrad,
    cnt = 0
    os.chdir(nexrad)
    for prod in prods:
        if not os.path.isdir(prod):
            continue
        os.chdir(prod)
        for file in glob.glob("*_*_*"):
            # NOQ_YYYYMMDD_HHMM
            ts = mx.DateTime.strptime(file[4:].replace("_",""),'%Y%m%d%H%M')
            #testfp = ts.strftime("/mnt/mesonet/ARCHIVE/data/%Y/%m/%d/GIS/ridge/"+nexrad+"/"+prod+"/"+nexrad+"_"+prod+"_%Y%m%d%H%M.png")
            #if os.path.isfile(testfp):
            #    continue
            # Run!
            #print 'Missing', nexrad, file
            shutil.copyfile(file, ts.strftime("/mesonet/ridge/input/"+ nexrad +"_%Y%m%d_%H%M_"+prod))
            cnt += 1
        while len(glob.glob("/mesonet/ridge/input/*")) > 10:
            print 'Sleeping!',
            time.sleep(30)
        os.chdir("..")
    os.chdir("..")
    print 'did', cnt
