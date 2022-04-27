import os
from os import path
import shutil

src = "/modules/Naver_Movie\\"
dst = "/core/db/csv_files\\"

files = os.listdir(src)
#regexCtask = "CTASK"
print(files)
#regex =re.compile(r'(?<=CTASK:)')


files = [i for i in os.listdir(src) if i.endswith(".csv") and path.isfile(path.join(src, i))]
for f in files:
    shutil.copy(path.join(src, f), dst)