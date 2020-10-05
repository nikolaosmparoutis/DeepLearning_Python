import json


class Config:
    """Config class which contains data, train and model hyperparameters"""

    def __init__(self, external_data_sources, data, train, model):
        self.external_data_sources = external_data_sources
        self.data = data
        # self.train = train
        # self.model = model

    @classmethod
    def from_json(cls, cfg):
        """Creates config from json"""
        params = json.loads(json.dumps(cfg), object_hook=HelperObject)
        return cls(params.train, params.external_data_sources)


class HelperObject(object):
    """Helper class to convert json into Python object"""
    def __init__(self, dict_):
        self.__dict__.update(dict_)