from itertools import zip_longest
from unittest import TestCase

from mame_nlp.batch import batch_by_slice


class TestBatch(TestCase):
    def test_batch_by_slice_negative(self):
        data = list(range(10))
        with self.assertRaises(AssertionError):
            list(batch_by_slice(data, -3))

    def test_batch_by_slice_list_drop_last(self):
        data = list(range(10))
        reference = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        ]
        iterator = zip_longest(
            batch_by_slice(data, 3, drop_last=True),
            reference,
        )
        for actual, ref in iterator:
            self.assertEqual(actual, ref)

    def test_batch_by_slice_list_no_drop_last(self):
        data = list(range(10))
        reference = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
            [9],
        ]
        iterator = zip_longest(
            batch_by_slice(data, 3, drop_last=False),
            reference,
        )
        for actual, ref in iterator:
            self.assertEqual(actual, ref)

    def test_batch_by_slice_list_batch_size_multiple(self):
        data = list(range(9))
        reference = [
            [0, 1, 2],
            [3, 4, 5],
            [6, 7, 8],
        ]
        iterator = zip_longest(
            batch_by_slice(data, 3, drop_last=True),
            reference,
        )
        for actual, ref in iterator:
            self.assertEqual(actual, ref)

        iterator = zip_longest(
            batch_by_slice(data, 3, drop_last=False),
            reference,
        )
        for actual, ref in iterator:
            self.assertEqual(actual, ref)
