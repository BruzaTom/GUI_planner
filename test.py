import calendar

diction = {
        'Event': 'probation', 
        'Year': '2025', 
        'Month': '08', 
        'Day': '20', 
        'Dayname': 'Wed', 
        'Time': '09:00pm', 
        'Reo': 'Bi-Weekly', 
        'Code': 'tcpi'
        }

def reocurrance(diction):
    eventDate = int(diction['Year'] + diction['Month'] + diction['Day'] + diction['Time'][0:2] + diction['Time'][3:5])
    if diction['Reo'] == 'Monthly':
        diction['Month'] = str(int(diction['Month']) + 1)#increment month
        if int(diction['Month']) > 12:#if past dec
            diction['Month'] = '01'#reset to jan
            diction['Year'] = str(int(diction['Year']) + 1)#increment year
    if diction['Reo'] == 'Yearly':
        diction['Year'] = str(int(diction['Year']) + 1)#increment year
    #func for incrementdays
    def incrementdays(number_of_days):
        max_day = calendar.monthrange(int(diction['Year']), int(diction['Month']))[1]#find max day date for the month
        calculated_day = int(diction['Day']) + number_of_days#add 14 days to current day
        if calculated_day > max_day:#if the days go past the max date
            diction['Month'] = str(int(diction['Month']) + 1).zfill(2)#increment month
            if int(diction['Month']) > 12:#if past dec
                diction['Year'] = str(int(diction['Year']) + 1)#increment year
                diction['Month'] = '01'#reset to jan
            diction['Day'] = str(calculated_day - max_day).zfill(2)#new day is remainder after the month
        else:
            diction['Day'] = str(calculated_day).zfill(2)#else just adjust the date with incremented days
    #usecases for incrementdays
    if diction['Reo'] == 'Bi-Weekly':
        incrementdays(14)
    if diction['Reo'] == 'Weekly':
        incrementdays(7)
    if diction['Reo'] == 'Daily':
        incrementdays(1)
    return diction

print(diction)

print(reocurrance(diction))
