from typing import Any, TypeAlias

JSON: TypeAlias = dict[str, Any]


class Model:
    def __init__(self, payload: JSON):
        self.payload = payload


class Field:
    def __init__(self, path: str):
        self.path = path
        self.keys = self.path.split('.')


    @staticmethod
    def recursive_access(keys, nested, value=None):
        if len(keys) == 1:
            key = keys[0]
            if value:
                nested[key] = value
            return nested[key]
        else:
            key = keys[0]
            if key not in nested.keys():
                return None
            return Field.recursive_access(keys[1:], nested[key], value=value)

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        payload = instance.__dict__.get('payload')
        return Field.recursive_access(self.keys, payload)

    
    def __set__(self, instance, value):
        payload = instance.__dict__.get('payload')
        Field.recursive_access(self.keys, payload, value)
   


