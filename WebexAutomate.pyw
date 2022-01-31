import webbrowser
import schedule
import os
import sys
import time
directory_path = os.getcwd()

def term():
    quit()

def theoryA():
    webbrowser.open_new_tab("https://guni.webex.com/meet/ICT4A")
    time.sleep(2700)

def theoryB():
    webbrowser.open_new_tab("https://guni.webex.com/meet/ICT4B")
    time.sleep(2700)

def practical():
    url="https://guni.webex.com/meet/ICT4"+str(batch)
    print(url)
    webbrowser.open_new_tab(url)
    time.sleep(2700)

def ibm():
    webbrowser.open_new_tab("https://bit.ly/IBMWAD")
    time.sleep(2700)
    
def french():
    webbrowser.open_new_tab("https://guni.webex.com/meet/ICT-FRENCH")
    time.sleep(2700)

def A41():
    schedule.every().monday.at("08:09:30").do(theoryA)
    schedule.every().monday.at("10:04:30").do(practical)
    schedule.every().monday.at("12:29:30").do(theoryA)
    schedule.every().tuesday.at("08:09:30").do(theoryA)
    schedule.every().tuesday.at("10:04:30").do(theoryA)
    schedule.every().tuesday.at("10:54:30").do(ibm)
    schedule.every().tuesday.at("08:09:30").do(practical)
    schedule.every().wednesday.at("08:09:30").do(practical)
    schedule.every().wednesday.at("10:04:30").do(theoryA)
    schedule.every().wednesday.at("12:29:30").do(theoryA)
    schedule.every().thursday.at("08:09:30").do(ibm)
    schedule.every().thursday.at("08:59:30").do(theoryA)
    schedule.every().thursday.at("10:04:30").do(practical)
    schedule.every().thursday.at("12:29:30").do(practical)
    schedule.every().friday.at("08:09:30").do(practical)
    schedule.every().friday.at("10:04:30").do(ibm)
    schedule.every().friday.at("12:29:30").do(ibm)
    schedule.every().friday.at("13:19:30").do(theoryA)
    schedule.every().saturday.at("09:59:30").do(french)
    schedule.every().day.at("16:00:40").do(term)
    while True:
        schedule.run_pending()

def A42():
    schedule.every().monday.at("08:09:30").do(theoryA)
    schedule.every().monday.at("10:04:30").do(practical)
    schedule.every().monday.at("12:29:30").do(theoryA)
    schedule.every().tuesday.at("08:09:30").do(theoryA)
    schedule.every().tuesday.at("10:04:30").do(theoryA)
    schedule.every().tuesday.at("10:54:30").do(ibm)
    schedule.every().tuesday.at("08:09:30").do(ibm)
    schedule.every().wednesday.at("08:09:30").do(practical)
    schedule.every().wednesday.at("10:04:30").do(theoryA)
    schedule.every().wednesday.at("12:29:30").do(theoryA)
    schedule.every().thursday.at("08:09:30").do(ibm)
    schedule.every().thursday.at("08:59:30").do(theoryA)
    schedule.every().thursday.at("10:04:30").do(ibm)
    schedule.every().thursday.at("12:29:30").do(practical)
    schedule.every().friday.at("08:09:30").do(practical)
    schedule.every().friday.at("10:04:30").do(practical)
    schedule.every().friday.at("12:29:30").do(ibm)
    schedule.every().friday.at("13:19:30").do(theoryA)
    schedule.every().saturday.at("09:59:30").do(french)
    schedule.every().day.at("16:00:40").do(term)
    while True:
        schedule.run_pending()

def A43():
    schedule.every().monday.at("08:09:30").do(theoryA)
    schedule.every().monday.at("10:04:30").do(practical)
    schedule.every().monday.at("12:29:30").do(theoryA)
    schedule.every().tuesday.at("08:09:30").do(theoryA)
    schedule.every().tuesday.at("10:04:30").do(theoryA)
    schedule.every().tuesday.at("10:54:30").do(ibm)
    schedule.every().tuesday.at("08:09:30").do(practical)
    schedule.every().wednesday.at("08:09:30").do(ibm)
    schedule.every().wednesday.at("10:04:30").do(theoryA)
    schedule.every().wednesday.at("12:29:30").do(theoryA)
    schedule.every().thursday.at("08:09:30").do(ibm)
    schedule.every().thursday.at("08:59:30").do(theoryA)
    schedule.every().thursday.at("10:04:30").do(practical)
    schedule.every().thursday.at("12:29:30").do(practical)
    schedule.every().friday.at("08:09:30").do(practical)
    schedule.every().friday.at("10:04:30").do(practical)
    schedule.every().friday.at("12:29:30").do(ibm)
    schedule.every().friday.at("13:19:30").do(theoryA)
    schedule.every().saturday.at("09:59:30").do(french)
    schedule.every().day.at("16:00:40").do(term)
    while True:
        schedule.run_pending()

