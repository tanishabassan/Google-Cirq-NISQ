import cirqy
import numpy as np
from cirq import Circuit
from cirq.devices import GridQubit
from cirq.google import XmonSimulator

#creating circuit with 4 qubits
length = 4

#qubits on a grid
qubits = [cirq.GridQubit(i,j) for i in range(length) for j in range(length)]
print(qubits)

circuit = cirq.Circuit()

## all gates applied to circuit
H1 = cirq.H(qubits[2])
TOFFOLI = cirq.TOFFOLI(qubits[2], qubits[3], qubits[4])
H2 = cirq.H(qubits[1])
H3 = cirq.H(qubits[2])
H4 = cirq.H(qubits[3])
CZ1 = cirq.CZ(qubits[2], qubits[1])
CZ2 = cirq.CZ(qubits[2], qubits[3])

## contstructing moments of gates to apply on circuit
moment1 = cirq.Moment([H1])
moment2 = cirq.Moment([TOFFOLI])
moment3 = cirq.Moment([H1])
moment4 = cirq.Moment([H2, H3, H4])
moment5 = cirq.Moment([CZ1])
moment6 = cirq.Moment([CZ2])
moment7 = cirq.Moment([H2, H3, H4])

simulator = cirq.google.XmonSimulator()
result = simulator.simulate(circuit)
print(result)

circuit = cirq.Circuit((moment1, moment2, moment3, moment4, moment5, moment6, moment7))
print(circuit)
simulator = cirq.google.XmonSimulator()
result = simulator.simulate(circuit)
print(result)
