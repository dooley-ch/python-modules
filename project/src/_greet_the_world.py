__all__ = ['GreetTheWorld']


class GreetTheWorld:
    def __init__(self, name: str):
        self._name = name

    def say_hello(self):
        print(f'Hello from GreetTheWorld: {self._name}')
