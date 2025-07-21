import unittest
import ex17


class TestList1(unittest.TestCase):
    def test_sortbyname_1(self):
        users = {
         "Harry": "Main Street",
         "Alex": "Garden Street",
         "James": "Knockturn Alley",
         "Suzan": "Diagon Alley",
         "Lily": "Great Peter Street"
}
        self.assertAlmostEqual(ex17.sortbyname(users), [('Alex', 'Garden Street'), ('Harry', 'Main Street'), ('James', 'Knockturn Alley'), ('Lily', 'Great Peter Street'), ('Suzan', 'Diagon Alley')])

    def test_sortbyname_empty_dict(self):
        users = {}
        self.assertAlmostEqual(ex17.sortbyname(users), [])

    def test_sortbyname_one_user(self):
        users = {
         "Harry": "Main Street"
        }
        self.assertAlmostEqual(ex17.sortbyname(users), [('Harry', 'Main Street')]) 

    def test_sortbyadress_1(self):
        users = {
         "Harry": "Main Street",
         "Alex": "Garden Street",
         "James": "Knockturn Alley",
         "Suzan": "Diagon Alley",
         "Lily": "Great Peter Street"
}
        self.assertAlmostEqual(ex17.sortbyadress(users),[('Suzan', 'Diagon Alley'), ('Alex', 'Garden Street'), ('Lily', 'Great Peter Street'), ('James', 'Knockturn Alley'), ('Harry', 'Main Street')])

    def test_sortbyadress_empty_dict(self):
        users = {}
        self.assertAlmostEqual(ex17.sortbyadress(users), [])

    def test_sortbyadress_one_user(self):
        users = {
         "Harry": "Main Street"
        }
        self.assertAlmostEqual(ex17.sortbyadress(users), [('Harry', 'Main Street')])    

if __name__ == '__main__':
    unittest.main()               

