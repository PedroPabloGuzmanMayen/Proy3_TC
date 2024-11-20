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
        self.output_tape = []
        self.memory = " "
        self.head_position = 0
        self.current_state = initial_state

    def load_tape(self, input_string):
        self.tape = list(input_string.upper()) + ['_']  # Convertir a mayúsculas y agregar símbolo en blanco
        self.head_position = 0
        print(f"Cinta cargada: {''.join(self.tape)}")  # Depuración

    def generate_output_tape(self):
        self.output_tape = [" "] * len(self.tape)

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
    
    def cipher(self, input_message):
        self.load_tape(input_message)
        self.generate_output_tape()
        while self.current_state not in self.accept_states:

            pass
        pass

    def run(self):
        while self.current_state not in self.accept_states:
            if not self.step():
                break
        return ''.join(self.tape).strip('_')

def load_machine_config(filename):
    with open(filename, 'r') as f:
        return json.load(f)
    
machine = TuringMachine(**load_machine_config('test_encryption_machine.json'))

print(machine.input_alphabet)

print(machine.output_tape)

print(machine.transitions["q0"][" "]["(A, )"])