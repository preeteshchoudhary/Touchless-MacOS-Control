import yaml
import os

class GestureMapper:
    def __init__(self, config_path='config/gestures.yaml'):
        self.config_path = config_path
        self.mappings = self._load_mappings()

    def _load_mappings(self):
        with open(self.config_path) as f:
            return yaml.safe_load(f) or {}

    def map_gesture(self, gesture):
        return self.mappings.get(gesture)
