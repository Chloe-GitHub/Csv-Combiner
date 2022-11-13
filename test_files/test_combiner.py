import unittest
import csv
from pathlib import Path

import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import csv_combiner 

class TestCombiner(unittest.TestCase):

    root = Path(__file__)
        
    def test_combiner_when_one_file(self):
        header_1 = ['name', 'area', 'country_code2', 'country_code3']
        data_1 =    [ 
            ['China', 1, 'AL', 'ALB'],
            ['America', 2, 'DZ', 'DZA'],
            ['Japan', 3, 'AS', 'ASM'],
            ['Mexico', 4, 'AD', 'AND'],
        ]
        header_2 = ['name', 'area', 'country_code2', 'country_code3', 'filename']
        data_2 =    [ 
            ['China', 1, 'AL', 'ALB', 'countries'],
            ['America', 2, 'DZ', 'DZA', 'countries'],
            ['Japan', 3, 'AS', 'ASM', 'countries'],
            ['Mexico', 4, 'AD', 'AND', 'countries'],
        ]
        
        countries_file_path = 'fixtures/countries.csv'
        expect_file_path = 'fixtures/expected.csv'
        combined_file_path = 'fixtures/combined.csv'
        
        self.createTestFile(header_1, data_1, countries_file_path)
        self.createTestFile(header_2, data_2, expect_file_path)
           
        # Act
        csv_combiner.csv_combine(self.root, [countries_file_path])
        
        # Assert
        assert [row for row in open(expect_file_path)] == [row for row in open(combined_file_path)]
        
    def test_combiner_when_two_files(self):
        header_1 = ['name', 'area', 'country_code2', 'country_code3']
        data_1 =    [ 
            ['China', 1, 'AL', 'ALB'],
            ['America', 2, 'DZ', 'DZA'],

        ]
        header_2 = ['name', 'area', 'country_code2', 'country_code3']
        data_2 =    [ 
            ['Japan', 3, 'AS', 'ASM'],
            ['Mexico', 4, 'AD', 'AND'],
        ]
        header_3 = ['name', 'area', 'country_code2', 'country_code3', 'filename']
        data_3 =    [ 
            ['China', 1, 'AL', 'ALB', 'countries_1'],
            ['America', 2, 'DZ', 'DZA', 'countries_1'],
            ['Japan', 3, 'AS', 'ASM', 'countries_2'],
            ['Mexico', 4, 'AD', 'AND', 'countries_2'],
        ]
        
        countries_1_file_path = 'fixtures/countries_1.csv'
        countries_2_file_path = 'fixtures/countries_2.csv'
        expect_file_path = 'fixtures/expected.csv'
        combined_file_path = 'fixtures/combined.csv'
        
        self.createTestFile(header_1, data_1, countries_1_file_path)
        self.createTestFile(header_2, data_2, countries_2_file_path)
        self.createTestFile(header_3, data_3, expect_file_path)
           
        # Act
        csv_combiner.csv_combine(self.root, [countries_1_file_path, countries_2_file_path])
        
        # Assert
        assert [row for row in open(expect_file_path)] == [row for row in open(combined_file_path)]
        
    def test_combiner_when_three_files(self):
        header_1 = ['name', 'area', 'country_code2', 'country_code3']
        data_1 =    [ 
            ['China', 1, 'AL', 'ALB'],
            ['America', 2, 'DZ', 'DZA'],

        ]
        header_2 = ['name', 'area', 'country_code2', 'country_code3']
        data_2 =    [ 
            ['Japan', 3, 'AS', 'ASM'],
            ['Mexico', 4, 'AD', 'AND']
        ]
        header_3 = ['name', 'area', 'country_code2', 'country_code3']
        data_3 =    [ 
            ['Iceland', 5, 'AB', 'ABM'],
            ['UK', 6, 'SD', 'SDC']
        ]
        header_4 = ['name', 'area', 'country_code2', 'country_code3', 'filename']
        data_4 =    [ 
            ['China', 1, 'AL', 'ALB', 'countries_1'],
            ['America', 2, 'DZ', 'DZA', 'countries_1'],
            ['Japan', 3, 'AS', 'ASM', 'countries_2'],
            ['Mexico', 4, 'AD', 'AND', 'countries_2'],
            ['Iceland', 5, 'AB', 'ABM', 'countries_3'],
            ['UK', 6, 'SD', 'SDC', 'countries_3']
        ]
        
        countries_1_file_path = 'fixtures/countries_1.csv'
        countries_2_file_path = 'fixtures/countries_2.csv'
        countries_3_file_path = 'fixtures/countries_3.csv'
        expect_file_path = 'fixtures/expected.csv'
        combined_file_path = 'fixtures/combined.csv'
        
        self.createTestFile(header_1, data_1, countries_1_file_path)
        self.createTestFile(header_2, data_2, countries_2_file_path)
        self.createTestFile(header_3, data_3, countries_3_file_path)
        self.createTestFile(header_4, data_4, expect_file_path)
           
        # Act
        csv_combiner.csv_combine(self.root, [countries_1_file_path,countries_2_file_path, countries_3_file_path])
        
        # Assert
        assert [row for row in open(expect_file_path)] == [row for row in open(combined_file_path)]
        
    
    
    def createTestFile(self, header, data, file_path):
        with open(file_path, 'w+', encoding='UTF8', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(header)
            writer.writerows(data)

t = TestCombiner()
t.test_combiner_when_one_file()
t.test_combiner_when_two_files()
t.test_combiner_when_three_files()

    