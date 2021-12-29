import unittest
import math

def division(a,b):
    return a/b
 
class testVolume(unittest.TestCase):
    def test_Nula(self):
        result = division(12,0)
        self.assertRaises(ZeroDivisionError,result,0), 
        #assertRaises(exc, fun, args, *kwds)
        
    def test_isString(self):
        result = int(division("12",7)) 
        self.assertRaises(TypeError,result,True) 
 
def suite():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(testVolume))
    return test_suite
 
 
mySuite=suite() 

runner=unittest.TextTestRunner()
runner.run(mySuite)