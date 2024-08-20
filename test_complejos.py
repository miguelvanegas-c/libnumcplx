import math
import libnumcplx as lc
import unittest
class TestLibnumcplx(unittest.TestCase):
    def test_sumaC(self):
        suma = lc.sumaC((2,3),(3,5))
        self.assertAlmostEqual(suma[0], 5)
        self.assertAlmostEqual(suma[1], 8)
        suma = lc.sumaC((2.8, 1.7), (-1, 5))
        self.assertAlmostEqual(suma[0], 1.8)
        self.assertAlmostEqual(suma[1], 6.7)

    def test_multiC(self):
        multi = lc.multiC((2,3),(3,5))
        self.assertAlmostEqual(multi[0], -9)
        self.assertAlmostEqual(multi[1], 19)
        multi = lc.multiC((2.8, 1.7), (-1, 5))
        self.assertAlmostEqual(multi[0], -11.3)
        self.assertAlmostEqual(multi[1], 12.3)

    def test_restaC(self):
        resta = lc.restaC((2, 3), (3, 5))
        self.assertAlmostEqual(resta[0], -1)
        self.assertAlmostEqual(resta[1], -2)
        resta = lc.restaC((2.8, 1.7), (-1, 5))
        self.assertAlmostEqual(resta[0], 3.8)
        self.assertAlmostEqual(resta[1], -3.3)

    def test_divisionC(self):
        division = lc.divisionC((2, 3), (3, 5))
        self.assertAlmostEqual(division[0],(21/34))
        self.assertAlmostEqual(division[1], (-1/34))
        division = lc.divisionC((2.8, 1.7), (-1, 5))
        self.assertAlmostEqual(division[0], (5.7/26))
        self.assertAlmostEqual(division[1], (-15.7/26))

    def test_moduloC(self):
        self.assertAlmostEqual(lc.moduloC((2, 3)), 13 ** (1 / 2))
        self.assertAlmostEqual(lc.moduloC((2.8, 1.7)), ((1073**(1/2))/10))

    def test_conjugadoC(self):
        self.assertAlmostEqual(lc.conjugadoC((2, 3)), (2, -3))
        self.assertAlmostEqual(lc.conjugadoC((2.8, 1.7)), (2.8, -1.7))

    def test_faseC(self):
        self.assertAlmostEqual(lc.faseC((2, 3)),math.atan2(2,3) )
        self.assertAlmostEqual(lc.faseC((2.8, 1.7)), math.atan2(2.8 ,1.7))

    def test_converC_P(self):
        conver = lc.converC_P((2,3))
        self.assertAlmostEqual(conver[0], 13 ** (1 / 2) )
        self.assertAlmostEqual(conver[1], math.atan2(2,3))
        conver = lc.converC_P((2.8, 1.7))
        self.assertAlmostEqual(conver[0], ((1073**(1/2))/10))
        self.assertAlmostEqual(conver[1], math.atan2(2.8, 1.7))

    def test_converP_C(self):
        conver = lc.converP_C((1,0.8))
        self.assertAlmostEqual(conver[0], math.cos(0.8))
        self.assertAlmostEqual(conver[1], math.sin(0.8))
        conver = lc.converP_C((2.8, 0.5))
        self.assertAlmostEqual(conver[0], 2.8 * math.cos(0.5))
        self.assertAlmostEqual(conver[1], 2.8 * math.sin(0.5))


if __name__ == '__main__':
    unittest.main()


