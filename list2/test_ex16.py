import unittest
from ex16 import encode, decode


class TestList1(unittest.TestCase):
    def test_encode_1(self):
        s="abc"
        d=3
        self.assertAlmostEqual(encode(s, d), "def")

    def test_encode_Upperletter(self):
        s="ABC"
        d=3
        self.assertAlmostEqual(encode(s, d), "DEF")

    def test_encode_Upperandlowerletter(self):
        s="AbC"
        d=3
        self.assertAlmostEqual(encode(s, d), "DeF")    

    def test_encode_0shift(self):
        s="abc"
        d=0
        self.assertAlmostEqual(encode(s, d), "abc")

    def test_encode_punktuation(self):
        s="abc."
        d=3
        self.assertAlmostEqual(encode(s, d), "def.")    

    def test_encode_shiftover26(self):
        s="abc"
        d=28
        self.assertAlmostEqual(encode(s, d), "cde")  

    def test_decode_1(self):
        s="def"
        d=3
        self.assertAlmostEqual(decode(s, d), "abc")

    def test_decode_Upperletter(self):
        s="DEF"
        d=3
        self.assertAlmostEqual(decode(s, d), "ABC")

    def test_decode_Upperandlowerletter(self):
        s="DeF"
        d=3
        self.assertAlmostEqual(decode(s, d), "AbC")    

    def test_decode_0shift(self):
        s="abc"
        d=0
        self.assertAlmostEqual(decode(s, d), "abc")

    def test_decode_shiftover26(self):
        s="cde"
        d=28
        self.assertAlmostEqual(decode(s, d), "abc")

    def test_decode_punktuation(self):
        s="def."
        d=3
        self.assertAlmostEqual(decode(s, d), "abc.")    


if __name__ == '__main__':
    unittest.main()               

