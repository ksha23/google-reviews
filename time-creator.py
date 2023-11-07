from datetime import datetime, timedelta

# Get the current date and time
current_datetime = datetime.now()

# Calculate the date and time three days ago
three_days_ago = current_datetime - timedelta(days=3)

# Format the date and time as 'YYYY-MM-DD HH:MM:SS'
formatted_date = three_days_ago.strftime("%Y-%m-%d %H:%M:%S")
print("Three days ago:", formatted_date)
