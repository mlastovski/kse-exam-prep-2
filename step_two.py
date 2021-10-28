day_input = input('Enter a date in format [DAY of MONTH]: ')
step_input = input('Enter step in format [X days]: ')

entered_day = day_input.split(' ')[0]
entered_day = int(entered_day)
entered_month = day_input.split(' ')[2]
day_step_input = step_input.split(' ')[0]
day_step_input = int(day_step_input)

max_days = 30

months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']

count = 0

while day_step_input >= max_days:
    day_step_input -=max_days
    count += 1

count += months.index(entered_month)
while count > 11:
    count -= 12
    
print(str(entered_day + day_step_input) + ' of ' + months[count])
