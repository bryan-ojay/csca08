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

    def test_02a_invalid_pair_1(self):
        subject = Female('test_subject')
        # try setting an out of bounds pair (too high), see if it crashes
        with self.assertRaises(Exception):
            subject.set_by_pos(23, 29, 'AG')

    def test_02b_invalid_pair_2(self):
        subject = Female('test_subject')
        # try setting an out of bounds pair (too low), see if it crashes
        with self.assertRaises(Exception):
            subject.set_by_pos(-4, 29, 'AG')

    def test_03_invalid_position(self):
        subject = Female('test_subject')
        # try setting an invalid position, see if it crashes
        with self.assertRaises(Exception):
            subject.set_by_pos(10, -5, 'CC')

    def test_04a_invalid_nucleotide_1(self):
        subject = Female('test_subject')
        # try setting a nucleotide pair with invalid codons, see if it crashes
        with self.assertRaises(Exception):
            subject.set_by_pos(10, 29, 'XX')

    def test_04b_invalid_nucleotide_2(self):
        subject = Female('test_subject')
        # try setting an nucleotide with length 1, see if it crashes
        with self.assertRaises(Exception):
            subject.set_by_pos(10, 29, 'C')

    def test_04c_invalid_nucleotide_3(self):
        subject = Female('test_subject')
        # try setting an nucleotide with length 4, see if it crashes
        with self.assertRaises(Exception):
            subject.set_by_pos(10, 29, 'ACAC')


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

    def test_02_get_unknown_nucleotide(self):
        subject = Female('test_subject')
        # Try getting from an unset position, see if it crashes
        with self.assertRaises(Exception):
            result = subject.get_by_pos(1, 10)

    def test_03a_invalid_pair_1(self):
        subject = Female('test_subject')
        subject.set_by_pos(1, 5, 'AT')
        # try getting from an out of bounds pair (too high), see if it crashes
        with self.assertRaises(Exception):
            result = subject.get_by_pos(23, 29)

    def test_03b_invalid_pair_2(self):
        subject = Female('test_subject')
        subject.set_by_pos(1, 5, 'AT')
        # try getting from an out of bounds pair (too high), see if it crashes
        with self.assertRaises(Exception):
            result = subject.get_by_pos(27, 29)


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

    def test_02a_invalid_pair_1(self):
        subject = Female('test_subject')
        # try setting an out of bounds pair (too high), see if it crashes
        with self.assertRaises(Exception):
            result = subject.set_marker('marker-2', 23, 2)

    def test_02b_invalid_pair_1(self):
        subject = Female('test_subject')
        # try setting an out of bounds pair (too high), see if it crashes
        with self.assertRaises(Exception):
            result = subject.set_marker('marker-2', 99, 2)


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

    def test_02_get_by_marker_unknown_nucleotide(self):
        subject = Female('test_subject')
        subject.set_marker('marker', 1, 5)
        # Try getting from an unset position, see if it crashes
        with self.assertRaises(Exception):
            result = subject.get_by_marker('marker')

    def test_02b_get_by_marker_unknown_nucleotide(self):
        subject = Female('test_subject')
        subject.set_marker('marker', 12, 5)
        # Try getting from an unset position, see if it crashes
        with self.assertRaises(Exception):
            result = subject.get_by_marker('marker')

    def test_02b_get_by_marker_unknown_nucleotide(self):
        subject = Female('test_subject')
        subject.set_marker('marker', 22, 5)
        # Try getting from an unset position, see if it crashes
        with self.assertRaises(Exception):
            result = subject.get_by_marker('marker')

    def test_03_get_by_marker_invalid_marker(self):
        subject = Female('test_subject')
        subject.set_by_pos(1, 5, 'AT')
        subject.set_marker('marker', 1, 5)
        # try getting from an unnamed marker, see if it crashes
        with self.assertRaises(Exception):
            result = subject.get_by_marker('invalid-marker')


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

    def test_03a_sbm_invalid_nucleotide_1(self):
        subject = Female('test_subject')
        # try setting a nucleotide pair with invalid codons, see if it crashes
        subject.set_marker('marker', 1, 5)
        with self.assertRaises(Exception):
            subject.set_by_marker('marker', 'XX')

    def test_03b_sbm_invalid_nucleotide_2(self):
        subject = Female('test_subject')
        # try setting an nucleotide with length 1, see if it crashes
        subject.set_marker('marker', 1, 5)
        with self.assertRaises(Exception):
            subject.set_by_marker('marker', 'C')

    def test_03c_sbm_invalid_nucleotide_3(self):
        subject = Female('test_subject')
        # try setting an nucleotide with length 4, see if it crashes
        subject.set_marker('marker', 1, 5)
        with self.assertRaises(Exception):
            subject.set_by_marker('marker', 'ACAC')

    def test_04_sbm_invalid_marker(self):
        subject = Female('test_subject')
        subject.set_marker('marker', 1, 5)
        with self.assertRaises(Exception):
            subject.set_by_marker('invalid-marker', 'AC')

    def test_04b_sbm_invalid_marker(self):
        subject = Female('test_subject')
        subject.set_marker('marker', 12, 5)
        with self.assertRaises(Exception):
            subject.set_by_marker('invalid-marker', 'C')

if(__name__ == "__main__"):
    unittest.main(exit=False)
