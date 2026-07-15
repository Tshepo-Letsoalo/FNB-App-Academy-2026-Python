students = [
    {"name": "Thabo", "maths": 85, "english": 78, "science": 90},
    {"name": "Sarah", "maths": 45, "english": 60, "science": 55},
    {"name": "Lerato", "maths": 92, "english": 88, "science": 95},
    {"name": "John", "maths": 35, "english": 40, "science": 38},
    {"name": "Zanele", "maths": 70, "english": 75, "science": 72}
]

results = []
all_avgs = []

for s in students:
    avg = (s["maths"] + s["english"] + s["science"]) / 3
    all_avgs.append(avg)
    
    if avg >= 80: grade = "A"
    elif avg >= 70: grade = "B"
    elif avg >= 60: grade = "C"
    elif avg >= 50: grade = "D"
    else: grade = "F"
    
    status = "Pass" if avg >= 50 else "Fail"
    results.append({"name": s["name"], "avg": avg, "grade": grade, "status": status})
    print(f"{s['name']}: Avg {avg:.1f}, Grade {grade}, {status}")

print(f"\nClass Avg: {sum(all_avgs)/len(all_avgs):.1f}")
print(f"Highest: {max(all_avgs):.1f}, Lowest: {min(all_avgs):.1f}")

while True:
    search = input("\nSearch student (or 'exit'): ")
    if search == 'exit': break
    for r in results:
        if r['name'].lower() == search.lower():
            print(f"Found: {r}")