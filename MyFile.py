#Nathaniel Peck
#Dota2_Matches

#imports request function to get data from api
import requests
import json

#imports GUI
from tkinter import *

request = requests.get('https://api.opendota.com/api/proMatches')

#api data
data = request.json()

#declares all match details
#num is item in list
def match_details(num):
	global match_id 
	match_id = data[num]["match_id"]
	global duration
	duration = data[num]["duration"]
	global start_time
	start_time = data[num]["start_time"]
	global radiant_team_id
	radiant_team_id = data[num]["radiant_team_id"]
	global radiant_name
	radiant_name = data[num]["radiant_name"]
	global dire_team_id
	dire_team_id = data[num]["dire_team_id"]
	global dire_name
	dire_name = data[num]["dire_name"]
	global leagueid
	leagueid = data[num]["leagueid"]
	global league_name
	league_name = data[num]["league_name"]
	global series_id
	series_id = data[num]["series_id"]
	global series_type
	series_type = data[num]["series_type"]
	global radiant_score
	radiant_score = data[num]["radiant_score"]
	global dire_score
	dire_score = data[num]["dire_score"]
	global radiant_win
	radiant_win = data[num]["radiant_win"]


### Begin GUI ###

#Main Window of GUI
root = Tk()

#Main text
label_match_id = Label(root, text="Match ID")
label_duration = Label(root, text="Duration")
label_start_time = Label(root, text="Start Time")
label_radiant_team_id = Label(root, text="Radiant Team ID")
label_radiant_name = Label(root, text="Radiant Name")
label_dire_team_id = Label(root, text="Dire Team ID")
label_dire_name = Label(root, text="Dire Name")
label_leagueid = Label(root, text="League ID")
label_league_name = Label(root, text="League Name")
label_series_id = Label(root, text="Series ID")
label_series_type = Label(root, text="Series Type")
label_radiant_score = Label(root, text="Radiant Score")
label_dire_score = Label(root, text="Dire Score")
label_radiant_win = Label(root, text="Radiant Win")
###

#Placement of the Text
label_match_id.grid(row=0, column=0)
label_duration.grid(row=0, column=1)
label_start_time.grid(row=0, column=2)
label_radiant_team_id.grid(row=0, column=3)
label_radiant_name.grid(row=0, column=4)
label_dire_team_id.grid(row=0, column=5)
label_dire_name.grid(row=0, column=6)
label_leagueid.grid(row=0, column=7)
label_league_name.grid(row=0, column=8)
label_series_id.grid(row=0, column=9)
label_series_type.grid(row=0, column=10)
label_radiant_score.grid(row=0, column=11)
label_dire_score.grid(row=0, column=12)
label_radiant_win.grid(row=0, column=13)
###

i = 0 #counter
r = 1 #r for row number
#Loop to create content for all data from api
while i < len(data):
	match_details(i)
	
	info_match_id = Label(root, text= match_id)
	info_duration = Label(root, text= duration)
	info_start_time = Label(root, text= start_time)
	info_radiant_team_id = Label(root, text= radiant_team_id)
	info_radiant_name = Label(root, text= radiant_name)
	info_dire_team_id = Label(root, text= dire_team_id)
	info_dire_name = Label(root, text= dire_name)
	info_leagueid = Label(root, text= leagueid)
	info_league_name = Label(root, text= league_name)
	info_series_id = Label(root, text= series_id)
	info_series_type = Label(root, text= series_type)
	info_radiant_score = Label(root, text= radiant_score)
	info_dire_score = Label(root, text= dire_score)
	info_radiant_win = Label(root, text= radiant_win)
	
	info_match_id.grid(row=r, column=0)
	info_duration.grid(row=r, column=1)
	info_start_time.grid(row=r, column=2)
	info_radiant_team_id.grid(row=r, column=3)
	info_radiant_name.grid(row=r, column=4)
	info_dire_team_id.grid(row=r, column=5)
	info_dire_name.grid(row=r, column=6)
	info_leagueid.grid(row=r, column=7)
	info_league_name.grid(row=r, column=8)
	info_series_id.grid(row=r, column=9)
	info_series_type.grid(row=r, column=10)
	info_radiant_score.grid(row=r, column=11)
	info_dire_score.grid(row=r, column=12)
	info_radiant_win.grid(row=r, column=13)
	r = r+1
	
	i = i+1

root.mainloop()

### End GUI ###
