from abc import ABC, abstractmethod
from model.events.lamp_event import LampEvent

class AbstractLightService(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def handleEvent(self, event: LampEvent) -> None:
        pass
