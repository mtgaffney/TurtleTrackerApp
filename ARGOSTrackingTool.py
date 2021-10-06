#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Michael Gaffney (michael.gaffney@duke.edu)
# Date:   Fall 2021
#--------------------------------------------------------------

#Ask user for the search date
user_date = input("Enter date to search for Sara: ")

#Create a variable pointing to data file
file_name = './data/raw/sara.txt'

#Create a file object from the file
file_object = open(file_name,'r')

#Read contenst of file into list
line_list = file_object.readlines()

#Close the file
file_object.close()

#Create two epmty dictionary objects
date_dict = {}
coord_dict = {}

#Pretend we read one line of data from the file
for lineString in line_list:
    if lineString[0] in ("#","u"): continue
    #Split the string into a list of data items
    lineData = lineString.split()
    
    #Extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    obs_lat = lineData[6]
    obs_long = lineData[7]
    
    #Print the location of sara if the lc is 1,2, or 3
    if obs_lc in ("1","2","3"):
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat,obs_long)

#Create empty list to hold matching keys
matching_keys = []

#Loop through items in the date_dict and collect keys for matching ones
for date_item in date_dict.items():
    #Get the key and date of the dictionary item 
    the_key, the_date = date_item
    #See if the date matches the use date
    if the_date == user_date:
        #If so, add the key to the list
        matching_keys.append(the_key)
        
#Reveal the locationms for eacgh key in the matching keys
for matching_keys in matching_keys:
    obs_lat, obs_long = coord_dict[matching_keys]
    print(f"Record {matching_keys} indicates Sara was seen at lat: {obs_lat}, lon: {obs_long} on {user_date}")