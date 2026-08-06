from datetime import datetime

LOG_FILE = "logs.txt"

while True:
    message = input("Enter log message (or type exit): ")

    if message.lower() == "exit":
        break

    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(LOG_FILE, "a") as file:
        file.write(f"[{current_time}] {message}\n")

    print("Log saved.")