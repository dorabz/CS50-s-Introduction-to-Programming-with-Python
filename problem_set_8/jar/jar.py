class Jar:
    def __init__(self, capacity=12):
        self._size = 0
        if capacity >= 0:
            self._capacity = capacity
        else:
            raise ValueError

    def __str__(self):
        return '🍪' * self.size

    def deposit(self, n):
        if self.size + n <= self.capacity:
            self._size = self._size + n
        else:
            raise ValueError

    def withdraw(self, n):
        if n <= self.size:
            self._size = self._size - n
        else:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size