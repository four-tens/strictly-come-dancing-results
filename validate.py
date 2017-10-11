#!/usr/bin/env python

import csv

class ResultConsistencyCheck(object):
    def __init__(self):
        with open('results.csv') as csvfile:
            self.results = list(csv.DictReader(csvfile))

    def scores_should_add_up(self):
        for row in self.results:
            derived_total = sum([int(value) for column, value in row.iteritems() if "score_" in column])
            actual_total = int(row['total'])
            assert derived_total == actual_total, "[FAIL] Inconsistent total score in row: %s" % row
        print "[PASS] Row totals consistent"

    def run(self):
        self.scores_should_add_up()

if __name__ == "__main__":
    ResultConsistencyCheck().run()
