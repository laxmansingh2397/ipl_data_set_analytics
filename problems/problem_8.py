import csv 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

deliveries_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/deliveries.csv"))
matches_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/matches.csv"))

def top_ten_economical_bowler(data):
    match_id = []
    total_bowlers = {}

    for match in data:
        if match["season"] == "2015":
            match_id.append(match["id"])

    for match in deliveries_data:
        if match["match_id"] in match_id:
            if match["bowler"] in total_bowlers:
                total_bowlers[match["bowler"]] += int(match["total_runs"])
            else:
                total_bowlers[match["bowler"]] = int(match["total_runs"])

    sorted_bowlers = dict(sorted(total_bowlers.items(), key=lambda total_runs : total_runs[1]))
    top_ten_bowlers = dict(list(sorted_bowlers.items())[:10])
    print(top_ten_bowlers)

    bowlers = list(top_ten_bowlers.keys())
    runs = list(top_ten_bowlers.values())

    return bowlers,runs

def plot_chart(bowlers,runs):
    plt.figure(figsize=(8,3))
    plt.title("Top Ten Economical Bowlers")
    plt.bar(bowlers, runs, color="blue")
    plt.xlabel("Bowlers")
    plt.ylabel("Total_runs")
    plt.tight_layout()
    plt.xticks(rotation=45, ha="right")
    plt.show()

plot_chart(*top_ten_economical_bowler(matches_data))