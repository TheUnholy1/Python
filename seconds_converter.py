def convert_seconds(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60
    return hours, minutes, seconds
total_seconds = 3661
hours, minutes, seconds = convert_seconds(total_seconds)

print("Total seconds:", total_seconds)
print("Hours:", hours)
print("Minutes:", minutes)
print("Seconds:", seconds)
