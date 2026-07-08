from collections import Counter

LOG_FILE = "sample.log"
OUTPUT_FILE = "summary.txt"

levels = Counter()
messages = []

with open(LOG_FILE, "r") as file:
    for line in file:
        parts = line.strip().split()

        if len(parts) < 4:
            continue

        level = parts[2]
        message = " ".join(parts[3:])

        levels[level] += 1

        if level == "ERROR":
            messages.append(message)

print("=" * 40)
print("LOG ANALYSIS REPORT")
print("=" * 40)

print(f"INFO    : {levels['INFO']}")
print(f"WARNING : {levels['WARNING']}")
print(f"ERROR   : {levels['ERROR']}")

print("\nError Messages")

for msg in messages:
    print("-", msg)

with open(OUTPUT_FILE, "w") as output:
    output.write("LOG ANALYSIS REPORT\n")
    output.write("===================\n\n")

    output.write(f"INFO    : {levels['INFO']}\n")
    output.write(f"WARNING : {levels['WARNING']}\n")
    output.write(f"ERROR   : {levels['ERROR']}\n\n")

    output.write("Error Messages\n")

    for msg in messages:
        output.write(f"- {msg}\n")

print("\nSummary saved to summary.txt")
