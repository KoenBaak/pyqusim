from pyqusim.measure import Measure
from pyqusim.unary_qubit_gate import Hadamard, PhaseShift

import pyqusim.typing as pqst


def had(index: int) -> None: Hadamard
def phase_shift(phi: float, index: int) -> None: PhaseShift
def measure(index: pqst.Indices) -> None: Measure
