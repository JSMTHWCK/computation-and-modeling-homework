from code import *


if check_for_symmetry('tacocat') != True:
  print('check_for_symmetry failed on input "tacocat"')
if check_for_symmetry('pinapple') != False:
	print('check_for_symmetry failed on input "pinapple"')

if convert_to_numbers('tacocat') != [20,1,3,15,3,1,20]:
	print('convert_to_numbers failed on input "tacocat"')


if convert_to_numbers('pinapple') != [16,9,14,1,16,16,12,5]:
	print('convert_to_numbers failed on input "pinapple"')

if is_prime(20) != False:
	print('is_prime failed on input "20"')


if is_prime(86) != False:
	print('is_prime failed on input "86"')

if get_intersection([1,3,5,7,8],[2,4,6,8,7]) !=  [7,8]:
	print('get_intersection failed on input "[1,3,5,7,8],[2,4,6,8,7]"')

if get_intersection([78,83,21,99],[43,16,45,58]) !=  []:
	print('get_intersection failed on input "[78,83,21,99],[43,16,45,58]"')

if get_union([1,3,5,7,8],[2,4,6,8,7]) != [1,3,5,7,8,2,4,6]:
	print('get_union failed on input "[1,3,5,7,8],[2,4,6,8,7]"')

if get_union([78,83,21,99],[43,16,45,58]) != [78,83,21,99,43,16,45,58]:
	print('get_union failed on input "[78,83,21,99],[43,16,45,58]"')

if count_characters("tacocat") != {'t': 2, 'a': 2, 'c': 2, 'o': 1}:
	print('count_characters failed on input "tacocat"')


if count_characters("pinapple") != {'p': 3, 'i': 1, 'n': 1, 'a': 1, 'l': 1, 'e':1}:
	print('count_characters failed on input "pinapple"')

if get_first_n_terms_nonrecursive(3) !=[5,11,29]:
	print('get_first_n_terms_nonrecursive failed on input "3"')

if get_first_n_terms_nonrecursive(5) !=[5,11,29,83,245]:
	print('get_first_n_terms_nonrecursive failed on input "5"')

if get_nth_term_recursive(3) != 29:
	print('get_nth_term_recursive failed on input 3')

if get_nth_term_recursive(5) !=245:
	print('get_nth_term_recursive failed on input 5')

if convert_to_base_10("01011110") != 94:
	print('convert_to_base_10 failed on input "01011110"')

if convert_to_base_10("00100100") != 36:
	print('convert_to_base_10 failed on input "00100100"')

if convert_to_base_2(12) != 1100:
	print('convert_to_base_2 failed on input "12"')
if convert_to_base_2(48) != 110000:
	print('convert_to_base_2 failed on input "48"')
