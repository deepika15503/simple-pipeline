# scripts/process_data.py

input_file = "data/input.txt"
output_file = "data/output.txt"

print("Pipeline started...")

with open(input_file, "r", encoding="utf-8") as f:
    lines = f.readlines()

filtered_lines = []

for line in lines:
    clean_line = line.strip()
    if not clean_line:
        continue
    parts = clean_line.split()
    if len(parts) < 3:
        continue
    try:
        age = int(parts[2])
        if age >= 18:
            filtered_lines.append(clean_line + "\n")
    except ValueError:
        continue

with open(output_file, "w", encoding="utf-8") as f:
    f.writelines(filtered_lines)

print("Pipeline completed!")
