"""
TASK: 04 Temp Stats Csv

# Skills CSV read, simple maths
Go to this site https://www.metoffice.gov.uk/hadobs/hadcet/data/download.html and download the txt file
Daily Mean Temperature.
This file has dates and daily temperatures:
- Read all of the values
- Find the highest, lowest and average
- Print those three values
Extend - See how you can potentially use the dates to chart daily temp changes by years, by months
by day comparisons over time. Maybe chart them using mathplotlib or another library. Just see what you can do with it

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def readValues():
    with open("meantemp_daily_totals.txt", "r") as file:
        min = 1000
        max = -1000
        rep = sum(1 for line in file)
        file.seek(2)
        line = "None"
        avg = 0
        for i in range(2,rep-1):
            l = file.readline()
            l = l.strip("\n")
            l = l.split()
            try:
                l[1] = float(l[1])
                if min > l[1]:
                    min = l[1]
                if max < l[1]:
                    max = l[1]
                avg += l[1]
            except:
                pass
        print(min)
        print(max)
        print(avg/rep)

if __name__ == "__main__":
    readValues()
