import datetime
import sys

dt = sys.argv[1:]

monday = "Monday's child is fair of face"
tuesday = "Tuesday's child is full of grace"
wednesday = "Wednesday's child is full of woe"
thursday = "Thursday's child has far to go"
friday = "Friday's child is loving and giving"
saturday = "Saturday's child works hard for a living"
sunday = "Sunday's child is fair and wise and good in every way"

day, month, year = (int(x) for x in dt)    
ans = datetime.date(year, month, day)

if ans.strftime("%A") == 'Monday':
	print ('You were born on a', ans.strftime("%A"),'and', monday+'.')
elif ans.strftime("%A") == 'Tuesday':
	print ('You were born on a', ans.strftime("%A"),'and', tuesday+'.')
elif ans.strftime("%A") == 'wednesday':
	print ('You were born on a', ans.strftime("%A"),'and', wednesday+'.')
elif ans.strftime("%A") == 'Thursday':
	print ('You were born on a', ans.strftime("%A"),'and', thursday+'.')
elif ans.strftime("%A") == 'Friday':
	print ('You were born on a', ans.strftime("%A"),'and', friday+'.')
elif ans.strftime("%A") == 'Sunday':
	print ('You were born on a', ans.strftime("%A"),'and', sunday+'.')
elif ans.strftime("%A") == 'Saturday':
	print ('You were born on a', ans.strftime("%A"),'and', saturday+'.')






