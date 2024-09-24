from qiskit import QuantumCircuit
from qiskit_aer import AerSimulator
from termcolor import colored




def NOT(inp):
    """An NOT gate.
    
    Parameters:
        inp (str): Input, encoded in qubit 0.
        
    Returns:
        QuantumCircuit: Output NOT circuit.
        str: Output value measured from qubit 0.
    """

    qc = QuantumCircuit(1, 1) # A quantum circuit with a single qubit and a single classical bit
    qc.reset(0)
    
    # We encode '0' as the qubit state |0⟩, and '1' as |1⟩
    # Since the qubit is initially |0⟩, we don't need to do anything for an input of '0'
    # For an input of '1', we do an x to rotate the |0⟩ to |1⟩
    if inp=='1':
        qc.x(0)
        
    # barrier between input state and gate operation 
    qc.barrier()
    
    # Now we've encoded the input, we can do a NOT on it using x
    qc.x(0)
    
    #barrier between gate operation and measurement
    qc.barrier()
    
    # Finally, we extract the |0⟩/|1⟩ output of the qubit and encode it in the bit c[0]
    qc.measure(0,0)
    qc.draw()
    
    # We'll run the program on a simulator
    backend = AerSimulator()
    # Since the output will be deterministic, we can use just a single shot to get it
    job = backend.run(qc, shots=1, memory=True)
    output = job.result().get_memory()[0]
    
    return qc, output


def XOR(inp1,inp2):
    """An XOR gate.
    
    Parameters:
        inpt1 (str): Input 1, encoded in qubit 0.
        inpt2 (str): Input 2, encoded in qubit 1.
        
    Returns:
        QuantumCircuit: Output XOR circuit.
        str: Output value measured from qubit 1.
    """
  
    qc = QuantumCircuit(2, 1) 
    qc.reset(range(2))
    
    if inp1=='1':
        qc.x(0)
    if inp2=='1':
        qc.x(1)
    
    # barrier between input state and gate operation 
    qc.barrier()
    
    # this is where your program for quantum XOR gate goes
    
    
    
    
    
    
    
    
    # barrier between input state and gate operation 
    qc.barrier()
    
    qc.measure(1,0) # output from qubit 1 is measured
  
    #We'll run the program on a simulator
    backend = AerSimulator()
    #Since the output will be deterministic, we can use just a single shot to get it
    job = backend.run(qc, shots=1, memory=True)
    output = job.result().get_memory()[0]
  
    return qc, output



def AND(inp1,inp2):
    """An AND gate.
    
    Parameters:
        inpt1 (str): Input 1, encoded in qubit 0.
        inpt2 (str): Input 2, encoded in qubit 1.
        
    Returns:
        QuantumCircuit: Output XOR circuit.
        str: Output value measured from qubit 2.
    """
    qc = QuantumCircuit(3, 1) 
    qc.reset(range(2))
  
    if inp1=='1':
        qc.x(0)
    if inp2=='1':
        qc.x(1)
        
    qc.barrier()

    # this is where your program for quantum AND gate goes

    
    
    
    
    

    qc.barrier()
    qc.measure(2, 0) # output from qubit 2 is measured
  
    # We'll run the program on a simulator
    backend = AerSimulator()
    # Since the output will be deterministic, we can use just a single shot to get it
    job = backend.run(qc, shots=1, memory=True)
    output = job.result().get_memory()[0]
  
    return qc, output



def NAND(inp1,inp2):
    """An NAND gate.
    
    Parameters:
        inpt1 (str): Input 1, encoded in qubit 0.
        inpt2 (str): Input 2, encoded in qubit 1.
        
    Returns:
        QuantumCircuit: Output NAND circuit.
        str: Output value measured from qubit 2.
    """
    qc = QuantumCircuit(3, 1) 
    qc.reset(range(3))
    
    if inp1=='1':
        qc.x(0)
    if inp2=='1':
        qc.x(1)
    
    qc.barrier()
    
    # this is where your program for quantum NAND gate goes


    
    
    
    
    
    qc.barrier()
    qc.measure(2, 0) # output from qubit 2 is measured
  
    #We'll run the program on a simulator
    backend = AerSimulator()
    # Since the output will be deterministic, we can use just a single shot to get it
    job = backend.run(qc,shots=1,memory=True)
    output = job.result().get_memory()[0]
  
    return qc, output


def OR(inp1,inp2):
    """An OR gate.
    
    Parameters:
        inpt1 (str): Input 1, encoded in qubit 0.
        inpt2 (str): Input 2, encoded in qubit 1.
        
    Returns:
        QuantumCircuit: Output XOR circuit.
        str: Output value measured from qubit 2.
    """

    qc = QuantumCircuit(3, 1) 
    qc.reset(range(3))
    
    if inp1=='1':
        qc.x(0)
    if inp2=='1':
        qc.x(1)
    
    qc.barrier()
   
    # this is where your program for quantum OR gate goes


    

    
    
    qc.barrier()
    qc.measure(2, 0) # output from qubit 2 is measured
  
    #We'll run the program on a simulator
    backend = AerSimulator()
    # Since the output will be deterministic, we can use just a single shot to get it
    job = backend.run(qc,shots=1,memory=True)
    output = job.result().get_memory()[0]
  
    return qc, output


def testNOT():
    qc1, output1 = NOT('1')
    qc0, output0 = NOT('0')    
    if output0 == '1' and output1 == '0':
        print(colored('Congrats, NOT Test passed ','green')+"\U0001f600")
    else:
        print(colored('OOPS, NOT Test failed! ','red')+"\U0001F923")        


def testXOR():
    qc00, output00 = XOR('0','0')
    qc01, output01 = XOR('0','1')   
    qc10, output10 = XOR('1','0')
    qc11, output11 = XOR('1','1')   
    if output01 == '1' and output10 == '1' and output11 == '0' and output00 == '0':
        print(colored('Congrats, XOR Test passed ','green')+"\U0001f600")
    else:
        print(colored('OOPS, XOR Test failed! ','red')+"\U0001F923")    


def testAND():
    qc00, output00 = AND('0','0')
    qc01, output01 = AND('0','1')   
    qc10, output10 = AND('1','0')
    qc11, output11 = AND('1','1')   
    if output01 == '0' and output10 == '0' and output11 == '1' and output00 == '0':
        print(colored('Congrats, AND Test passed ','green')+"\U0001f600")
    else:
        print(colored('OOPS, AND Test failed! ','red')+"\U0001F923")    


def testNAND():
    qc00, output00 = AND('0','0')
    qc01, output01 = AND('0','1')   
    qc10, output10 = AND('1','0')
    qc11, output11 = AND('1','1')   
    if output01 == '1' and output10 == '1' and output11 == '0' and output00 == '1':
        print(colored('Congrats, NAND Test passed ','green')+"\U0001f600")
    else:
        print(colored('OOPS, NAND Test failed! ','red')+"\U0001F923")    


def testOR():
    qc00, output00 = OR('0','0')
    qc01, output01 = OR('0','1')   
    qc10, output10 = OR('1','0')
    qc11, output11 = OR('1','1')   
    if output01 == '1' and output10 == '1' and output11 == '1' and output00 == '0':
        print(colored('Congrats, OR Test passed ','green')+"\U0001f600")
    else:
        print(colored('OOPS, OR Test failed! ','red')+"\U0001F923")    


def testANDOR():
    pass




if __name__ == '__main__':
    print("-----------Strating the tests of IBM Lab1: logical gates-----------")
    testNOT()
    testXOR()
    testAND()
    testNAND()
    testOR()
    print("--------------------------Your score is:--------------------------")    


