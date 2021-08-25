from code import check_for_symmetry
from code import convert_to_numbers
from code import is_prime
from code import get_intersection
from code import get_union

print(check_for_symmetry("tacocat"))
print(check_for_symmetry("pinapple"))
print(check_for_symmetry("kayak"))
print(check_for_symmetry("potato"))
print(check_for_symmetry("symmetry"))

print(convert_to_numbers("tacocat"))
print(convert_to_numbers("pinapple"))
print(convert_to_numbers("kayak"))
print(convert_to_numbers("potato"))
print(convert_to_numbers("symmetry"))

print(is_prime(20))
print(is_prime(16))
print(is_prime(86))
print(is_prime(25))
print(is_prime(37))

print(get_intersection([1,3,5,7,8],[2,4,6,8,7]))
print(get_intersection([78,83,21,99],[43,16,45,58]))
print(get_intersection([66,63,96,25],[63,14,84,69]))
print(get_intersection([84,78,99,69],[21,25,69,81]))
print(get_intersection([42,61,42,17],[33,83,20,28]))

print(get_union([1,3,5,7,8],[2,4,6,8,7]))
print(get_union([78,83,21,99],[43,16,45,58]))
print(get_union([66,63,96,25],[63,14,84,69]))
print(get_union([84,78,99,69],[21,25,69,81]))
print(get_union([42,61,42,17],[33,83,20,28]))
