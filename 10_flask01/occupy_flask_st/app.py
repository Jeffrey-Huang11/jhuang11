# Team Tiny Elephant (Jeffrey Huang, Erin Lee, Jonathan Lee)
# SoftDev
# K10 -- Putting Little Pieces Together
# Looked at solutions for 07_py-csv.py, and amalgamated a simpler/better version of the occupations.py and integrated it with the app.py.
# 2020-10-13
from flask import Flask
import csv
import random
app = Flask(__name__)
@app.route("/")

def hello_world():
  occupations_dict = {} #dictionary created!

  with open("occupations.csv") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter =',') #reading the csv file
      for row in csv_reader: #for each row
        if row[0].startswith("Job Class") or row[0].startswith("Total"):continue #skips first and last line
        occupations_dict[row[0]] = float(row[1]) #putting the stuff in the dict (name key, percent value).

  all_occupations = list(occupations_dict.keys())
  all_chances = occupations_dict.values()
  result = random.choices(all_occupations, weights = all_chances, k = 1) #using the values as the weights for probability, and the last line's total percent as the total weight!

  #compile list of the dictionary to be added to the return statement
  occup_list = "<br>LIST<br>------<br>"+ "<br>".join(occupations_dict)# title/header for the list and then the body of the list—concatenated list

  #random.choices() returns a list. Gotta get the 0th index of a 1 item list.
  return(result[0] + " (Chance: " + str(occupations_dict.get(result[0])) + "%) <br>" + occup_list) #Returns the random occupation, as well as a list of all the occupations

if __name__ == "__main__":  # true if this file NOT imported
  app.debug = True        # enable auto-reload upon code change
  app.run()
