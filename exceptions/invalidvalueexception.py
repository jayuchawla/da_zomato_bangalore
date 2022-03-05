class InvalidValue(Exception):
    def __init__(self, msg='invalid value'):
        self.msg = msg
        super().__init__(self.msg)
    def __str__(self):
        return self.msg

if __name__ == '__main__':
    raise InvalidValue