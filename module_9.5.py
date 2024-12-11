# "Итераторы"
# Задача "Range - это просто"


class StepValueError(ValueError):
    pass


class Iterator:
    def __init__(self, start, stop, step=1):
        if step != 0:
            self.step = step             # шаг
        else:
            raise StepValueError('Шаг не может быть равен 0')
        self.start = start               # начало
        self.stop = stop                 # конец    
        self.pointer = start             # текущая итерация

 # метод, сбрасывает pointer на start и возвращает сам объект итератора.
    def __iter__(self):
        self.pointer = self.start
        return self


  # метод, увеличивающий атрибут pointer на step.
  # В зависимости от знака атрибута step итерация завершится
  # либо когда pointer станет больше stop, либо меньше stop
    def __next__(self): 
 #       if self.pointer == self.start
        if (self.step > 0 and self.pointer > self.stop) or (self.step < 0 and self.pointer < self.stop):
            raise StopIteration()  
        current_pointer = self.pointer   
        self.pointer += self.step                 
        return current_pointer


try:
    iter1 = Iterator(100, 200, 0)
    for i in iter1:
        print(i, end=' ')
except StepValueError as exc:
    print('Шаг указан неверно', exc)


iter2 = Iterator(-5, 1)
iter3 = Iterator(6, 15, 2)
iter4 = Iterator(5, 1, -1)
iter5 = Iterator(10, 1)


for i in iter2:
    print(i, end=' ')
print()
for i in iter3:
    print(i, end=' ')
print()
for i in iter4:
    print(i, end=' ')
print()
for i in iter5:
    print(i, end=' ')
print()
