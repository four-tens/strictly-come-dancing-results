#!/usr/bin/env python

import csv
import collections

class ResultConsistencyCheck(object):
    def __init__(self):
        with open('results.csv') as csvfile:
            self.results = list(csv.DictReader(csvfile))

    def scores_should_add_up(self):
        for row in self.results:
            derived_total = sum([int(value) for column, value in row.iteritems() if "score_" in column])
            actual_total = int(row['total'])
            assert derived_total == actual_total, "[FAIL] Inconsistent total score in row: %s" % row
        print("[PASS] All dances have consistent totals")

        
    def series_week_runningorder_should_be_unique(self):
        unique_ids = [ "%s-%s-%s" % (row['series'], row['week'], row['running_order']) for row in self.results]
        counts = [item for item, count in collections.Counter(unique_ids).items() if count > 1]
        assert not counts, "[FAIL] Non-unique identifiers: %s" % counts
        print("[PASS] All dances have unique identifiers")
        
    def run(self):
        self.scores_should_add_up()
        self.series_week_runningorder_should_be_unique()

if __name__ == "__main__":
    ResultConsistencyCheck().run()
