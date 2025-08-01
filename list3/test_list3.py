import unittest
import list3


class TestList1(unittest.TestCase):
    def test_bitstring_hamming_1(self):
        b = "110"
        n = 2
        self.assertCountEqual(list3.bitstring_hamming(b, n),['000', '011', '101'])

    def test_bitstring_hamming_n_equal_1(self):
        b = "101"
        n = 1
        self.assertCountEqual(list3.bitstring_hamming(b, n),['001', '100', '111'])

    def test_bitstring_hamming_b_empty(self):
        b = ""
        n = 2
        self.assertCountEqual(list3.bitstring_hamming(b, n),[""])

    def test_bitstring_hamming_n_equal_0(self):
        b = "101"
        n = 0
        self.assertCountEqual(list3.bitstring_hamming(b, n),['101']) 

    def test_bitstring_hamming_b_only_1(self):
        b = "1111"
        n = 2
        self.assertCountEqual(list3.bitstring_hamming(b, n),['0011', '0101', '0110', '1001', '1010', '1100'])

    def test_bitstring_hamming_n_length_b(self):
        b = "101"
        n = len(b)
        self.assertCountEqual(list3.bitstring_hamming(b, n),['010'])

    def test_levenshtein_1(self):
        x = "abc"
        y = "ebx"
        self.assertEqual(list3.levenshtein(x, y),2)

    def test_levenshtein_the_same_strings(self):
        x = "abc"
        y = "abc"
        self.assertEqual(list3.levenshtein(x, y),0)

    def test_levenshtein_completly_different(self):
        x = "abcd"
        y = "efgh"
        self.assertEqual(list3.levenshtein(x, y),4) 

    def test_levenshtein_different_length(self):
        x = "abcd"
        y = "abc"
        self.assertEqual(list3.levenshtein(x, y),1)

    def test_levenshtein_empty(self):
        x = ""
        y = "abc"
        self.assertEqual(list3.levenshtein(x, y),3)

    def test_set_jaccard_1(self):
        x = {1, 2, 3}
        y = {3, 4, 5}   
        self.assertAlmostEqual(list3.set_jaccard(x, y), 0.2)

    def test_set_jaccard_one_empty(self):
        x = set()
        y = {3, 4, 5}   
        self.assertAlmostEqual(list3.set_jaccard(x, y), 0)

    def test_set_jaccard_both_empty(self):
        x = set()
        y = set()   
        with self.assertRaises(ValueError):
            list3.set_jaccard(x, y)

    def test_set_jaccard_the_same(self):
        x = {3, 4, 5}
        y = {3, 4, 5}   
        self.assertAlmostEqual(list3.set_jaccard(x, y), 1)

    def test_set_jaccard_different(self):
        x = {0, 1, 2}
        y = {3, 4, 5}   
        self.assertAlmostEqual(list3.set_jaccard(x, y), 0) 

    def test_set_jaccard_2(self):
        x = {1, 2, 2}
        y = {2, 3, 4}   
        self.assertAlmostEqual(list3.set_jaccard(x, y), 0.25)

    def test_set_jaccard_different_len(self):
        x = {1, 2, 2, 4}
        y = {2, 2, 4}  
        self.assertAlmostEqual(list3.set_jaccard(x, y), 2/3)    


    def test_bag_jaccard_1(self):
        x = '1 2 3'
        y = '3 4 5'
        self.assertAlmostEqual(list3.bag_jaccard(x, y), 1/5)

    def test_bag_jaccard_one_empty(self):
        x = ""
        y = "3 4 5"   
        self.assertAlmostEqual(list3.bag_jaccard(x, y), 0)

    def test_bag_jaccard_both_empty(self):
        x = ""
        y = "" 
        with self.assertRaises(ValueError):
            list3.bag_jaccard(x, y)

    def test_bag_jaccard_the_same(self):
        x = "3 4 5"
        y = "3 4 5"    
        self.assertAlmostEqual(list3.bag_jaccard(x, y), 1)

    def test_bag_jaccard_different(self):
        x = "0 1 2"
        y = "3 4 5"  
        self.assertAlmostEqual(list3.bag_jaccard(x, y), 0) 

    def test_bag_jaccard_2(self):
        x = "1 2 2"
        y = "2 2 4"  
        self.assertAlmostEqual(list3.bag_jaccard(x, y), 1/2)

    def test_bag_jaccard_different_len(self):
        x = "1 2 2 4"
        y = "2 2 4"  
        self.assertAlmostEqual(list3.bag_jaccard(x, y), 3/4)     


    def test_shingles_1(self):
        s = 'abcd'
        k = 2 
        self.assertCountEqual(list3.shingles(s, k), ['ab', 'bc', 'cd'])

    def test_shingles_k_0(self):
        s = 'abcd'
        k = 0 
        self.assertCountEqual(list3.shingles(s, k), []) 

    def test_shingles_k_length_s(self):
        s = 'abcd'
        k = len(s)
        self.assertCountEqual(list3.shingles(s, k), ['abcd'])

    def test_shingles_k_length_s(self):
        s = ''
        k = 2
        self.assertCountEqual(list3.shingles(s, k), [])

    def test_diameter_1(self):
        S = ["abcde", "abeab","axqwf"]
        d=list3.levenshtein
        self.assertEqual(list3.diameter(S, d), 4)

    def test_diameter_empty_S(self):
        S = set()
        d=list3.levenshtein
        self.assertEqual(list3.diameter(S, d), 0)

    def test_diameter_one_element_in_S(self):
        S = ["abcde"]
        d=list3.levenshtein
        self.assertEqual(list3.diameter(S, d), 0)

    def test_diameter_same_elements_in_S(self):
        S = ["abcde","abcde"]
        d=list3.levenshtein
        self.assertEqual(list3.diameter(S, d), 0)                                                      
                                              

                                             

if __name__ == '__main__':
    unittest.main()