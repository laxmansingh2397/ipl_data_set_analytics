import csv 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

deliveries_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/deliveries.csv"))
matches_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/matches.csv"))

def extra_run_of_teams(data):
    extra_run = {}
    match_id = []
    for match in data:
        if match["season"] == "2016":
            match_id.append(match["id"])

    for match in deliveries_data:
        if match["match_id"] in match_id:
            if match["batting_team"] in extra_run:
                extra_run[match["batting_team"]] += int(match["extra_runs"])
            else:
                extra_run[match["batting_team"]] = int(match["extra_runs"])
    print(extra_run)
    teams = list(extra_run.keys())
    extra = list(extra_run.values())

    return teams,extra

def plot_chart(teams,extra):
    plt.figure(figsize=(8,3))
    plt.title("Extra Run Per Team")6
    plt.bar(teams, extra, color="blue")
    plt.xlabel("Teams")
    plt.ylabel("Extra_Runs")
    plt.tight_layout()
    plt.xticks(rotation=45, ha="right")
    plt.show()

plot_chart(*(extra_run_of_teams(matches_data)))
