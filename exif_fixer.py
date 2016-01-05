import time
import sys, os

filepath = os.path.abspath(sys.argv[1])

# magic numbers, need to change this if jpg is jpeg
name = os.path.basename(filepath)[:-4] # strip off extension 
ext = os.path.basename(filepath)[-3:] 
correct_time = time.strptime(name ,"%m-%d-%y_%H%M")

if ext.lower() == "jpg":
    argument = "datetimeoriginal"
elif ext.lower() == "3gp":
    argument = "createdate"
else:
    sys.exit(1)

formatted_time = time.strftime("%Y:%m:%d %H:%M:%S", correct_time)

command = "exiftool '-" + argument + "=" + formatted_time + "' '" + filepath + "'"

print command
os.system(command)