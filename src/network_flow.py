import networkx


class ScheduleNetwork:
    def __init__(self):
        self.network = networkx.DiGraph()
        self.necessary_demand = 0
        self.necessary_supply = 0
        self.total = 0
        self.network.add_node('s')
        self.network.add_node('t')
        self.network.add_edge('s', 't')

    def add_workers(self, workers):
        for worker in workers:
            name = 'w' + str(worker.get_id())
            excess = worker.get_max_hours() - worker.get_min_hours()
            self.network.add_node(name, demand=-worker.get_min_hours())
            self.network.add_node('e' + name)
            self.network.add_edge('s', 'e' + name, weight=0, capacity=excess)
            self.add_edges(name, worker.get_qualifications(), worker.get_preferences())
            self.necessary_supply += worker.get_min_hours()
            self.total += worker.get_max_hours()

    def add_jobs(self, jobs):
        for job in jobs:
            name = 'j' + str(job.get_id())
            excess = job.get_max_workers() - job.get_min_workers()
            self.network.add_node(name, demand=job.get_min_workers())
            self.network.add_node('e' + name)
            self.network.add_edge('e' + name, 't', weight=0, capacity=excess)
            self.necessary_demand += job.get_min_workers()
            self.total += job.get_max_workers()

    def add_edges(self, name, constraints, preferences):
        for shift in constraints:
            shift_name = 'j' + str(shift)
            if shift in preferences:
                weight = -(len(preferences) - preferences.index(shift))
            else:
                weight = 0
            self.network.add_node(name+shift_name)
            self.network.add_edge(name, name+shift_name, weight=weight, capacity=1)
            self.network.add_edge(name+shift_name, 'e' + shift_name, weight=weight, capacity=1)
            self.network.add_edge('e' + name, name+shift_name, weight=weight, capacity=1)
            self.network.add_edge(name+shift_name, shift_name, weight=weight, capacity=1)

    def schedule(self):
        '''
        computes a MCNF
        rtype: dict of dicts
        '''
        diff = self.necessary_supply - self.necessary_demand
        self.network.nodes['s']['demand'] = -self.total
        self.network.nodes['t']['demand'] = self.total + diff
        return networkx.min_cost_flow(self.network)
