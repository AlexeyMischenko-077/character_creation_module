def calculation(x, y):
    return (x - y) * (y - x) - 2


print('Модуль запущен')
print('Проверка работы функции')
print(543 == calculation(93, 88))
print(543 == calculation(102, 58))
print(543 == calculation(221, 188))
print(543 == calculation(193, 188))




print("Без применения cleandoc:")
print(Test.first.__doc__)
print("С применением cleandoc:")
print(inspect.cleandoc(Test.first.__doc__))
