import sys
import os 

from blogger import convert
file_path = "/storage/emulated/0/blog_texts/pykancha/jupyter_files/"
os.chdir(file_path)
for f in os.listdir():
	try:
		file_list = f.split(".")
		if "ipynb" in file_list:
			convert(f)
	except:
		continue;
			
