import unittest
from src import cso
import random


class ShiftTest(unittest.TestCase):
    def setUp(self):
        self.shifts = []
        for i in range(10):
            new_shift = cso.Shift(i, 5)
            self.shifts.append(new_shift)

    def test_ids(self):
        seen = set()
        for shift in self.shifts:
            self.assertNotIn(shift.get_id(), seen)
            seen.add(shift.get_id())


class WorkerTest(unittest.TestCase):
    def setUp(self):
        self.workers = []
        for i in range(10):
            # random preferences
            new_worker = cso.Worker(i, 5, 0, random.sample(range(10), 4),
                                    random.sample(range(10), 4))
            self.workers.append(new_worker)

    def test_get_preferences(self):
        for worker in self.workers:
            available = set(range(10))
            for job in worker.get_preferences():
                self.assertIn(job, available)
                available.remove(job)
