from stat import ST_CTIME
from datetime import date
import os


def time_check(files, folder):
	os.chdir(folder)
	time = 0
	newest = ""
	for file in files:
		tmp = os.stat(file)
		if (tmp.st_ctime > time):
			time = tmp.st_ctime
			newest = file
	return newest


# check if there is a folder with actual month(if not create one)
def new_folder():
	dates = date.today()
	today = dates.strftime("%m.%Y")
	if today not in os.listdir():
		try:
			os.makedirs(today)
		except:
			pass
