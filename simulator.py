import random, time, csv

inputCSV = input('What is the name of the CSV baseline you would like to use?  ')
outputCSV = input('What is the name of the CSV output? ')

if not outputCSV.endswith('.csv'):
  outputCSV = outputCSV + '.csv'


resultsFile = open(outputCSV, 'w', newline = '')

#pull from CSV

#run set rounds for judges

#export data