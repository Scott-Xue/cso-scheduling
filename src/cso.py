class Shift:
    def __init__(self, id, max_workers, min_workers=0):
        self.id = id
        self.min_workers = min_workers
        self.max_workers = max_workers

    def get_id(self):
        """Returns unique identifying key of this shift.
        rtype: int
        """
        return self.id

    def get_min_workers(self):
        """Returns the minimum number of workers required for this shift.
        Default is 0, essential shifts will specify min_workers.
        rtype: int
        """
        return self.min_workers

    def get_max_workers(self):
        """Returns capacity for workers for this shift.
        rtype: int
        """
        return self.max_workers


class Worker:
    def __init__(self, id, max_hours, min_hours, preferences, qualifications):
        self.id = id
        self.max_hours = max_hours
        self.min_hours = min_hours
        self.preferences = preferences
        self.qualifications = qualifications

    def get_id(self):
        return self.id

    def get_max_hours(self):
        """Returns max hours this worker can work.
        rtype: int
        """
        return self.max_hours

    def get_min_hours(self):
        """Returns min hours this worker can work.
        rtype: int
        """
        return self.min_hours

    def get_preferences(self):
        """Returns the ranking of preferred shifts for this worker.
        rtype: List of shift ids (int), sorted by preference, from most preferred to least preferred
        """
        return self.preferences

    def get_qualifications(self):
        """Returns the ids of shifts this worker is qualified for.
        rtype: Set of shift ids (int)"""
        return self.qualifications
