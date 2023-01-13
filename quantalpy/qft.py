import numpy as np

from quantalpy.circuit import Circuit
from quantalpy.unary_qubit_gate import Hadamard, PhaseShift
from quantalpy.binary_qubit_gate import ControlledQubitGate
from quantalpy.ctx_funcs import had, phase_shift
from quantalpy.utils import export
import quantalpy.typing as qpt


@export
def qft(indices: qpt.Indices) -> Circuit:
    c = Circuit()
    indices = (1, 2, 3, 4, 5, 6)

    with c:
        for idx, i in enumerate(indices, start=1):
            had(i)
            for jdx, j in enumerate(indices[idx:], start=1):
                print(idx, idx + jdx)
                phase_shift(phi=2 * np.pi / (2 ** (idx + jdx)), index=i).controlled(
                    control=j
                )

    # for i in indices:
    #     c.gates.append(Hadamard(i))
    #     for a, x in enumerate(range(2, len(indices) + 1 - i), start=1):
    #         gate = PhaseShift(phi=2 * np.pi / (2**x), index=i)
    #         c.gates.append(ControlledQubitGate(gate=gate, control=i + a))

    return c