def B44():
    schedule.every().monday.at("08:09:30").do(practical)
    schedule.every().monday.at("10:04:30").do(theoryB)
    schedule.every().monday.at("12:29:30").do(practical)
    schedule.every().tuesday.at("08:09:30").do(ibm)
    schedule.every().tuesday.at("08:59:30").do(theoryB)
    schedule.every().tuesday.at("10:04:30").do(practical)
    schedule.every().tuesday.at("12:29:30").do(theoryB)
    schedule.every().wednesday.at("08:09:30").do(theoryB)
    schedule.every().wednesday.at("10:04:30").do(practical)
    schedule.every().wednesday.at("12:29:30").do(practical)
    schedule.every().thursday.at("08:09:30").do(theoryB)
    schedule.every().thursday.at("08:59:30").do(ibm)
    schedule.every().thursday.at("10:04:30").do(theoryB)
    schedule.every().thursday.at("12:29:30").do(ibm)
    schedule.every().friday.at("08:09:30").do(ibm)
    schedule.every().friday.at("08:59:30").do(theoryB)
    schedule.every().friday.at("10:04:30").do(practical)
    schedule.every().friday.at("12:29:30").do(theoryB)
    schedule.every().saturday.at("09:59:30").do(french)
    schedule.every().day.at("16:00:40").do(term)
    while True:
        schedule.run_pending()

def B45():
    schedule.every().monday.at("08:09:30").do(ibm)
    schedule.every().monday.at("10:04:30").do(theoryB)
    schedule.every().monday.at("12:29:30").do(practical)
    schedule.every().tuesday.at("08:09:30").do(ibm)
    schedule.every().tuesday.at("08:59:30").do(theoryB)
    schedule.every().tuesday.at("10:04:30").do(practical)
    schedule.every().tuesday.at("12:29:30").do(theoryB)
    schedule.every().wednesday.at("08:09:30").do(theoryB)
    schedule.every().wednesday.at("10:04:30").do(ibm)
    schedule.every().wednesday.at("12:29:30").do(practical)
    schedule.every().thursday.at("08:09:30").do(theoryB)
    schedule.every().thursday.at("08:59:30").do(ibm)
    schedule.every().thursday.at("10:04:30").do(theoryB)
    schedule.every().thursday.at("12:29:30").do(practical)
    schedule.every().friday.at("08:09:30").do(ibm)
    schedule.every().friday.at("08:59:30").do(theoryB)
    schedule.every().friday.at("10:04:30").do(practical)
    schedule.every().friday.at("12:29:30").do(theoryB)
    schedule.every().saturday.at("09:59:30").do(french)
    schedule.every().day.at("16:00:40").do(term)
    while True:
        schedule.run_pending()

def B46():
    schedule.every().monday.at("08:09:30").do(practical)
    schedule.every().monday.at("10:04:30").do(theoryB)
    schedule.every().monday.at("12:29:30").do(practical)
    schedule.every().tuesday.at("08:09:30").do(ibm)
    schedule.every().tuesday.at("08:59:30").do(theoryB)
    schedule.every().tuesday.at("10:04:30").do(practical)
    schedule.every().tuesday.at("12:29:30").do(theoryB)
    schedule.every().wednesday.at("08:09:30").do(theoryB)
    schedule.every().wednesday.at("10:04:30").do(practical)
    schedule.every().wednesday.at("12:29:30").do(ibm)
    schedule.every().thursday.at("08:09:30").do(theoryB)
    schedule.every().thursday.at("08:59:30").do(ibm)
    schedule.every().thursday.at("10:04:30").do(theoryB)
    schedule.every().thursday.at("12:29:30").do(practical)
    schedule.every().friday.at("08:09:30").do(ibm)
    schedule.every().friday.at("08:59:30").do(theoryB)
    schedule.every().friday.at("10:04:30").do(practical)
    schedule.every().friday.at("12:29:30").do(theoryB)
    schedule.every().saturday.at("09:59:30").do(french)
    schedule.every().day.at("16:00:00").do(term)
    while True:
        schedule.run_pending()


def B(batch):
    if batch==4:
        B44()
    elif batch==5:
        B45()
    elif batch==6:
        B46()

def A(batch):
    if batch==1:
        A41()
    elif batch==2:
        A42()
    elif batch==3:
        A43()



with open(os.path.join(sys.path[0], "config.txt"), "r") as f:
    #for lines in f:
    line1=f.readline()
    line2=f.readline()
    
line1=line1.strip()
clss=line1[-1]
print(clss)
line2=line2.strip()
batch=int(line2[-1])
print(batch)
if clss=="B":
    if batch==4 or batch==5 or batch==6:
        B(batch)
elif clss=="A":
    if batch==1 or batch==2 or batch==3:
        A(batch)
else: 
    print("Error in Config File")
