import sys
import os
import shutil

def newCourse(cName):
    calendarFile = "calendar.xlsx"
    os.makedirs(cName)
    shutil.copy(calendarFile, cName)
    os.rename(cName + "\\" + calendarFile, cName +"\\" + cName + " "+ calendarFile)
    print("Copied, Renamed and Ready!")



if len(sys.argv) > 1:
    print(sys.argv)
    newCourseName = sys.argv[1]
    newCourse(newCourseName)
