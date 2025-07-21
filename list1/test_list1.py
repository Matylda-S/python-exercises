# -*- coding: utf-8 -*-


import unittest
import list1


class TestList1(unittest.TestCase):
    def test_cosine_1(self):
        v1 = [1, 2, 3]
        v2 = [0, 1, 0]
        self.assertAlmostEqual(list1.cosine(v1, v2), 57.68846676257615)

    def test_cosine_vector_of_length_0(self):
        v1 = [1, 1]
        v2 = [0, 0]
        self.assertAlmostEqual(list1.cosine(v1, v2), 0.0)

    def test_cosine_negative(self):
        v1 = [1, 1]
        v2 = [-2, 3]
        self.assertAlmostEqual(list1.cosine(v1, v2), 78.69006752597979)

    def test_divisible_in_range_1(self):
        a=1
        b=10
        c=3
        self.assertEqual(list1.divisible_in_range(a, b, c), [3, 6, 9])

    def test_divisible_in_range_negative_d(self):
        a=0
        b=10
        c=-2
        self.assertEqual(list1.divisible_in_range(a, b, c), [0,2,4,6,8,10])
        
    def test_divisible_in_range_dividing_by_0(self):
        a=0
        b=10
        c=0
        self.assertEqual(list1.divisible_in_range(a, b, c), [])

    def test_common_elements_1(self):
        x = [1, 2, 3, 4, 5]
        y = [6, 7, 8, 2, 3]
        self.assertEqual(list1.common_elements(x, y), [2, 3])

    def test_common_elements_empty_list(self):
        x = []
        y = [4, 5, 6, 7, 8]
        self.assertEqual(list1.common_elements(x, y), [])

    def test_common_elements_no_common_elements(self):
        x = [1, 2, 3]
        y = [4, 5, 6]
        self.assertEqual(list1.common_elements(x, y), [])

    def test_common_elements_different_size(self):
        x = [1, 2, 3]
        y = [4, 5, 6, 1, 2]
        self.assertEqual(list1.common_elements(x, y), [1,2])    

    def test_exclude_1(self):
        letter = 'a'
        string = 'anaconda'
        self.assertEqual(list1.exclude(letter, string), 'ncond')

    def test_exclude_no_occurrences(self):
        letter = 'x'
        string = 'anaconda'
        self.assertEqual(list1.exclude(letter, string), 'anaconda')

    def test_exclude_empty(self):
        letter = 'x'
        string = ''
        self.assertEqual(list1.exclude(letter, string), '')

    def test_exclude_no_letters(self):
        letter = ''
        string = 'anaconda'
        self.assertEqual(list1.exclude(letter, string), 'anaconda')

    def test_exclude_no_different_letters(self):
        letter = 'a'
        string = 'aaaaa'
        self.assertEqual(list1.exclude(letter, string), '')  

    def test_letters_and_digits_1(self):
        s = "abc123x24n"
        self.assertEqual(list1.letters_and_digits(s), (5, 5))

    def test_letters_and_digits_s_is_empty(self):
        s = ""
        self.assertEqual(list1.letters_and_digits(s), (0,0))
        
    def test_letters_and_digits_only_letters(self):
        s = "abc"
        self.assertEqual(list1.letters_and_digits(s), (3,0))

    def test_letters_and_digits_only_numbers(self):
        s = "123"
        self.assertEqual(list1.letters_and_digits(s), (0,3))    
        
    def test_subsets_1(self):
        x = {'a', 'b', 'c', 'd'}
        exp_result = [
    set(),  # Pusty zbiór {}
    {'a'},
    {'b'},
    {'c'},
    {'d'},
    {'a', 'b'},
    {'a', 'c'},
    {'a', 'd'},
    {'b', 'c'},
    {'b', 'd'},
    {'c', 'd'},
    {'a', 'b', 'c'},
    {'a', 'b', 'd'},
    {'a', 'c', 'd'},
    {'b', 'c', 'd'},
    {'a', 'b', 'c', 'd'}, 
]

        self.assertSetEqual(set(map(frozenset, list1.subsets(x))), set(map(frozenset, exp_result)))
      

    def test_subsets_set_is_empty(self):
        x = ''
        self.assertEqual(list1.subsets(x), [set()])

    def test_subsets_one_element(self):
        x = {'a'} 
        self.assertEqual(set(map(frozenset, list1.subsets(x))), set(map(frozenset,[set(),{'a'}])))  

    def test_dec_to_bin_1(self):
        x = 10
        self.assertEqual(list1.dec_to_bin(x), "1010")
    
    def test_dec_to_bin_0(self):
        x = 0
        self.assertEqual(list1.dec_to_bin(x), '0')

    def test_dec_to_bin_negative_num(self):
        x = -10
        self.assertEqual(list1.dec_to_bin(x), "Invalid input")
    
    def test_dec_to_bin_huge_num(self):
        x = 123456789
        self.assertEqual(list1.dec_to_bin(x), "111010110111100110100010101")   

    def test_mode_1(self):
        s = "ala"
        self.assertEqual(list1.mode(s), "a")

    def test_mode_s_is_empty(self):
        s = ""
        self.assertEqual(list1.mode(s), "")

    def test_mode_same_frequency(self):
        s = "alla"
        self.assertEqual(list1.mode(s), "a")  

    def test_non_negative_1(self):
        x = [1, -2, 3, 4, -5, -10]
        self.assertEqual(list1.non_negative(x), [1, 3, 4])

    def test_non_negative_0(self):
        x = [-1, 0, 5, 2]
        self.assertEqual(list1.non_negative(x), [0, 5, 2])

    def test_non_negative_empty(self):
        x = []
        self.assertEqual(list1.non_negative(x), [])

    def test_non_negative_only_negative(self):
        x = [-2, -1, -10]
        self.assertEqual(list1.non_negative(x), [])  

    def test_no_longer_than_1(self):
        threshold = 3
        x = ["a", "ab", "abcd", "abcdef"]
        self.assertEqual(list1.no_longer_than(threshold, x), ["a","ab"])

    def test_no_longer_than_the_same_length(self):
        threshold = 3
        x = ["a", "abc", "abcd", "abcdef"]
        self.assertEqual(list1.no_longer_than(threshold, x),["a","abc"])
        
    def test_no_longer_than_every_longer(self):
        threshold = 3
        x = ["abcdefs", "abcccc", "abcd", "abcdef"]
        self.assertEqual(list1.no_longer_than(threshold, x),[])

    def test_no_longer_than_empty(self):
        threshold = 3
        x = []
        self.assertEqual(list1.no_longer_than(threshold, x),[]) 

    def test_max_string_1(self):
       x = ["a", "abcdef", "abcd", "abcde"]
       self.assertEqual(list1.max_string(x), "abcdef")

    def test_max_string_same_length(self):
        x = ["a", "abcdef", "abcd", "abcdex"]
        self.assertEqual(list1.max_string(x), "abcdef")

    def test_max_string_x_is_empty(self):
        x = []
        self.assertEqual(list1.max_string(x), "")    

    def test_alternate_1(self):
        a=["a1","a2","a3"]
        b=["b1","b2","b3"]
        self.assertEqual(list1.alternate(a, b), ["a1","b1","a2","b2","a3","b3"])

    def test_alternate_different_types(self):
        a=["a","aba","baba","alaa"]
        b=[1,2,3,4]
        self.assertEqual(list1.alternate(a, b), ["a",1,"aba",2,"baba",3,"alaa",4])

    def test_alternate_different_length_of_lists(self):
        a=["a","aba","baba","alaa","a"]
        b=[1,2,3,4]
        self.assertEqual(list1.alternate(a, b), "the lists aren't of equal length")

    def test_alternate_empty_lists(self):
        a=[]
        b=[]
        self.assertEqual(list1.alternate(a, b), []) 

    def test_separate_and_sort_1(self):
        x = ['zz', 5, 2, 'a', 8, 'def']
        self.assertEqual(list1.separate_and_sort(x), ['a', 'def', 'zz', 2, 5, 8])

    def test_separate_and_sort_empty_list(self):
        x = []
        self.assertEqual(list1.separate_and_sort(x), [])

    def test_separate_and_sort_only_strings(self):
        x = ['abc', 'wrf', 'xyz']
        self.assertEqual(list1.separate_and_sort(x), ['abc', 'wrf', 'xyz'])

    def test_separate_and_sort_only_intigers(self):
        x = [10, 12, 1]
        self.assertEqual(list1.separate_and_sort(x), [1, 10, 12])

    def test_separate_and_sort_duplicates(self):
        x = ['zz', 5, 2, 'a', 8, 'def',2,'zz']
        self.assertEqual(list1.separate_and_sort(x), ['a', 'def', 'zz','zz', 2,2, 5, 8])                                       
            
           

if __name__ == '__main__':
    unittest.main()