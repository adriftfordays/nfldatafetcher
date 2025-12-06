parts = ["user=john.doe action=login ip=192.168.1.50 result=failed reason=invalid password"]
parts = log_Line.split(" ", 4)
action = parts[1].split("=")[1]

actionlog = {parts[1]: parts[2]}
print(actionlog)
