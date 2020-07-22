import unittest
from src import network_flow, cso


class SimpleFlowTest(unittest.TestCase):
    def setUp(self):
        self.simple_network = network_flow.ScheduleNetwork()

    def test_two_node(self):
        job = [cso.Shift(0, 5, 1)]
        worker = [cso.Worker(0, 10, 1, [0], [0])]
        self.simple_network.add_jobs(job)
        self.simple_network.add_workers(worker)
        res = self.simple_network.schedule()
        self.assertEqual(res['w0']['w0j0'], 1)
        self.assertEqual(res['w0j0']['j0'], 1)
