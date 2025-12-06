def parse_log_line(line):
    parts = line.strip().split(" - ")
    timestamp = parts[0]
    level_message = parts[1].split(": ", 1)
    level = level_message[0]
    message = level_message[1]
    return timestamp, level, message

with open("device_log.txt", "r") as file:
    for line in file:
        timestamp, level, message = parse_log_line(line)
        print(f"Timestamp: {timestamp}, Level: {level}, Message: {message}")
        