print(f"NameError - {type(NameError)} - {issubclass(NameError, BaseException)}")
try:
    try:
        print("start cod")
        print(10/0)
        print("not error")
    except (NameError, ZeroDivisionError):
        print("we have an error")
except(NameError, ZeroDivisionError):
    print("we have an error")
print("code after capsule")
#-----------------------------------------------------------------------------------------

def check(var_1):
    if type(var_1)!=str:
        raise TypeError(f"Sorry, we can't work with {type(var_1)}," f"we need class str")
    else:
        return var_1
first_var=10
check(first_var)

class BuildingError(Exception):
    def __str__(self):
        return f"3 такою кількістю матеріалів будинок побудувати не можливо"
def check_material(amount_material, limit_value):
    if amount_material>limit_value:
        return f"Матеріалу достатньо"
    else:
        raise BuildingError(amount_material)
material=123
check_material(material, 300)
#---------------------------------------------------------------------------------------------

class FoodError(Exception):
    def __str__(self):
        return f"З такою кількістю продуктів нічого не пригутуєш"
def check_material(amount_material, limit_value):
    if amount_material>limit_value:
        return f"продуктів достатньо"
    else:
        raise FoodError(amount_material)
material = 3
check_material(material, 10)

