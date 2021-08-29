from code import check_for_symmetry
from code import convert_to_numbers
from code import is_prime
from code import get_intersection
from code import get_union
from code import count_characters
from code import get_first_n_terms_nonrecursive
from code import get_nth_term_recursive
from code import convert_to_base_10
from code import convert_to_base_2

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

print(count_characters("tacocat"))
print(count_characters("pinapple"))
print(count_characters("kayak"))
print(count_characters("potato"))
print(count_characters("symmetry"))
#need to figure out what's wrong

print(get_first_n_terms_nonrecursive(1))
print(get_first_n_terms_nonrecursive(2))
print(get_first_n_terms_nonrecursive(3))
print(get_first_n_terms_nonrecursive(4))
print(get_first_n_terms_nonrecursive(5))

print(get_nth_term_recursive(1))
print(get_nth_term_recursive(2))
print(get_nth_term_recursive(3))
print(get_nth_term_recursive(4))
print(get_nth_term_recursive(5))

print(convert_to_base_10("01011110"))
print(convert_to_base_10("00100100"))
print(convert_to_base_10("11100011"))
print(convert_to_base_10("10011111"))
print(convert_to_base_10("10000111"))

print(convert_to_base_2(12))
print(convert_to_base_2(48))
print(convert_to_base_2(45))
print(convert_to_base_2(7))
print(convert_to_base_2(38))
