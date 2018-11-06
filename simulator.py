import random, time, csv

inputCSV = input('What is the name of the CSV baseline you would like to use?  ')
outputCSV = input('What is the name of the CSV output? ')
jvar = int(input("What is the judge variance from 'correct' you would like to see? "))


if not outputCSV.endswith('.csv'):
  outputCSV = outputCSV + '.csv'

if not inputCSV.endswith('.csv'):
  inputCSV = inputCSV + '.csv'

resultsFile = open(outputCSV, 'w', newline = '')
outputWrite = csv.writer(resultsFile)
outputWrite.writerow(['Name', 'Rounds Judged','Minority Decisions', 'Majority Decisions', 'Unaminously Right Decisions', 'Unaminously wrong decisions', 
  'right 2-1 Decisons', 'wrong 2-1 decisions', 'Right Ballot', 'Wrong Ballot' ])



inputFile = open(inputCSV)
inputReader = csv.reader(inputFile)



def judgeCalculator():
  global jvar
  for row in inputReader:
    unam_right = 0
    unam_wrong = 0
    split_right = 0
    split_wrong = 0
    majCount = 0
    minCount = 0
    rightDec = 0
    wrongDec = 0
    runCount = 0
    name = row[0]
    roundGoal = row[1]

    if runCount < roundGoal:
      runCount += 1
      judge1 = random.randint(1,100)
      judge2 = random.randint(1,100)
      judge3 = random.randint(1,100)
      panelDec = 0
      panel = [judge1, judge2, judge3]
      if judge1 <= jvar:
        wrongDec += 1
      else:
        rightDec += 1
      for int in panel:
        if int <= jvar:
          panelDec += 2
        elif int > jvar:
          panelDec += 1
      if panelDec == 6:
        unam_wrong += 1
        majCount += 1
      elif ((panelDec == 5) and (judge1 <= jvar)):
        majCount += 1
        split_wrong += 1
      elif ((panelDec == 5) and (judge1 > jvar)):
        minCount += 1
        split_wrong += 1
      elif ((panelDec == 4) and (judge1 <= jvar)):
        split_right += 1
        minCount += 1
      elif ((panelDec == 4) and (judge1 > jvar)):
        majCount += 1
        split_right += 1
      elif panelDec == 3:
        unam_right += 1
        majCount += 1

    else:
      outputWrite.writerow[name,str(runCount),str(minCount),str(majCount),str(unam_right),str(unam_wrong),str(split_right),str(split_wrong),str(rightDec),str(wrongDec)]
      continue



judgeCalculator()

outputWrite.close()