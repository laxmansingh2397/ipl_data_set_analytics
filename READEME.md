# IPL DATA Set Analytics

* This project reads IPL deliveries and matches data from a CSV file and visualizes the data with the help of matplotlib

### Prerequisites
* Python3.x installled on your system 
* pip(Python Package Manager)

### Installation

1. **Clone this repository(or download the code files):**
```
git clone https://github.com/yourusername/ipl-team-runs.git
```
2. **Install required packages from requirement.txt.**
```
pip freeze > requirements.txt
```
This command will install all required package you want to run this project.

This file is inside ipl folder

3. **Ensure your CSV file is present correctly.**
Place the deliveries.csv and matches.csv file at the following path (or update the script with your path):
```
/home/laxman/python_virtual_env/ipl/required_data/deliveries.csv
/home/laxman/python_virtual_env/ipl/required_data/matches.csv
```

### Usage

1. **Edit the file path(if needed):**
If your CSV file is in a different location, update the path in the script:
```
deliveries_data = csv.DictReader(open("path/to/your/deliveries.csv"))
matches_data = csv.DictReader(open("path/to/your/matches.csv"))
```

2. **Run the script:**
```
python3 your_script_name.py
```
If you are using any **IDE** you can run it from there