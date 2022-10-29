import csv
import time
import random
import datetime as dt



# create a bunch random data into a csv file
def create_data():
    t = random.randint(10000, 100000)
    x = dt.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    x = x + str(t)
    with open(f'sheets/data{x}.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['id', 'name', 'age'])
       
        
        for i in range(1000):
            for j in range(10000):
                writer.writerow([j, 'name' + str(j), j])
        






#make csv files
while True:
    create_data()
    time.sleep(1)
    