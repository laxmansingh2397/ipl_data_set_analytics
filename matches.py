import csv

with open('/home/laxman/python_virtual_env/my_env/ipl/required_data/matches.csv','r') as csvfile:
    matches_data = csv.DictReader(csvfile)

    for matches in matches_data:
        print(matches)