"""
This example showcases entangled qubits!
"""

import numpy as np

from pyqusim import QPU, Circuit, had, phase_shift, measure

circuit = Circuit()
with circuit:
    had(index=0)
    had(index=1)
    phase_shift(phi=np.pi, index=1).controlled(control=0)
    had(index=1)
    measure(index=(0, 1))

qpu = QPU(n_qubits=2)
result = circuit.run_multiple(qpu=qpu, n=1000, normalize=True)

# 50% (0, 0) and 50% (1, 1)
print(result)
