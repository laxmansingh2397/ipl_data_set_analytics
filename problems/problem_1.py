import csv 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

deliveries_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/deliveries.csv"))
matches_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/matches.csv"))

def teams_total_runs(data):
    batting_team_total_runs = {}
    for teams_match in data:
        if teams_match["batting_team"] in batting_team_total_runs:
            batting_team_total_runs[teams_match["batting_team"]] += int(teams_match["total_runs"])
        else:
            batting_team_total_runs[teams_match["batting_team"]] = int(teams_match["total_runs"])

    batting_team_total_runs["Rising Pune Supergiant"] += batting_team_total_runs["Rising Pune Supergiants"]
    del batting_team_total_runs["Rising Pune Supergiants"]

    teams = list(batting_team_total_runs.keys())
    runs = list(batting_team_total_runs.values())

    return teams,runs

def plot_chart(teams,runs):
    plt.figure(figsize=(8,3))
    plt.title("Total_Teams_runs")
    plt.bar(teams, runs, color="blue")
    plt.xlabel("Total_Teams")
    plt.ylabel("Total_runs")
    plt.tight_layout()
    plt.xticks(rotation=45, ha="right")
    plt.show()

plot_chart(*teams_total_runs(deliveries_data))