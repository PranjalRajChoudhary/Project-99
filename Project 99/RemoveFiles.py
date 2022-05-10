import os
import shutil
import time

path = input("Enter the directory to be backuped")
days = int(input("Enter the number of days"))
seconds = time.time() - (days * 24 * 60 * 60)
print(seconds)

if(os.path.exists(path)):
  for roots,dirs,files in os.walk(path):
     for name in files:
          path_of_file = os.path.join(path,name)
          ctime = os.stat(path_of_file).st_ctime
          print(ctime)
          if(seconds >= ctime):
               os.remove(path_of_file)
     
     for name in dirs:
          path_of_dir = os.path.join(path,name)
          ctime = os.stat(path_of_dir).st_ctime
          if(seconds >= ctime):
               shutil.rmtree(path_of_dir)
