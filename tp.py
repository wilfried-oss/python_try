class A:
    def func(self):
        print("Cool")


class B:
    def func(self):
        print("Cool")


if __name__ == '__main__':
    elements = [A(), B()]
    for item in elements:
        item.func()
