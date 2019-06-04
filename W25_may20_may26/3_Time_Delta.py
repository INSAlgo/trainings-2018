from datetime import datetime
n = int(input())
for i in range(n):
    da = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    db = datetime.strptime(input(), "%a %d %b %Y %H:%M:%S %z")
    print(abs(int((da - db).total_seconds())))
