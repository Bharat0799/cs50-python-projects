def convert(time):
    hours, minutes = time.split(":")
    return int(hours) + int(minutes) / 60

time = input("What time is it? ")
t = convert(time)

if 7 <= t <= 8:
    print("breakfast time")
elif 12 <= t <= 13:
    print("lunch time")
elif 18 <= t <= 19:
    print("dinner time")