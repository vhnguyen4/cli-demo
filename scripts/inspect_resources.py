"""Inspect fictional practice data. Run from the repository root."""

import csv

# Supplied loading code: csv.DictReader reads each row as a dictionary.
# This relative path starts at the terminal's current working directory.
with open("data/resources.csv", newline="", encoding="utf-8") as source:
    resources = list(csv.DictReader(source))

# TODO 1: Replace None with an expression that counts the resources.
resource_count = None

# TODO 2: Change this slice to show the first THREE resources.
preview = resources[:2]

print("Fictional campus resources")
if resource_count is None:
    print("Resource count: TODO — complete the counting expression")
else:
    print(f"Resource count: {resource_count}")

print("Preview:")
for resource in preview:
    print(f"- {resource['name']} ({resource['category']})")
