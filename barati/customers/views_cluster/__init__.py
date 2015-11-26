#Importing all the clustered views
import os
modules = []
file_list = os.listdir(os.path.dirname(__file__))
for files in file_list:
   mod_name,file_ext = os.path.splitext(os.path.split(files)[-1])
   if file_ext.lower() == '.py':
      if mod_name != '__init__':
         modules.append(files.split(".")[0])

__all__ = modules
