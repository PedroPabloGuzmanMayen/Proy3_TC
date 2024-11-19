import json
import string

def generate_encryption_transitions(shift):
    transitions = {}
    alphabet = list(string.ascii_uppercase) + [" ", "#"]
    n = len(alphabet)

    # Generar transiciones para las letras
    for i, letter in enumerate(alphabet[:-1]):  # Excluye el separador #
        shifted_index = (i + shift) % (n - 1)  # No rota el separador #
        transitions[f"(q1, {letter})"] = ["q1", alphabet[shifted_index], "R"]

    # Añadir transición para la llave, separador y estado final
    transitions["(q0, 3)"] = ["q1", "3", "R"]
    transitions["(q1, #)"] = ["q1", "#", "R"]
    transitions["(q1, _)"] = ["q_accept", "_", "R"]
    return transitions

def generate_decryption_transitions(shift):
    transitions = {}
    alphabet = list(string.ascii_uppercase) + [" ", "#"]
    n = len(alphabet)

    # Generar transiciones para las letras
    for i, letter in enumerate(alphabet[:-1]):  # Excluye el separador #
        shifted_index = (i - shift) % (n - 1)  # No rota el separador #
        transitions[f"(q1, {letter})"] = ["q1", alphabet[shifted_index], "R"]

    # Añadir transición para la llave, separador y estado final
    transitions["(q0, 3)"] = ["q1", "3", "R"]
    transitions["(q1, #)"] = ["q1", "#", "R"]
    transitions["(q1, _)"] = ["q_accept", "_", "R"]
    return transitions

def save_transitions_to_file(filename, transitions):
    machine = {
        "states": ["q0", "q1", "q_accept"],
        "input_alphabet": list(string.ascii_uppercase) + [" ", "#"],
        "tape_alphabet": list(string.ascii_uppercase) + [" ", "#", "_"],
        "initial_state": "q0",
        "accept_states": ["q_accept"],
        "transitions": transitions
    }
    with open(filename, "w") as f:
        json.dump(machine, f, indent=4)

# Generar y guardar transiciones
encryption_transitions = generate_encryption_transitions(shift=3)
save_transitions_to_file("encryption_machine.json", encryption_transitions)

decryption_transitions = generate_decryption_transitions(shift=3)
save_transitions_to_file("decryption_machine.json", decryption_transitions)
