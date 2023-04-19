import pandas as pd
import csv
import re
import time
import psutil

# starting time for performance calculation
startTime = time.time()

# Reading the find_words.txt file and frequency
frequency = {}
shakespeare_text = open("t8.shakespeare.txt", "r")
text_string = shakespeare_text.read().lower()
pattern = re.findall(r'\b[a-z]{1,15}\b', text_string)


# Reading the find_words.txt file
wordsInText = open("find_words.txt", "r")
wordsFound = wordsInText.read()
wordsInText.close()
wordsFound_inlist = wordsFound.split()


# Reading the dictionary.csv file
with open('french_dictionary.csv', mode='r') as data:
    reader = csv.reader(data)
    dictCsv = {rows[0]: rows[1] for rows in reader}

# creating list for all english words in find_words.txt file
tot_eng_word = []

for word in pattern:
    if word in wordsFound_inlist:
        tot_eng_word.append(word)

engWord = list(set(tot_eng_word))


count_tot_eng_word = []
for i in engWord:
    count_tot_eng_word.append(tot_eng_word.count(i))

# creating list for all french words in find_word file
frenchWord = []
for x in engWord:
    for key, value in dictCsv.items():
        if x in key:
            frenchWord.append(value)

final = list(zip(engWord, frenchWord, count_tot_eng_word))

# creating the table form of output
header = ['English Word', 'French Word', 'Frequency']
with open('Frequency.csv', 'w') as f:
    # Create a CSV writer object that will write to the file 'f'
    csv_writer = csv.writer(f)

    # Write the field names (column headers) to the first row of the CSV file
    csv_writer.writerow(header)

    # Write all of the rows of data to the CSV file
    csv_writer.writerows(final)

# creating performance.txt
timeTook = time.time() - startTime
memoryUsed = psutil.cpu_percent(timeTook)
f = open("performance.txt", "w")
f.write(f'Time to process: 0 minutes {timeTook} seconds\nMemory used: {memoryUsed} MB')
f.close()

#  converting csv file to xlsx
# df_new = pd.read_csv('frequency.csv')

# saving xlsx file
# GFG = pd.ExcelWriter('frequency.xlsx')
# df_new.to_excel(GFG, index=False)
#
# GFG.save()


