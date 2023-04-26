import time
import datetime
import csv

# opening text file in read only mode
file = open("./AutomationQA_Summary.csv", "r")

search_word_count = 'Passed'
start_time = datetime.datetime.now()
# reading data of the file
read_data = file.read()
per_word = read_data.split()

total =len(per_word)
print(total)
print(per_word)

num_rows = 0

for row in open("./AutomationQA_Summary.csv"):
    num_rows += 1


# converting data in lower case and the counting the occurrence 
word_count = read_data.count(search_word_count)

reader = csv.reader(file)
linecount= len(list(reader))


# printing word and it's count
print(f"The word '{search_word_count}' appeared {word_count} times.")
linecount=num_rows
percentageresult = (word_count/linecount)*100

print(f"'{percentageresult}' %" )

if percentageresult<85:
    print("The test has failed")

else:
    print('We have the Go Ahead with P2 Tests')

end_time = datetime.datetime.now()
print(start_time)
print(end_time)

timediff = end_time - start_time

print(timediff)

print(f"Total time taken to execute the script is {timediff.total_seconds()} seconds")
inMinutes = timediff/60
print(inMinutes)

ms = timediff.total_seconds() * 1000
print(f"Total time taken to execute the script is {ms} milliseconds")

lines = [f"The word '{search_word_count}' appeared {word_count} times.", f" Percentage pass-rate'{percentageresult}' %" , f"Total time taken to execute the script is {timediff.total_seconds()} seconds", f"Total time taken to execute the script is {ms} milliseconds" ]
contentEmail= lines

with open('emailContent.txt', 'w') as f:
    for line in contentEmail:
        f.write(line)
        f.write('\n')










