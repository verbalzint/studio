import unittest
from brightics.common.datasets import load_iris
from brightics.function.timeseries import autocorrelation


class TestAutoCorrelation(unittest.TestCase):

    def setUp(self):
        print("*** AutoCorrelation UnitTest Start ***")
        self.iris = load_iris()

    def tearDown(self):
        print("*** AutoCorrelation UnitTest End ***")

    def test_autocorrelation(self):
        input_dataframe = self.iris
        
        res = autocorrelation(table=input_dataframe, input_col='sepal_length')['model']
        res_autocorrelation=res['autocorrelation_table']
        res_partial_autocorrelation=res['partial_autocorrelation_table']
        
        
        print("Autocorrelation Table\n", res_autocorrelation.values)
        
        print("Partial Autocorrelation Table\n", res_partial_autocorrelation.values)
        
        table1=res_autocorrelation.values.tolist()
        table2=res_partial_autocorrelation.values.tolist()
        self.assertListEqual(table1[1], [1, 0.5920665785767498, '(0.4320361893649062, 0.7520969677885935)'])
        self.assertListEqual(table1[19], [19, 0.3326828817365676, '(-0.15031337059372796, 0.8156791340668632)'])
        self.assertListEqual(table2[2], [2, 0.446878925378876, '(0.2868485361670323, 0.6069093145907197)'])
        self.assertListEqual(table2[18], [18, 0.057734494528377006, '(-0.10229589468346667, 0.21776488374022068)'])


if __name__ == '__main__':
    unittest.main()