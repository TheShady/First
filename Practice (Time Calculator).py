# a start time in the 12-hour clock format (ending in AM or PM)
# a duration time that indicates the number of hours and minutes
# (optional) a starting day of the week, case-insensitive


start_time = input('Enter starting time(hour:minute AM/PM): ')
duration_time = input('Enter a time to be added(hour:minute): ')
week_day = input('Enter starting day of the week: ').lower()


def add_time(start_time,duration_time,week_day=0):
# saving AM/PM state
    if 'A' in start_time:
        am_pm_check = 1
    elif 'P' in start_time:
        am_pm_check = -1
# getting hours and minutes
    st_time_pm = start_time.split(' ')
    st_hours_mins = st_time_pm[0].split(':')
    dt_hours_mins = duration_time.split(':')
    st_hours = int(st_hours_mins[0])
    st_mins = int(st_hours_mins[1])
    dt_hours = int(dt_hours_mins[0])
    dt_mins = int(dt_hours_mins[1])
    summed_hours = st_hours + dt_hours
    summed_minutes = st_mins + dt_mins
    #print('summed time: ',summed_hours,summed_minutes)
    hours_from_minutes = summed_minutes // 60
    current_minutes = summed_minutes % 60
    current_hours = (summed_hours + hours_from_minutes) % 12
    am_pm_cycles = summed_hours // 12
    days_past = am_pm_cycles // 2
# List with week days
    if week_day != 0:
        week_all = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
        start_day_index = week_all.index(week_day.lower())
        current_week_day = week_all[(start_day_index + days_past) % 7]
    #print('am pm cycles: ',am_pm_cycles)
    if am_pm_cycles % 2 != 0:
        am_pm_check = am_pm_check * -1
    if am_pm_check == 1:
        am_pm = 'AM'
    elif am_pm_check == -1:
        am_pm = 'PM'
    if week_day == 0:
        print(f'Current time: {current_hours}:{current_minutes} {am_pm} ({days_past} days later)'.format(current_hours,current_minutes,am_pm,days_past))
    elif week_day.lower() in week_all:
        print(f'Current time: {current_hours}:{current_minutes} {am_pm} {current_week_day} ({days_past} days later)'.format(current_hours,current_minutes,am_pm,current_week_day,days_past))

add_time(start_time,duration_time,week_day)
