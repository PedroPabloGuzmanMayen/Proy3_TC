import json

# Initialize parameters
alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
state = "q0"
memory_placeholder = "-"
tape2_placeholder = "-"
movement = "R"

# Create transitions
transitions = {
    state: {
        memory_placeholder: {
            f"({letter}, {tape2_placeholder})": {
                "memory_value": letter,
                "tape1_value": letter,
                "tape2_value": tape2_placeholder,
                "movement": movement
            }
            for letter in alphabet
        }
    }
}

# Output as JSON
with open("transitions.json", "w") as f:
    json.dump(transitions, f, indent=4)

print("JSON file generated.")
