from quantalpy.qpu import QPU
from quantalpy.runnable import Runnable
import quantalpy.typing as qpt
from quantalpy.utils import export


@export
class Measure(Runnable):
    def __init__(self, index: qpt.Indices) -> None:
        self.index = index

    @property
    def ends_with_measure(self) -> bool:
        return True

    def run(self, qpu: QPU) -> qpt.MeasureOutcome:
        indices = qpu.get_qubit_indices(self.index)
        outcomes = tuple(qpu.measure(i) for i in indices)
        if len(outcomes) == 1:
            return outcomes[0]
        return outcomes
