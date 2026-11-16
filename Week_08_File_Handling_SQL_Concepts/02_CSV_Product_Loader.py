"""
TASK: 02 Csv Product Loader

# Create a CSV file via Excel which contains a list of random objects and prices
Load products from a CSV into objects and print:
- highest price
- average price
- most common category

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import csv
import statistics

def csvRead(filename):
    data = []
    with open(filename, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    return(data)

def analyseData(data):
    highest = -1
    highestIndex = -1
    total = 0
    categories = []
    for i in range(len(data)):
        if float(data[i][2]) > highest:
            highest = float(data[i][2])
            highestIndex = i
        total += float(data[i][2])
        categories.append(data[i][1])
    mostCommon = statistics.mode(categories)
    return(
    highest,
    data[highestIndex][0],
    round(total/len(data)*100)/100,
    mostCommon
    )



if __name__ == "__main__":
    highest, category, mean, mostCommon = analyseData(csvRead("week8_02_products.csv"))
    print("Highest priced product: " + category + " - " + str(highest))
    print("Average price: " + str(mean))
    print("Most common category: " + mostCommon)
