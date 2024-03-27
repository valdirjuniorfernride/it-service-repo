import subprocess

# Path to GAM executable
GAM_PATH = '/path/to/gam'

# Path to the usernames file
USER_IDS_FILE = 'usernames.txt'

# Path to the event IDs file
EVENT_IDS_FILE = 'ids.txt'

# Read event IDs from the file
with open(EVENT_IDS_FILE, 'r') as event_file:
    event_ids = event_file.readlines()

# Remove newline characters from event IDs
event_ids = [event_id.strip() for event_id in event_ids]

# Read username from the file and delete events for each user
with open(USER_IDS_FILE, 'r') as user_file:
    user_ids = user_file.readlines()

# Remove newline characters from usernames
user_ids = [user_id.strip() for user_id in user_ids]

# Iterate through each event ID and each user ID to delete events
for event_id in event_ids:
    print(f"Deleting event with ID: {event_id}")
    for user_id in user_ids:
        print(f"  - for user: {user_id}")
        # Run GAM command to delete event
        command = f'{GAM_PATH} calendar {user_id} deleteevent eventid "{event_id}" doit'
        result = subprocess.run(command, shell=True, capture_output=True, text=True)
        if result.returncode == 0:
            print("  Successfully deleted event.")
        else:
            print(result.stderr.strip())

