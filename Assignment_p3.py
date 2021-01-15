import json

# Part 3

with open('precipitation.json') as file:
    data = json.load(file)
    stations = [] #create an empty array for all stations 
    for i in stations: 
      indiv_stations = [] #create an empty array for each individual station
      for lines in data: 
        if lines['station'] == i: #if the station lines equal my stations then ...
          indiv_stations.append({'date':lines['date'], 'value':lines['value'], 'station':lines['station']}) # append the corresponding data to it 
      stations.append(indiv_stations) # and append that to my total empty array (so it does this 4 times i.e. for each station) 

print(stations)

# It is strange that the above code doesnt work and I can't really figure out why ... before it worked ... 

months = ['2010-01', '2010-02', '2010-03', '2010-04', '2010-05', '2010-06', '2010-07', '2010-08', '2010-09', '2010-10', '2010-11', '2010-12']
sum_results = []
for station in range(len(stations)): # do the following for each station in the length of the station number (4)
  sumprec = [] # create an empty array
  for month in months: # loop over all the months
    monthly_prec = 0 # create an empty aray
    for i in stations[station]: # for the stations ...
      if month in i['date']: # ... if the months from above appear in the dates ...
        monthly_prec += i['value'] # ... add the values up and store them into the previously created array
    sumprec.append(monthly_prec) # now append that to the first array 
  sum_results.append(sumprec) # and then through the second
  #json.dump(newresults, file_newresult, indent=1)  
  #print(newresults)
#total_all = sum(sum_results)
print(sum_results)

# This second part of the code also doesn't really work ... probably because the first one doesn't ... Not sure again.