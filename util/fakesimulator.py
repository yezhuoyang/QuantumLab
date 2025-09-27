
from qiskit.providers.fake_provider import GenericBackendV2





def fakeQC_6qubits():
    coupling_map=[[0, 4], [0, 2], [4, 2], [2, 3], [4, 1], [0, 5]]

    # Generate a 6-qubit simulated backend
    backend = GenericBackendV2(num_qubits=6,coupling_map=coupling_map)


    # Customize the noise level on each fake qubit.
    # Please don't modify it during your experiment
    backend.target['measure'][(0,)].error = 0.15
    backend.target['measure'][(4,)].error = 0.15
    backend.target['measure'][(2,)].error = 0.15

    for (i,j) in coupling_map:
            backend.target['cx'][(i,j)].error = 0.2        
    
    backend.target['measure'][(3,)].error = 0.35
    backend.target['measure'][(1,)].error = 0.35
    backend.target['measure'][(5,)].error = 0.35
    
    return backend