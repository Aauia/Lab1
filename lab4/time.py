from datetime import datetime, timedelta

#ex 1
n = datetime.now()
mi= n - timedelta(days=5)

print("Current Date:", n)
print("Five Days Ago:", mi)

#ex 2
ti = datetime.now()
a = ti - timedelta(days=1)
tim = ti + timedelta(days=1)

print("Yesterday:", a)
print("Today:", ti)
print("Tomorrow:", tim)

#ex 3
a = datetime.now()
b = a.replace(microsecond=0)

print("Datetime without Microseconds:", b)

#ex 4
a1 = datetime(2024, 2, 10, 12, 0, 0)
a2 = datetime(2024, 2, 15, 18, 30, 0)

a3 = (a2 - a1).total_seconds()

print(f"Difference between {a1} and {a2} in seconds: {a3} seconds")
