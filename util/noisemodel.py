# Import from Qiskit Aer noise module
from qiskit_aer.noise import (NoiseModel, QuantumError, ReadoutError,
    pauli_error, depolarizing_error, thermal_relaxation_error)





def construct_bitflip_noise_model(p_reset, p_meas, p_gate1):
    # Example error probabilities
    p_reset = p_reset
    p_meas = p_meas
    p_gate1 = p_gate1

    # QuantumError objects
    error_reset = pauli_error([('X', p_reset), ('I', 1 - p_reset)])
    error_meas = pauli_error([('X',p_meas), ('I', 1 - p_meas)])
    error_gate1 = pauli_error([('X',p_gate1), ('I', 1 - p_gate1)])
    error_gate2 = error_gate1.tensor(error_gate1)

    # Add errors to noise model
    noise_bit_flip = NoiseModel()
    noise_bit_flip.add_all_qubit_quantum_error(error_reset, "reset")
    noise_bit_flip.add_all_qubit_quantum_error(error_meas, "measure")
    noise_bit_flip.add_all_qubit_quantum_error(error_gate1, ["t","tdag"])
    noise_bit_flip.add_all_qubit_quantum_error(error_gate2, ["cx"])

    return noise_bit_flip



def construct_gate_bitflip_noise_model(p_gate):

    error_gate = pauli_error([('X',p_gate), ('I', 1 - p_gate)])
    error_gate2 = error_gate.tensor(error_gate)
    # Add errors to noise model
    noise_bit_flip = NoiseModel()
    noise_bit_flip.add_all_qubit_quantum_error(error_gate2 , ["cx"])

    return noise_bit_flip






def construct_phaseflip_noise_model(p_reset, p_meas, p_gate1):
    # Example error probabilities
    p_reset = p_reset
    p_meas = p_meas
    p_gate1 = p_gate1

    # QuantumError objects
    error_reset = pauli_error([('Z', p_reset), ('I', 1 - p_reset)])
    error_meas = pauli_error([('Z',p_meas), ('I', 1 - p_meas)])
    error_gate1 = pauli_error([('Z',p_gate1), ('I', 1 - p_gate1)])
    error_gate2 = error_gate1.tensor(error_gate1)


    # Add errors to noise model
    noise_phase_flip = NoiseModel()
    noise_phase_flip.add_all_qubit_quantum_error(error_reset, "reset")
    noise_phase_flip.add_all_qubit_quantum_error(error_meas, "measure")
    noise_phase_flip.add_all_qubit_quantum_error(error_gate1, ["t","tdag"])
    noise_phase_flip.add_all_qubit_quantum_error(error_gate2, ["cz"])

    return noise_phase_flip



def construct_bitphaseflip_noise_model(p_reset, p_meas, p_gate1):
    # Example error probabilities
    p_reset = p_reset
    p_meas = p_meas
    p_gate1 = p_gate1

    # QuantumError objects
    error_reset = pauli_error([('Z', p_reset), ('I', 1 - p_reset)])
    error_meas = pauli_error([('Z',p_meas), ('I', 1 - p_meas)])
    error_gate1 = pauli_error([('Z',p_gate1), ('I', 1 - p_gate1)])
    error_gate2 = error_gate1.tensor(error_gate1)

    # QuantumError objects
    error_reset_bit = pauli_error([('X', p_reset), ('I', 1 - p_reset)])
    error_meas_bit = pauli_error([('X',p_meas), ('I', 1 - p_meas)])
    error_gate1_bit = pauli_error([('X',p_gate1), ('I', 1 - p_gate1)])
    error_gate2_bit = error_gate1_bit.tensor(error_gate1)

    # Add errors to noise model
    noise_bitphase_flip = NoiseModel()
    noise_bitphase_flip.add_all_qubit_quantum_error(error_reset_bit, "reset")
    noise_bitphase_flip.add_all_qubit_quantum_error(error_meas_bit, "measure")
    noise_bitphase_flip.add_all_qubit_quantum_error(error_gate1_bit, ["t","tdg"])
    noise_bitphase_flip.add_all_qubit_quantum_error(error_gate2_bit, ["cx"])

    return noise_bitphase_flip