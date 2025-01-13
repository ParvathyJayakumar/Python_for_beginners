#Categorize a given time of the day into NIGHT, MORNING, AFTERNOON, or EVENING.
T = int(input("Enter the time in hours (0-23): "))
if 0 <= T <= 5:
    print("NIGHT")
elif 6 <= T <= 11:
    print("MORNING")
elif 12 <= T <= 17:
    print("AFTERNOON")
elif 18 <= T <= 23:
    print("EVENING")
else:
    print("INVALID")
