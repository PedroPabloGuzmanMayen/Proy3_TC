import json

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

def menu():
    print("\n=== Máquina de Turing - Cifrado César ===")
    print("1. Encriptar mensaje")
    print("2. Desencriptar último mensaje encriptado")
    print("3. Salir")
    choice = input("Selecciona una opción: ")
    return choice

def main():
    # Cargar configuraciones de las máquinas
    encryption_config = load_machine_config("encryption_machine.json")
    encryption_tm = TuringMachine(**encryption_config)

    decryption_config = load_machine_config("decryption_machine.json")
    decryption_tm = TuringMachine(**decryption_config)

    # Variable para almacenar el mensaje encriptado
    last_encrypted_message = None

    while True:
        choice = menu()
        if choice == "1":
            message = input("Ingresa el mensaje para encriptar (formato: k#mensaje): ")
            encryption_tm.load_tape(message)
            print("\nProceso de encriptación:")
            last_encrypted_message = encryption_tm.run()
            print(f"\nMensaje encriptado: {last_encrypted_message}")
        elif choice == "2":
            if last_encrypted_message is None:
                print("\nNo hay ningún mensaje encriptado para desencriptar.")
            else:
                decryption_tm.load_tape(last_encrypted_message)
                print("\nProceso de desencriptación:")
                decrypted_message = decryption_tm.run()
                print(f"\nMensaje desencriptado: {decrypted_message}")
        elif choice == "3":
            print("Saliendo del programa. ¡Hasta luego!")
            break
        else:
            print("Opción no válida, intenta de nuevo.")

if __name__ == "__main__":
    main()
