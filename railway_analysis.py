import csv

file_path = "data/railway.csv"
trains = []

with open(file_path, newline="", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        row["Delay_Min"] = int(row["Delay_Min"])
        row["Passengers"] = int(row["Passengers"])
        trains.append(row)

total_passengers = sum(t["Passengers"] for t in trains)
total_delay = sum(t["Delay_Min"] for t in trains)
average_delay = total_delay / len(trains) if trains else 0

print("=" * 40)
print("RAILWAY DATA ANALYSIS")
print("=" * 40)
print("Total trains:", len(trains))
print("Total passengers:", total_passengers)
print("Average delay:", round(average_delay, 2), "minutes")

print("\nTOP 5 MOST DELAYED TRAINS")
for train in sorted(trains, key=lambda t: t["Delay_Min"], reverse=True)[:5]:
    print(train["Train_Name"], "-", train["Delay_Min"], "minutes")

with open("railway_results.txt", "w", encoding="utf-8") as output:
    output.write("RAILWAY DATA ANALYSIS\n")
    output.write(f"Total trains: {len(trains)}\n")
    output.write(f"Total passengers: {total_passengers}\n")
    output.write(f"Average delay: {average_delay:.2f} minutes\n")
    output.write("\nTop 5 most delayed trains:\n")
    for train in sorted(trains, key=lambda t: t["Delay_Min"], reverse=True)[:5]:
        output.write(f'{train["Train_Name"]}: {train["Delay_Min"]} minutes\n')

print("\nResults saved to railway_results.txt")
