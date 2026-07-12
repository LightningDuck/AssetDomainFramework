# core/custodian.py

from abc import ABC, abstractmethod

class AssetCustodian(ABC):

    @property
    @abstractmethod
    def custodian_id(self):
        ...

    @property
    @abstractmethod
    def name(self):
        ...

    @abstractmethod
    def serialize(self):
        ...