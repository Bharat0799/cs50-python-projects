months = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
]

while True:
    try:
        date = input("Date: ")

        if "/" in date:
            m, d, y = date.split("/")
            m = int(m)
            d = int(d)
            y = int(y)

        else:
            parts = date.split()

            if len(parts) != 3:
                continue

            month = parts[0]

            if month not in months:
                continue

            m = months.index(month) + 1
            d = int(parts[1].replace(",", ""))
            y = int(parts[2])

        if 1 <= m <= 12 and 1 <= d <= 31:
            print(f"{y}-{m:02}-{d:02}")
            break

    except:
        pass