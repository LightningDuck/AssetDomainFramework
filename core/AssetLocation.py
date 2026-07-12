# core/location.py

from abc import ABC, abstractmethod

class AssetLocation(ABC):

    @property
    @abstractmethod
    def location_id(self):
        ...

    @property
    @abstractmethod
    def description(self):
        ...

    @abstractmethod
    def serialize(self):
        ...