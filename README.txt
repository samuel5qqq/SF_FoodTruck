# The Task
## Data
The San Francisco government’s website has a public data source of food trucks (https://data.sfgov.org/Economy-and-Community/Mobile-Food-Schedule/jjew-r69b). The data can be accessed in a number of forms, including JSON, CSV, and XML. How you access the data is up to you, but you can find some useful information about making an API request to this data source here (https://dev.socrata.com/foundry/data.sfgov.org/bbb8-hzi6).
The Problem
Write a command line program that prints out a list of food trucks that are open at the current date and current time, when the program is being run. So if I run the program at noon on a Friday, I should see a list of all the food trucks that are open then.
## Criteria
Please display results in pages of 10 trucks. That is: if there are more than 10 food trucks open, the program should display the first 10, then wait for input from the user before displaying the next 10 (or fewer if there are fewer than 10 remaining), and so on until there are no more food trucks to display. Display the name and address of the trucks and sort the output alphabetically by name.
## Example
$ show-open-food-trucks
NAME ADDRESS Mang Hang Catering 1 Thomas More Way Steve’s Mobile Deli 145 King Street

## Program Execution
1. Install Dependencies:
   - Check Python’s version is 3.7.3
   I use three external Python library for my program, need to install Python Library datetime, requests, pandas 
   For Mac OS, open terminal and run the following command to install the library
     • pip3 install datetime
     • pip3 install requests
     • pip3 install datetime
2. Run the program:
   ⁃ Simply use command line to navigate to the project folder
     • cd /Users/samuelchen/PycharmProjects/Food_Truck
   ⁃ Execute there program
     • python3 show_open_food_trucks.py
