import unittest
import list4

class TestList4(unittest.TestCase):
    def test_gen_hash_1(self):
        s='1001'
        m=5
        self.assertAlmostEqual(list4.gen_hash(s,m), 4)

    def test_gen_hash_0_first(self):
        s='0001'
        m=5
        self.assertAlmostEqual(list4.gen_hash(s,m), 1)

    def test_gen_hash_1_same_result(self):
        s='1001'
        m=5
        self.assertAlmostEqual(list4.gen_hash(s,m), list4.gen_hash(s,m))

    def test_gen_hash_1_same_result_only_0(self):
        s='0000'
        m=5
        self.assertAlmostEqual(list4.gen_hash(s,m), list4.gen_hash(s,m))

    def test_gen_hash_1_same_result_only_1(self):
        s='1111'
        m=5
        self.assertAlmostEqual(list4.gen_hash(s,m), list4.gen_hash(s,m))        

    def test_gen_hash_m_equal_1(self):
        s='1001'
        m=1
        self.assertAlmostEqual(list4.gen_hash(s,m), 0)

    def test_gen_hash_m_equal_0(self):
        s='1001'
        m=0
        with self.assertRaises(ValueError):
            list4.gen_hash(s,m)

    def test_gen_hash_m_negative(self):
        s='1001'
        m=-2
        with self.assertRaises(ValueError):
            list4.gen_hash(s,m)

    def test_gen_hash_m_equal_2(self):
        s='1001'
        m=2
        self.assertIn(list4.gen_hash(s,m), [0, 1]) 

    def test_gen_hash_1_same_result_for_big_bitstirng(self):
        s='101010000010000100001000100010100101010101010101010101011111000010101'
        m=10
        self.assertAlmostEqual(list4.gen_hash(s,m), list4.gen_hash(s,m))

    def test_gen_hash_1_same_result_for_big_m(self):
        s='1010100000100001'
        m=1000
        self.assertAlmostEqual(list4.gen_hash(s,m), list4.gen_hash(s,m))

    def test_gen_hash_s_includes_letter(self):
        s='10a10v0'
        m=3
        with self.assertRaises(ValueError):
            list4.gen_hash(s,m)

    def test_gen_hash_s_not_bitstring(self):
        s='103401'
        m=3
        with self.assertRaises(ValueError):
            list4.gen_hash(s,m)  

    def test_minhash_bands_1(self):
        s=0.5
        n=100
        self.assertAlmostEqual(list4.minhash_bands(n,s), (21,4))

    def test_minhash_bands_n_lower_than_0(self):
        s=0.5
        n=-100
        with self.assertRaises(ValueError):
            list4.minhash_bands(n,s)  

    def test_minhash_bands_n_lower_equal_0(self):
        s=0.5
        n=0
        with self.assertRaises(ValueError):
            list4.minhash_bands(n,s)

    def test_minhash_bands_s_bigger_than_1(self):
        s=1.2
        n=100
        with self.assertRaises(ValueError):
            list4.minhash_bands(n,s)

    def test_minhash_bands_s_bigger_lower_than_0(self):
        s=-0.2
        n=100
        with self.assertRaises(ValueError):
            list4.minhash_bands(n,s)

    def test_minhash_bands_s_close_to_0(self):
        s=0.0001
        n=100
        self.assertAlmostEqual(list4.minhash_bands(n,s), (n,1)) 

    def test_minhash_bands_s_close_to_1(self):
        s=0.9999
        n=100
        self.assertAlmostEqual(list4.minhash_bands(n,s), (1,n))                                              
            
                                                    

if __name__ == '__main__':
    unittest.main()        