# main.py

with open("login_logs.txt", "r") as file:
    logs = file.readlines()

failed_attempts = {}

for line in logs:
    line = line.strip()
    parts = line.split(",")

    if len(parts) == 4:
        timestamp, username, ip, status = parts

        if status == "FAILED":
            if username not in failed_attempts:
                failed_attempts[username] = 1
            else:
                failed_attempts[username] += 1

# نطبع المستخدمين اللي عندهم أكثر من 3 محاولات فاشلة

for user, count in failed_attempts.items():
    if count >= 3:
        print(f"⚠️  {user} {count} has failed login attempts.")

import csv 

with open("suspicious_users.csv","w",newline="") as csvfile: 
    writer = csv.writer(csvfile)
    writer.writerow(["username","failed_attempts"])
    for user, count in failed_attempts.items():
        if count >= 3:
            writer.writerow([user,count])
# Generate HTML report
html_content = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Suspicious Login Report</title>
    <style>
        body { font-family: Arial; background-color: #f4f4f4; padding: 20px; }
        h2 { color: #333; }
        table { width: 50%; border-collapse: collapse; margin-top: 20px; }
        th, td { border: 1px solid #999; padding: 8px; text-align: center; }
        th { background-color: #555; color: white; }
        tr:nth-child(even) { background-color: #eee; }
    </style>
</head>
<body>
    <h2>🚨 Suspicious Login Attempts Report</h2>
    <table>
        <tr>
            <th>Username</th>
            <th>Failed Attempts</th>
        </tr>
"""

# Add table rows
for user, count in failed_attempts.items():
    if count >= 3:
        html_content += f"<tr><td>{user}</td><td>{count}</td></tr>\n"

# Close HTML
html_content += """
    </table>
</body>
</html>
"""

# Save the report to file
with open("report.html", "w", encoding="utf-8") as file:
    file.write(html_content)

print("🌐 HTML report generated: report.html")
