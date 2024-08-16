import tkinter as tk# first, import the library
import calendar
import datetime
import random
import string
import ast

root = tk.Tk() # create a window
root.title("Planner")
root.geometry("900x925") # set the window size
root.configure(bg="#333333")
entry = tk.Entry(root)

class App:
    def __init__(self):
        self.results = []
        self.newLst = []
        self.foundDict = {}
        self.count = 0
        self.count2 = 0
        self.func = None
        self.code = None
        self.dataLst = events(file)
        self.weekEvents = inWeek(self.dataLst, date)
        self.file = file
        self.now = now
        self.days = days
        self.today = today
        self.thisTime = time
        self.date = date
        self.thisDay = day
        self.daysLeft = daysLeft
        self.schedual = '\n*New Event Manager*'

    def errMessage(self):
        self.count = 0
        forget_all(root)
        makeLable('\n\n\n-Error0: Incorrect Format\n')
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Try Again', self.newEvent, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def errMessage1(self):
        self.count = 0
        forget_all(root)
        makeLable('\n\n\n-Error0: Input Error\n')
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Try Again', self.newEvent, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def ohno(self):
        forget_all(root)
        makeLable('\n\n\n-Exception raised:\nThe Date You Entered Dosent Exist.\n')
        makeButton('Try Again', self.newEvent, "#B0C4DE", "#444444")
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")

    def submitNew(self):
        newLst = []
        eventDict = {}
        try:
            if self.code == None:
                self.code = randomStr(4)
            if (len(self.results) == 6):
                usrData = Answers(self.results[0], self.results[1], self.results[2], self.results[3], self.results[4], self.results[5])
                if usrData.check() == True:
                    eventDict = makeDict(self.results[0], self.results[1], self.results[2], self.results[3], self.results[4], self.results[5], self.code)
                    newLst.append(eventDict)
                    for item in self.dataLst:
                        if self.code != item['Code']:
                            newLst.append(item)
                    updateData(newLst, self.file)
                else:
                    self.errMessage()
            else:
                self.errMessage1()
            self.btm()
        except Exception as _:
            self.ohno()

    def handleui(self, value, string):
        makeLable(string)
        value = newEntry()
        value.pack()
        self.makeBind(value)

    def dataStr2(self, subject, dictLst):
        tempLst = sort_dates(dictLst)
        string = ''
        if tempLst == []:
            makeLable(f'No Events {subject}..')
            return ''
        else:
            makeLable(f'Events {subject}!\n')
            for data in tempLst:
                string += f"{data['Event']} on {data['Dayname']} {data['Month']}-{data['Day']}-{data['Year']} at {data['Time']}. ID#{data['Code']}\n" 
        return string

    def debuger(self, value):
        print(f'DEBUGGER::{value}::')

    def handle_entry(self, event):
        self.readyButton()
        self.results.append(event.widget.get())
        event.widget.tk_focusNext().focus()

    def makeBind(self, entry):
        return entry.bind("<Return>", self.handle_entry)

    def btm(self):
        forget_all(root)
        main()
    
    def readyButton(self):
        self.count += 1
        if self.count == self.count2:
            makeButton('Submit', self.func, "#B0C4DE", "#444444")

    def newDict(self):
        pass

    def newEvent(self):
        self.count = 0
        self.count2 = 6
        self.results = []
        self.func = self.submitNew
        forget_all(root)
        event,year ,month ,day , time, apm = 0, 0, 0, 0, 0, 0
        makeLable('\n*New Event Manager*')
        self.handleui(event, '\nWhat Event?')
        self.handleui(year, '\nWhat Year?\nxxxx')
        self.handleui(month, '\nWhat Month\nxx')
        self.handleui(day, '\nWhat Day?\nxx')
        self.handleui(time, '\nWhat Time?\nxxxx')
        self.handleui(apm, '\nam or pm?')
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def errorMessage3(self):
        self.count = 0
        forget_all(root)
        makeLable(f'\n\n\n-Error3: {self.results[0]} Not In Data..\n\n')
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Try Again', self.editData, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def changeData(self):
        event,year ,month ,day , time, apm = 0, 0, 0, 0, 0, 0
        self.count = 0
        self.count2 = 6
        self.func = self.submitNew
        if self.results[0] not in map(lambda d: d.get('Code'), self.dataLst):
            self.errorMessage3()
        forget_all(root)
        self.code = self.results[0]
        self.results = []
        makeLable('\n*Edit Event Manager*')
        self.handleui(event, '\nWhat Event?')
        self.handleui(year, '\nWhat Year?\nxxxx')
        self.handleui(month, '\nWhat Month\nxx')
        self.handleui(day, '\nWhat Day?\nxx')
        self.handleui(time, '\nWhat Time?\nxxxx')
        self.handleui(apm, '\nam or pm?') 
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()


    def editData(self):
        self.count = 0
        self.count2 = 1
        self.results = []
        self.func = self.changeData
        code = ''
        forget_all(root)
        makeLable('\n*Enter In Event Manager*\n\n')
        self.dataBox2('Stored', self.dataLst)
        self.handleui(code, '\nEnter ID#')
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")

    def errorMessage4(self):
        self.count = 0
        forget_all(root)
        makeLable(f'\n\n\n-Error4: {self.results[0]} Not In Data..\n\n')
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Try Again', self.unschedual, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def removeData(self):
        self.code = self.results[0]
        newLst = []
        if self.code not in map(lambda d: d.get('Code'), self.dataLst):
            self.errorMessage4()
        self.dataBox2('Stored', self.dataLst)
        for diction in self.dataLst:
            if diction['Code'] != self.code:
                newLst.append(diction)
            else:
                self.foundDict = diction
        self.areYouShure()

    def areYouShure(self):
        forget_all(root)
        event = self.foundDict['Event']
        dayname = self.foundDict['Dayname']
        year = self.foundDict['Year']
        month = self.foundDict['Month']
        day = self.foundDict['Day']
        time = self.foundDict['Time']
        self.code = self.foundDict['Code']
        makeLable('\n*Delete Event Manager*\n\n')
        makeLable(f"\nAre You Sure You Want To Delete This?")
        makeLable(f"\n{event} on {dayname} {month}-{day}-{year} at {time}\n")
        makeButton('Yes', self.removeCode, "#B0C4DE", "#444444")
        makeButton('No - Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Try Again', self.unschedual, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def removeCode(self):
        newLst = []
        for item in self.dataLst:
            if self.code != item['Code']:
                newLst.append(item)
            updateData(newLst, self.file)
        self.btm() 

    def unschedual(self):
        self.count = 0
        self.count2 = 1
        self.results = []
        self.func = self.removeData
        code = ''
        forget_all(root)
        makeLable('\n*Delete Event Manager*\n\n')
        self.dataBox2('Stored', self.dataLst)
        self.handleui(code, '\nEnter ID#')
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def dataBox2(self, subject, dictLst):
        return tk.Label(root, text=self.dataStr2(subject, dictLst), bg="#222222", fg="#B0C4DE", font=("Arial", 16, "bold"), padx=10, pady=5).pack()

    def checkSchedual(self):
        forget_all(root)
        makeLable('\n\n\n\n')
        self.dataBox2('Scheduled', self.dataLst)
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def checkWeek(self):
        forget_all(root)
        makeLable('\n\n\n\n')
        self.dataBox2('This Week', inWeek(self.dataLst, date))
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def checkTomorrow(self):
        forget_all(root)
        makeLable('\n\n\n\n')
        self.dataBox2('Tomorrow', inTomorrow(self.dataLst, date))
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def checkToday(self):
        forget_all(root)
        makeLable('\n\n\n\n')
        self.dataBox2('Today', inToday(self.dataLst, date))
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        makeButton('Options', self.options, "#B0C4DE", "#444444")
        root.mainloop()

    def options(self):
        forget_all(root)
        tk.Label(root, text=initMessage(now, date, daysLeft), fg="#B0C4DE", bg="#333333", font=("Arial", 18, "bold")).pack()
        tk.Label(root, text=miniCal(now), font="TkFixedFont", justify=tk.LEFT, fg="#B0C4DE", bg="#333333").pack()
        makeButton('Schedule', self.newEvent, "#B0C4DE", "#444444")
        makeButton('Edit', self.editData, "#B0C4DE", "#444444")
        makeButton('Remove', self.unschedual, "#B0C4DE", "#444444")
        makeButton('Home', self.btm, "#B0C4DE", "#444444")
        root.mainloop()



class Answers:
    def __init__(self, event, year, month, day, time, apm):
        self.event = str(event),
        self.year = str(year),
        self.month = str(month),
        self.day = str(day),
        self.time = str(time),
        self.apm = str(apm)

    def printAnswers(self):
        return print(str(self.event[0]) + str(self.year[0]) + str(self.month[0]) + str(self.day[0]) + str(self.time[0]) + str(self.apm))

    def check(self):
        check1 = (len(self.year[0]) == 4) & (all(map(lambda c: c.isdigit(), str(self.year[0]))))
        #print(str(self.year[0]))
        check2 = (len(self.month[0]) == 2) & (all(map(lambda c: c.isdigit(), str(self.month[0])))) & (int(self.month[0]) <= 12)
        check3 = (len(self.day[0]) == 2) & (all(map(lambda c: c.isdigit(), str(self.day[0]))))
        check4 = (len(self.time[0]) == 4) & (all(map(lambda c: c.isdigit(), str(self.time[0]))))
        check5 = (self.apm == 'am') | (self.apm == 'pm')
        #self.printAnswers()
        if (check1 == True) & (check2 == True) & (check3 == True) & (check4 == True) & (check5 == True):
            return True
        return False

def main():
    user = App()
    updateData(removeOld(events(file), date, time), file)
    #print initmessage
    tk.Label(root, text=initMessage(now, date, daysLeft), fg="#B0C4DE", bg="#333333", font=("Arial", 18, "bold")).pack()
    #pint calendar
    tk.Label(root, text=miniCal(now), font="TkFixedFont", justify=tk.LEFT, fg="#B0C4DE", bg="#333333").pack()
    makeButton('Today\n'+str(len(inToday(events(file), date))), user.checkToday, "#444444", "#B0C4DE")
    makeButton('Tomorrow\n'+str(len(inTomorrow(events(file), date))), user.checkTomorrow, "#444444", "#B0C4DE")
    makeButton('This Week\n'+str(len(inWeek(events(file), date))), user.checkWeek, "#444444", "#B0C4DE")
    makeButton('All Data\n'+str(len(events(file))), user.checkSchedual, "#444444", "#B0C4DE")
    makeButton('Options', user.options, "#B0C4DE", "#444444")
    tk.Label(root, text='\n\n\nDeveloped By Thomas Gomez @https://github.com/BruzaTom', fg="#B0C4DE", bg="#333333", font=("Arial", 10, "bold")).pack()
    root.mainloop()
#tkinter functions
def forget_all(parent):
    for widget in parent.winfo_children():
        widget.forget()
#End tkinter

def dataBox(subject, dictLst):
    return tk.Label(root, text=dataStr(subject, dictLst), bg="#222222", fg="#B0C4DE", font=("Arial", 12, "bold"), padx=10, pady=5).pack() 

def makeButton(name, func, lc, bgc):
    return tk.Button(
        root,
        text=name,
        command=func,
        fg=lc, bg=bgc,
        height=3, width=8,
        font=("Arial", 12, "bold")
        ).pack()

def sort_dates(dictLst):
    tempLst = dictLst.copy()
    return sorted(sorted(sorted(sorted(sorted(tempLst,
        key=lambda n: n['Time'][5]),
        key=lambda t: t['Time']),
        key=lambda d: d['Day']),
        key=lambda m: m['Month']),
        key=lambda y: y['Year']) 

def inTomorrow(dictLst, date):
    tempLst = []
    thisYear = date[0:4]#date
    thisMonth = date[5:7]
    thisDay = date[8:10]
    numThisDay = int(thisDay)
    for diction in dictLst:
        if (diction['Year'] == thisYear) & (diction['Month'] == thisMonth) & (numThisDay + 1 == int(diction['Day'])):
            tempLst.append(diction)
    return tempLst

def inToday(dictLst, date):
    tempLst = []
    thisYear = date[0:4]#date
    thisMonth = date[5:7]
    thisDay = date[8:10]
    for diction in dictLst:
        if (diction['Year'] == thisYear) & (diction['Month'] == thisMonth) & (thisDay == diction['Day']):
            tempLst.append(diction)
    return tempLst

def timeOnly(today):
    time = today[11:13] + today[14:16]
    return time

def removeOld(dictLst, date, time):
    tempLst = []
    todayDate = int(date[0:4] + date[5:7] + date[8:10] + time)
    for diction in dictLst:
        eventDate = int(diction['Year'] + diction['Month'] + diction['Day'] + diction['Time'][0:2] + diction['Time'][3:5])
        if (int(diction['Time'][0:2]) < 12) & (diction['Time'][5] == 'p'):#if for example 01:30pm
            milTime = int(diction['Time'][0:2]) + 12 
            eventDate = int(diction['Year'] + diction['Month'] + diction['Day'] + str(milTime) + diction['Time'][3:5])
        if (int(diction['Time'][0:2]) == 12) & (diction['Time'][5] == 'a'):#if for example 12:30am
            eventDate = int(diction['Year'] + diction['Month'] + diction['Day'] + "00" + diction['Time'][3:5])
        if todayDate <= eventDate:
            tempLst.append(diction)
    return tempLst

def getDaysLeft(days, day):
    return days - int(day)

def dateOnly(today):
    date = ""
    for i in range(0, 10):
        date += today[i]
    return date

def getDay(date):
    day = ""
    for i in range(0, len(date)):
        if i >= 8:
            day += date[i]
    return day

def miniCal(now):
    return calendar.TextCalendar().formatmonth(now.year, now.month, w=5, l=2)# prints calender

def getDays(now):
    return calendar.monthrange(now.year, now.month)[1]#representing [0][1], 0 is lowest in range and 1 is highest

def initMessage(now, date, daysLeft):
    year = date[:4]
    month = date[5:7]
    day = date[8:]
    string = ''
    string += "\nGreetings from the PLANNER!\n" 
    string += f"\nTodays date is: {month}-{day}-{year}\n"
    string += f"There are {daysLeft} days left in this month.\n"
    return string

def inWeek(dictLst, date):
    thisWeek = []
    thisYear = date[0:4]#date
    thisMonth = date[5:7]
    thisDay = date[8:10]
    numThisDay = int(thisDay)
    for diction in dictLst:
        if (diction['Year'] == thisYear) & (diction['Month'] == thisMonth) & (numThisDay + 7 >= int(diction['Day'])):
            if (diction not in inToday(dictLst, date)) & (diction not in inTomorrow(dictLst, date)):
                thisWeek.append(diction)
    return thisWeek

def randomStr(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for _ in range(length))

def events(file):
    dictLst = []
    with open(file) as f: 
        data = f.read()
    dictLst = ast.literal_eval(data)
    return dictLst

def makeDict(event, year, month, day, time, apm, code):
    newDict = {}
    newDict.update({
        'Event': event,
        'Year': year,
        'Month': month,
        'Day': day,
        'Dayname': calendar.day_abbr[datetime.date(int(year), int(month), int(day)).weekday()],
        'Time': time[:2]+':'+time[2:]+apm,
        'Code': code
        })
    return newDict

def updateData(dictLst, file):
    with open(file, "w") as f:
        f.write(str(dictLst))

def dataStr(subject, dictLst):
    tempLst = sort_dates(dictLst)
    string = ''
    if tempLst == []:
        string = f'No Events {subject}..\n'
    else:
        newLbl = tk.Label(root, text=f'Events {subject}!', fg="#B0C4DE", bg="#333333", font=("Arial", 12, "bold")).pack()
        for data in tempLst:
            string += f"{data['Event']} on {data['Dayname']} {data['Month']}-{data['Day']}-{data['Year']} at {data['Time']}\n" 
    return string

def makeLable(string):
    return tk.Label(root, text=string, fg="#B0C4DE", bg="#333333", font=("Arial", 16, "bold")).pack()

def newEntry():
    return tk.Entry(root, width=15, bg="#E3E3E3", borderwidth=5)

#globals
file = "plannerData.txt"
now = datetime.datetime.now()
days = getDays(now)
today = str(datetime.datetime.today())
time = timeOnly(today)
date = dateOnly(today)
day = getDay(date)
daysLeft = getDaysLeft(days, day)
dataLst = events(file)

main()