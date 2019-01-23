import math

class Person:
    def __init__(self, name, surname, position):
        self._name = name
        self._surname = surname
        self._position = position

    def __repr__(self):
        return self._name + ' ' + self._surname + ' ' + self._position

    @staticmethod
    def dev(name, surname):
        return Person(name, surname, 'developer')

    @classmethod
    def stu(cls, name, surname):
        return cls(name, surname, 'student')

    @property
    def full_name(self):
        return self._name + ' ' + self._surname

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, val):
        self._name = val

    @property
    def surname(self):
        return self._surname

    @surname.setter
    def surname(self, val):
        self._name = val

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, val):
        self._name = val

class Developer(Person):
    pass

class Student(Person):
    pass

class Built_in():
    def __init__(self, k, m, n, l, s, b):
        self.num = k
        self.num_complex = complex(m, n)
        self.list = l
        self.str = s
        self.bool = b
        self.attr1 = 'attr_1'
        self.attr2 = 'attr_2'

    def out(self, output, flag, *input):
        if flag:
            print()
            print(output.__name__, end='\n\t')
        print(output.__name__, '(',*input, ') = ', output(*input), end='\n\t', sep='')

    def __str__(self):
        return 'object '

    def abs_info(self): # num and bool and complex
        self.out(abs,True, self.num)
        self.out(abs,False, self.num_complex)
        self.out(abs,False, self.bool)

    def all_info(self): # iterable
        self.out(all, True, self.list)

    def any_info(self): # iterable
        self.out(any, True, self.list)

    def ascii_info(self): # object
        self.out(ascii, True, self.str)
        self.out(ascii, False, self.bool)
        self.out(ascii, False, self.num)
        self.out(ascii, False, self.list)

    def bin_info(self): # num and bool or obj having __index__
        self.out(bin, True, self.num)
        self.out(bin, False, self.bool)

    def bool_info(self):  # is a subclass of num
        self.out(bool, False, self.bool)
        self.out(bool, False, self.num_complex)
        self.out(bool, False, self.str)
        self.out(bool, False, self.list)
        self.out(bool, False, ['ANYTHING'])
        self.out(bool, False, ())

    def chr_info(self):  # num
        self.out(chr, True, self.num)
        self.out(chr, False, self.bool)

    def delattr_info(self):
        self.out(delattr, True, self, 'attr2')

    def dir_info(self):
        self.out(dir, True, self)
        self.out(dir, False, )
        self.out(dir, False, math)


ex = Built_in(72, 2, 4, (4, 5, 1<2), '√', True)

ex.abs_info()
ex.all_info()
ex.any_info()
ex.ascii_info()
ex.bin_info()
ex.bool_info()
ex.chr_info()
ex.delattr_info()
ex.dir_info()
