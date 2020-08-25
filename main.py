#!/usr/bin/python
import json
import sys
import os.path as directory

#Check for argument passing to be correct
if len(sys.argv) != 2:
	print("Pass exactly one jsonfile to execute this code.")
	sys.exit()

#Check for the file to exists
filename = sys.argv[1]
if not directory.isfile(filename):
	print("Chosen file doesn't exists.\nProvide exactly an existing jsonfile to execute this code.")
	sys.exit()

with open(filename) as f:
  raw_data = json.load(f)


#Check for the k-value proposed system. 
#NOTE: Actually only the basic one is developed
adjustment = 0
k_factor = 0
if "k-adjustment" not in raw_data or raw_data["k-adjustment"] == "none":
	if "k-value" not in raw_data or "average" not in raw_data["k-value"]:
		print("No k-value provided. Check your config file.")
		sys.exit()
	k_factor = raw_data["k-value"]["average"]
else:
	adjustment = 1
	k_factor = [raw_data["k-value"]["beginner"],raw_data["k-value"]["average"],raw_data["k-value"]["top"]]

#load the users and bad formed files.
users = []
if "users" not in raw_data:
	print("Not users found . Check your config file.")
	sys.exit()
users = raw_data["users"]

if len(users) < 2:
	print("Not enough player to implement an Elo rating system. Check your config file.")
	sys.exit()

for player in users:
	if "name" not in player or "rating" not in player:
		print("A player is wrongly defined. Check your config file.")
		sys.exit()

#Check for the turnaround value to exists
turnaround = 0
if "turnaround" not in raw_data:
	print("No turnaround value found. Check your config file.")
	sys.exit()
turnaround = raw_data["users"]
if turnaround < 1:
	print("No positive turnaround value found. Check your config file.")
	sys.exit()