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
        self.tape = list(input_string.upper()) + [" "]  # Convertir a mayúsculas y agregar símbolo en blanco
        self.head_position = 0
        print(f"Cinta cargada: {''.join(self.tape)}")  # Depuración

    def generate_output_tape(self):
        self.output_tape = [" "] * len(self.tape)

    def step(self):
        current_symbol = self.tape[self.head_position]
        print(f"Current symbol: {current_symbol}")
        tape2_symbol = self.output_tape[self.head_position]
        print(f"Current symbol tape2: {tape2_symbol}")
        print(f"Memory: {self.memory}")
        values = self.transitions[self.current_state][self.memory][f"({current_symbol},{tape2_symbol})"]
        self.current_state = values["next_state"]
        print(f"Next state: {self.current_state}")
        self.memory = values["memory_value"]
        self.output_tape[self.head_position] = values["tape2_value"]
        if values["movement"] == "R":
            if self.head_position != len(self.tape) - 1:
                self.head_position += 1
    
    def cipher(self, input_message):
        self.load_tape(input_message)
        self.generate_output_tape()
        while self.current_state not in self.accept_states:
            self.step()
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

print(machine.transitions["q0"][" "]["(D, )"])





machine.cipher("D#HOLA")

print(machine.output_tape)