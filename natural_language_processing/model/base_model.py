from abc import ABC, abstractmethod
from natural_language_processing.configurations.configuration_infrastructure import Config

"""We have to think about the infrastructure  before we dive into the code of the model.
Abstract Model Class (ABC) that is inherited to all models."""


class BaseModel(ABC):

    def __init__(self, cfg):
        super().__init__()
        self.config = Config.from_json(cfg)

    @abstractmethod
    def load_data(self, **kwargs):
        pass

    @abstractmethod
    def build(self, **kwargs):
        pass

    @abstractmethod
    def train(self, **kwargs):
        pass

    @abstractmethod
    def evaluate(self, **kwargs):
        pass
