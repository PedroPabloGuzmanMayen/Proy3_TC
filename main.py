import json
from TM import TuringMachine
'''
class TuringMachine:
    def __init__(self, states, input_alphabet, tape_alphabet, initial_state, accept_states, transitions):
        self.states = states
        self.input_alphabet = input_alphabet
        self.tape_alphabet = tape_alphabet
        self.initial_state = initial_state
        self.accept_states = accept_states
        self.transitions = transitions
        self.tape = []
        self.head_position = 0
        self.current_state = initial_state

    def load_tape(self, input_string):
        self.tape = list(input_string.upper()) + ['_']  # Convertir a mayúsculas y agregar símbolo en blanco
        self.head_position = 0
        print(f"Cinta cargada: {''.join(self.tape)}")  # Depuración

    def step(self):
        current_symbol = self.tape[self.head_position]
        transition_key = f"({self.current_state}, {current_symbol})"
        print(f"Buscando clave: {transition_key}")
        transition = self.transitions.get(transition_key)
        if not transition:
            print(f"No hay transición válida para la clave {transition_key}.")
            return False  # No valid transition, halt
        next_state, write_symbol, direction = transition
        print(f"Transición: ({self.current_state}, {current_symbol}) -> ({next_state}, {write_symbol}, {direction})")
        self.tape[self.head_position] = write_symbol
        self.current_state = next_state
        self.head_position += 1 if direction == 'R' else -1
        return True

    def run(self):
        while self.current_state not in self.accept_states:
            if not self.step():
                break
        return ''.join(self.tape).strip('_')

def load_machine_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)

def validate_input(message):
    """Validar que el mensaje siga el formato 'k#mensaje'."""
    if '#' not in message or len(message.split('#')) != 2:
        print("Formato inválido. Debe ser 'k#mensaje' donde 'k' es la llave.")
        return False
    return True

def show_examples():
    """Mostrar ejemplos de encriptación y desencriptación."""
    print("\n=== Ejemplos de Encriptación y Desencriptación ===")
    examples = [
        ("3#ROMA NO FUE CONSTRUIDA EN UN DIA", "URPD QR IXH FRQVWUXLGD HQ XQ GLD"),
        ("2#PYTHON ES DIVERTIDO", "RAVJQP GU FKXGTXKFQ")
    ]
    for original, encrypted in examples:
        print(f"Original: {original}")
        print(f"Encriptado: {encrypted}")
        print()
'''

def show_examples():
    """Mostrar ejemplos de encriptación y desencriptación."""
    print("\n=== Ejemplos de Encriptación y Desencriptación ===")
    examples = [
        ("D#ROMA NO FUE CONSTRUIDA EN UN DIA", "URPD QR IXH FRQVWUXLGD HQ XQ GLD"),
        ("C#PYTHON ES DIVERTIDO", "RAVJQP GU FKXGTXKFQ")
    ]
    for original, encrypted in examples:
        print(f"Original: {original}")
        print(f"Encriptado: {encrypted}")
        print()

def validate_input(message):
    """Validar que el mensaje siga el formato 'k#mensaje'."""
    if '#' not in message or len(message.split('#')) != 2:
        print("Formato inválido. Debe ser 'k#mensaje' donde 'k' es la llave.")
        return False
    return True

def load_machine_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)
def menu():
    print("\n=== Máquina de Turing - Cifrado César ===")
    print("1. Encriptar mensaje")
    print("2. Desencriptar mensaje")
    print("3. Mostrar ejemplos")
    print("4. Salir")
    return input("Selecciona una opción: ")

def main():
    # Cargar configuraciones de las máquinas
    encryption_config = load_machine_config("test_encryption_machine.json")
    encryption_tm = TuringMachine(**encryption_config)

    decryption_config = load_machine_config("test_decryption_machine.json")
    decryption_tm = TuringMachine(**decryption_config)

    while True:
        choice = menu()
        if choice == "1":
            message = input("Ingresa el mensaje para encriptar (formato: k#mensaje): ")
            if not validate_input(message):
                continue
            encryption_tm.cipher(message)
            print("\nProceso de encriptación:")
            print(f"\nMensaje encriptado: {encryption_tm.cipher(message)}")
        elif choice == "2":
            message = input("Ingresa el mensaje para desencriptar (formato: k#mensaje): ")
            if not validate_input(message):
                continue
            print("\nProceso de desencriptación:")
            print(f"\nMensaje desencriptado: {decryption_tm.cipher(message)}")
        elif choice == "3":
            show_examples()
        elif choice == "4":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
