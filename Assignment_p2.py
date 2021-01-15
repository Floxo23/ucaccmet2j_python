import csv
import json

# Part 1

with open('precipitation.json') as file:
    data = json.load(file) #loading in the file
    prec_seattle = [] #create empty variable
    for measurement in data: 
      if (measurement['station']) == 'GHCND:US1WAKG0038': #looping over all data to check if they include Seattle
        prec_seattle.append({'date': measurement['date'],'value':measurement['value']}) #append the data for Seattle to the empty variable
         
months = ['2010-01', '2010-02', '2010-03', '2010-04', '2010-05', '2010-06', '2010-07', '2010-08', '2010-09', '2010-10', '2010-11', '2010-12'] # define what months to include for the dates
with open('result.json', 'w') as file_result: #open file that we will later create
  results = [] #create empty variable for pt. 1 results (this will be a dictionary)
  sum_results = [] #create empty variable for a list of all value without dates (for Part 2)
  for month in months:
    prec_monthly = 0 # create a pooling variable to count the values for the months to 
    for i in prec_seattle: 
        if month in i['date']:
          prec_monthly += i['value'] # loop over the data always adding the value for each month to the variable
    results.append ({month:prec_monthly}) # append that to the results variable making it a list of dictionaries with months included 
    sum_results.append(prec_monthly) # append only the value of each month as a list into the empty varible (Prep for Part 2)
  json.dump(results, file_result, indent=1) # make a Json file with the results variable 
 
# Part 2.1

annual_sum = sum(sum_results) # just add together all monthly values saved above to get an annual sum of rain
#print(annual_sum)

# Part 2.2

# dvivide each month by the annual_sum (i.e. Jan / sum_results)
Relative_pr = [] #create an empty value to later store my stuff in
for i in sum_results:
  perc=[i/annual_sum]  #work out the percentage of each month looping over the list with monthly values 
  Relative_pr.append(perc) #append that to the empty list I made above 
#print(Relative_pr)