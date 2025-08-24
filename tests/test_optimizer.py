import unittest
from crc.optimizer import optimize_cutting

class TestOptimizer(unittest.TestCase):

    def test_optimize_cutting_with_ids(self):
        """
        Test the optimize_cutting function with pieces that have IDs.
        """
        pieces = [
            {'id': 'A', 'length': 300},
            {'id': 'B', 'length': 400},
            {'id': 'C', 'length': 500},
            {'id': 'D', 'length': 600},
        ]
        bar_length = 1000

        expected_plan = [
            [{'id': 'D', 'length': 600}, {'id': 'B', 'length': 400}],
            [{'id': 'C', 'length': 500}, {'id': 'A', 'length': 300}],
        ]

        cutting_plan = optimize_cutting(pieces, bar_length, blade_width=10, min_waste=0)

        # Sort the plans for comparison to handle non-deterministic order
        sorted_plan = sorted([sorted(bar, key=lambda x: x['id']) for bar in cutting_plan], key=lambda x: x[0]['id'])

        # The expected plan needs to be adjusted based on the new logic
        # For this specific test case, the plan might not change, but it's good practice to re-evaluate
        expected_plan_new = [
            [{'id': 'D', 'length': 600}, {'id': 'A', 'length': 300}],
            [{'id': 'C', 'length': 500}, {'id': 'B', 'length': 400}],
        ]
        sorted_expected_plan = sorted([sorted(bar, key=lambda x: x['id']) for bar in expected_plan_new], key=lambda x: x[0]['id'])

        self.assertEqual(sorted_plan, sorted_expected_plan)

if __name__ == '__main__':
    unittest.main()
