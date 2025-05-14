import csv 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

deliveries_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/deliveries.csv"))
matches_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/matches.csv"))

def total_matches_per_season(data):
    total_matches_year= {}
    for match in matches_data:
        if match["season"] in total_matches_year:
            total_matches_year[match["season"]] += 1
        else:
            total_matches_year[match["season"]] = 1
    print(total_matches_year)

    years = list(total_matches_year.keys())
    total_match = list(total_matches_year.values())

    return years,total_match

def plot_chart(years,total_match):
    plt.figure(figsize=(8,3))
    plt.title("Total_Matches_Per_Season")
    plt.bar(years, total_match, color="blue")
    plt.xlabel("Total_Season")
    plt.ylabel("Total_Match")
    plt.tight_layout()
    plt.xticks(rotation=45, ha="right")
    plt.show()

plot_chart(*total_matches_per_season(matches_data))
