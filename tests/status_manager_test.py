import unittest

from scripts.status_manager import parse_statuses_and_update_times, parse_statuses, \
    get_new_delayed_trains_and_update_times
from scripts.timer import Timer


class StatusManagerTest(unittest.TestCase):

    def test_shouldParseStatusesIntDict(self):
        status = """Trains Rerouted
                        D
                        N
                        Planned Work
                        2
                        5
                        E
                        SIR
                        Weekday Service
                        1
                        3
                        4"""

        statuses_dict = {'Trains Rerouted': ['D', 'N'], 'Planned Work': ['2', '5', 'E', 'SIR'],
                         'Weekday Service': ['1', '3', '4']}

        parsed_statuses_dict = parse_statuses(status)

        self.assertDictEqual(statuses_dict, parsed_statuses_dict)

    def test_shouldReturnEmptyListGivenNoDelayedTrainsInTrainStatus(self):
        delayed_trains = set()
        train_delay_times = get_test_mta_line_delay_times_dict()

        statuses_dict = {'Trains Rerouted': ['D', 'N'], 'Planned Work': ['2', '5', 'E', 'SIR'],
                         'Weekday Service': ['1', '3', '4']}
        new_delayed_trains = get_new_delayed_trains_and_update_times(statuses_dict, delayed_trains, train_delay_times)

        self.assertTrue(not new_delayed_trains)

    def test_shouldReturnListOfDelayedTrainsGivenDelayedTrainsInTrainStatus(self):
        delayed_trains = set()
        train_delay_times = get_test_mta_line_delay_times_dict()

        statuses_dict = {'Trains Rerouted': ['D', 'N'], 'Planned Work': ['2', '5', 'E', 'SIR'],
                         'Delayed': ['A', 'B', 'C', 'F']}
        new_delayed_trains = get_new_delayed_trains_and_update_times(statuses_dict, delayed_trains, train_delay_times)

        self.assertEqual(new_delayed_trains, {'A', 'B', 'C', 'F'})

    def test_shouldPrintLineRecoveredWhenTrainWasDelayedButNowIsnt(self):
        delayed_trains = {'A', 'B', 'C', 'F'}
        train_delay_times = get_test_mta_line_delay_times_dict()
        train_delay_times['F'].start()

        statuses_dict = {'Trains Rerouted': ['D', 'N'], 'Planned Work': ['2', '5', 'E', 'SIR'],
                         'Delayed': ['A', 'B', 'C']}
        new_delayed_trains = get_new_delayed_trains_and_update_times(statuses_dict, delayed_trains, train_delay_times)

        self.assertEqual(new_delayed_trains, {'A', 'B', 'C'})


def get_test_mta_line_delay_times_dict():
    return {'R': Timer(),
            'D': Timer(),
            'E': Timer(),
            'N': Timer(),
            'SIR': Timer(),
            '1': Timer(),
            '2': Timer(),
            '3': Timer(),
            '4': Timer(),
            '5': Timer(),
            '6': Timer(),
            '7': Timer(),
            'A': Timer(),
            'B': Timer(),
            'C': Timer(),
            'F': Timer(),
            'S': Timer(),
            'G': Timer(),
            'J': Timer(),
            'L': Timer(),
            'M': Timer(),
            'Q': Timer(),
            'W': Timer()
            }
