from tqdm import tqdm
import time
import subprocess

# Function to read lines from a file and strip newline characters
def read_lines_from_file(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()
    return [line.strip() for line in lines]

# Function to execute a command and handle errors
def execute_command(command):
    try:
        print("Executing command:", command)
        subprocess.run(command, shell=True, check=True)
        print("Command executed successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error: Command '{command}' failed with exit code {e.returncode}.")
        print("Error output:", e.output.decode())
    except Exception as e:
        print("An unexpected error occurred:", e)

# Function to generate commands based on usernames and event IDs
def generate_commands(usernames_file, ids_file):
    # Read usernames and event IDs from respective files
    usernames = read_lines_from_file(usernames_file)
    ids = read_lines_from_file(ids_file)
    
    commands = [] # List to store generated commands

    # Loop through event IDs with progress bar
    for event_id in tqdm(ids, desc="Processing IDs"):
        # Loop through usernames
        for username in usernames:
            # Generate command for deleting event for each username and event ID
            command = f'gam calendar {username} deleteevent eventid "{event_id}" doit'
            commands.append(command) # Append command to list of commands

    return commands # Return the list of generated commands

# File paths for usernames and event IDs
usernames_file = 'usernames.txt'
ids_file = 'ids.txt'

# Generate commands
commands = generate_commands(usernames_file, ids_file)

# Open a file to write the results
with open('results.txt', 'w') as result_file:
    # Loop through the commands with tqdm progress bar
    for command in tqdm(commands, desc="Processing Commands"):
        # Write each command to the results file
        result_file.write(command + '\n')
        # Execute the command
        execute_command(command)
        # Add a 10-second wait after each command execution
        time.sleep(3)
