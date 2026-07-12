# core/asset.py

from abc import ABC, abstractmethod

class Asset(ABC):

    @property
    @abstractmethod
    def asset_id(self):
        ...

    @property
    @abstractmethod
    def owner(self):
        ...

    @owner.setter
    @abstractmethod
    def owner(self, value):
        ...

    @property
    @abstractmethod
    def holder(self):
        ...

    @holder.setter
    @abstractmethod
    def holder(self, value):
        ...

    @property
    @abstractmethod
    def location(self):
        ...

    @location.setter
    @abstractmethod
    def location(self, value):
        ...

    @abstractmethod
    def serialize(self):
        ...


    ≠≠