import csv 
import matplotlib
matplotlib.use('TkAgg')
from matplotlib import pyplot as plt

deliveries_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/deliveries.csv"))
matches_data = csv.DictReader(open("/home/laxman/python_virtual_env/ipl/required_data/matches.csv"))
umpires_data = {
            'RB Tiffin': 'Zimbabwe',
            'S Das': 'India',
            'A Nand Kishore': 'India',
            'TH Wijewardene': 'Sri Lanka',
            'PR Reiffel': 'Australia',
            'AL Hill': 'England',
            'RM Deshpande': 'India',
            'SD Fry': 'Australia',
            'C Shamshuddin': 'India',
            'AM Saheba': 'India',
            'IL Howell': 'South Africa',
            'DJ Harper': 'Australia',
            'AY Dandekar': 'India',
            'AK Chaudhary': 'India',
            'K Srinivasan': 'India',
            'BNJ Oxenford': 'Australia',
            'RK Illingworth': 'England',
            'Aleem Dar': 'Pakistan',
            'SJ Davis': 'Australia',
            'S Asnani': 'India',
            'K Srinath': 'India',
            'SL Shastri': 'India',
            'MR Benson': 'England',
            'CB Gaffaney': 'New Zealand',
            'RJ Tucker': 'Australia',
            'GAV Baxter': 'New Zealand',
            'RE Koertzen': 'South Africa',
            'I Shivram': 'India',
            'PG Pathak': 'India',
            'SS Hazare': 'India',
            'CK Nandan': 'India',
            'SJA Taufel': 'Australia',
            'KN Ananthapadmanabhan': 'India',
            'BG Jerling': 'South Africa',
            'Asad Rauf': 'Pakistan',
            'K Bharatan': 'India',
            'A Deshmukh': 'India',
            'BF Bowden': 'New Zealand',
            'GA Pratapkumar': 'India',
            'BR Doctrove': 'West Indies',
            'Nitin Menon': 'India',
            'VA Kulkarni': 'India',
            'K Hariharan': 'India',
            'SK Tarapore': 'India',
            'Subroto Das': 'India',
            'HDPK Dharmasena': 'Sri Lanka',
            'M Erasmus': 'South Africa',
            'AV Jayaprakash': 'India',
            'VK Sharma': 'India',
            'JD Cloete': 'South Africa',
            'YC Barde': 'India',
            'NJ Llong': 'England',
            'SD Ranade': 'India',
            'S Ravi': 'India'
        }
def total_umpires(data):
    umpires_count = {}

    for umpires,country in data.items():
        if country in umpires_count:
            umpires_count[country] += 1
        else:
            umpires_count[country] = 1

    del umpires_count["India"]

    country = list(umpires_count.keys())
    count = list(umpires_count.values())

    return country,count

def plot_chart(country,count):
    plt.figure(figsize=(8,3))
    plt.title("Total_Umpire_from_country")
    plt.bar(country, count, color="blue")
    plt.xlabel("country")
    plt.ylabel("Total_umpires")
    plt.tight_layout()
    plt.xticks(rotation=45, ha="right")
    plt.show()

plot_chart(*total_umpires(umpires_data))