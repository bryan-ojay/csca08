from a2 import *
import unittest


class TestSetByPos(unittest.TestCase):

    def test_00_no_print_function(self):
        subject = Female('test_subject')
        self.assertFalse('print' in subject.set_by_pos.__code__.co_names,
                         'print() function found in set_by_pos()')

    def test_01a_set_returns_none(self):
        subject = Female('test_subject')
        # try setting by position
        result = subject.set_by_pos(0, 5, 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_pos shouldn't be returning anything")

    def test_01b_set_returns_none(self):
        subject = Female('test_subject')
        # try setting by position
        result = subject.set_by_pos(12, 5, 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_pos shouldn't be returning anything")

    def test_01c_set_returns_none(self):
        subject = Female('test_subject')
        # try setting by position
        result = subject.set_by_pos(22, 5, 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_pos shouldn't be returning anything")


class TestGetByPos(unittest.TestCase):

    def test_00_no_print_function(self):
        subject = Female('test_subject')
        self.assertFalse('print' in subject.get_by_pos.__code__.co_names,
                         'print() function found in get_by_pos()')

    def test_01_get_returns_nucleotide(self):
        subject = Female('test_subject')
        # try setting by position
        subject.set_by_pos(0, 5, 'AT')
        result = subject.get_by_pos(0, 5)
        expected = 'AT'
        self.assertEqual(result, expected,
                         "get_by_pos did not return the nucleotide")

    def test_01b_get_returns_nucleotide(self):
        subject = Female('test_subject')
        # try setting by position
        subject.set_by_pos(12, 5, 'AT')
        result = subject.get_by_pos(12, 5)
        expected = 'AT'
        self.assertEqual(result, expected,
                         "get_by_pos did not return the nucleotide")

    def test_01c_get_returns_nucleotide(self):
        subject = Female('test_subject')
        # try setting by position
        subject.set_by_pos(22, 5, 'AT')
        result = subject.get_by_pos(22, 5)
        expected = 'AT'
        self.assertEqual(result, expected,
                         "get_by_pos did not return the nucleotide")


class TestSetMarker(unittest.TestCase):

    def test_00_no_print_function(self):
        subject = Female('test_subject')
        self.assertFalse('print' in subject.set_marker.__code__.co_names,
                         'print() function found in set_marker()')

    def test_01_set_marker_returns_none(self):
        subject = Female('test_subject')
        # try setting by marker
        result = subject.set_marker('marker', 0, 5)
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_marker shouldn't be returning anything")

    def test_01b_set_marker_returns_none(self):
        subject = Female('test_subject')
        # try setting by marker
        result = subject.set_marker('marker', 12, 5)
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_marker shouldn't be returning anything")

    def test_01c_set_marker_returns_none(self):
        subject = Female('test_subject')
        # try setting by marker
        result = subject.set_marker('marker', 22, 5)
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_marker shouldn't be returning anything")


class TestGetByMarker(unittest.TestCase):

    def test_00_no_print_function(self):
        subject = Female('test_subject')
        self.assertFalse('print' in subject.set_by_pos.__code__.co_names,
                         'print() function found in get_by_marker()')

    def test_01_get_by_marker_returns_nucleotide(self):
        subject = Female('test_subject')
        # set position and marker at position
        subject.set_by_pos(1, 5, 'AT')
        subject.set_marker('marker', 1, 5)
        result = subject.get_by_marker('marker')
        expected = 'AT'
        self.assertEqual(result, expected,
                         "get_by_marker did not return the correct nucleotide")


class TestSetByMarker(unittest.TestCase):

    def test_00_no_print_function(self):
        jill = Female('test_subject')
        self.assertTrue('set_by_pos' in jill.set_by_marker.__code__.co_names,
                        'set_by_pos function not found in set_by_marker')

    def test_01a_set_by_marker_returns_none(self):
        subject = Female('test_subject')
        # try setting by marker
        subject.set_marker('marker', 0, 5)
        result = subject.set_by_marker('marker', 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_marker shouldn't be returning anything")

    def test_01b_set_by_marker_returns_none(self):
        subject = Female('test_subject')
        # try setting by marker
        subject.set_marker('marker', 12, 5)
        result = subject.set_by_marker('marker', 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_marker shouldn't be returning anything")

    def test_01c_set_by_marker_returns_none(self):
        subject = Female('test_subject')
        # try setting by marker
        subject.set_marker('marker', 22, 5)
        result = subject.set_by_marker('marker', 'AT')
        # if we got this far, we know it at least didn't crash
        # now also check that it's not returning anything
        expected = None
        self.assertEqual(result, expected,
                         "set_by_marker shouldn't be returning anything")

    def test_02_set_by_marker_correct_set(self):
        subject = Female('test_subject')
        # try setting by marker
        subject.set_marker('marker', 1, 5)
        subject.set_by_marker('marker', 'AT')
        result = subject.get_by_marker('marker')
        # check if the nucleotide was set at the correct position
        expected = 'AT'
        self.assertEqual(result, expected,
                         "set_by_marker does not set the nucleotide correctly")

if(__name__ == "__main__"):
    unittest.main(exit=False)
