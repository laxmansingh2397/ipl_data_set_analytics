import csv 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

deliveries_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/deliveries.csv"))
matches_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/matches.csv"))

def top_batsman_rcb(data):
    rcb_batsman = {}
    for team_match in data:
        if team_match["batting_team"] == "Royal Challengers Bangalore":
            if team_match["batsman"] in rcb_batsman:
                rcb_batsman[team_match["batsman"]] += int(team_match["total_runs"])
            else:
                rcb_batsman[team_match["batsman"]] = int(team_match["total_runs"])

    reversed_rcb_batsman = dict(sorted(rcb_batsman.items(), key=lambda total_runs : total_runs[1], reverse=True))

    top_ten_batsman_data = dict(list(reversed_rcb_batsman.items())[:10])

    batsman = list(top_ten_batsman_data.keys())
    total_runs = list(top_ten_batsman_data.values())

    return batsman,total_runs

def plot_chart(batsman,runs):
    plt.figure(figsize=(8,3))
    plt.title("Top_Ten_Batsman")
    plt.bar(batsman, runs, color="blue")
    plt.xlabel("Batsman")
    plt.ylabel("Total_runs")
    plt.tight_layout()
    plt.xticks(rotation=45, ha="right")
    plt.show()

plot_chart(*top_batsman_rcb(deliveries_data))