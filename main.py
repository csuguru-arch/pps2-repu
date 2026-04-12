import time
import json
from tracker_utils import calculate_duration, format_time

# Dictionary to store session data
session_data = {}

# Set to store unique session names
session_names = set()

# Function to start tracking
def start_tracking():
    try:
        name = input("Enter session name: ")

        if name in session_names:
            print("Session already exists! Try a different name.")
            return

        session_names.add(name)

        print("Tracking started... Stay away from phone 📵")
        start_time = time.time()

        input("Press ENTER to stop tracking...")

        end_time = time.time()

        duration = calculate_duration(start_time, end_time)

        # Store in dictionary
        session_data[name] = duration

        print(f"Session '{name}' recorded: {duration} seconds")

    except Exception as e:
        print("Error occurred while tracking:", e)


# Function to save data to file
def save_to_file():
    try:
        with open("phone_free_data.json", "w") as file:
            json.dump(session_data, file)
        print("Data saved successfully 💾")
    except IOError:
        print("File error occurred!")


# Function to load data from file
def load_from_file():
    global session_data
    try:
        with open("phone_free_data.json", "r") as file:
            session_data = json.load(file)
        print("Data loaded successfully 📂")
    except FileNotFoundError:
        print("No previous data found.")
    except json.JSONDecodeError:
        print("File is corrupted!")


# Function to display report
def show_report():
    try:
        if not session_data:
            print("No sessions recorded yet!")
            return

        print("\n📊 Phone-Free Report:")
        for name, duration in session_data.items():
            print(f"{name} → {duration} sec ({format_time(duration)} min)")

    except Exception as e:
        print("Error displaying report:", e)


# Main menu function
def main():
    load_from_file()

    while True:
        print("\n--- Phone-Free Tracker ---")
        print("1. Start Tracking")
        print("2. Show Report")
        print("3. Save Data")
        print("4. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            start_tracking()
        elif choice == "2":
            show_report()
        elif choice == "3":
            save_to_file()
        elif choice == "4":
            save_to_file()
            print("Goodbye 👋")
            break
        else:
            print("Invalid choice! Try again.")


# Run program
if __name__ == "__main__":
    main()
