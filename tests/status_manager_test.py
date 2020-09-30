import unittest

from scripts.status_manager import parse_statuses
from scripts.timer import Timer


class StatusManagerTest(unittest.TestCase):

    def test_shouldReturnEmptyListGivenNoDelayedTrainsInTrainStatus(self):
        delayed_trains = set()
        train_delay_times = get_mta_line_delay_times_dict()

        status = """"Trains Rerouted
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
                        4
                        6
                        7
                        A
                        B
                        C
                        F
                        S
                        G
                        S
                        S
                        J
                        L
                        M
                        Q
                        R
                        W
                        Z
                        Trains Rerouted
                        D
                        N"""
        new_delayed_trains = parse_statuses(status, delayed_trains, train_delay_times)

        self.assertTrue(not new_delayed_trains)

    def test_shouldReturnListOfDelayedTrainsGivenDelayedTrainsInTrainStatus(self):
        delayed_trains = set()
        train_delay_times = get_mta_line_delay_times_dict()

        status = """"Trains Rerouted
                        D
                        N
                        Planned Work
                        2
                        5
                        E
                        SIR
                        Delays
                        A
                        B
                        C
                        F
                        Weekday Service
                        1
                        3
                        4
                        6
                        7
                        S
                        G
                        S
                        S
                        J
                        L
                        M
                        Q
                        R
                        W
                        Z
                        Trains Rerouted
                        D
                        N"""
        new_delayed_trains = parse_statuses(status, delayed_trains, train_delay_times)

        self.assertEqual(new_delayed_trains, {'A', 'B', 'C', 'F'})

    def test_shouldPrintLineRecoveredWhenTrainWasDelayedButNowIsnt(self):
        delayed_trains = {'A', 'B', 'C', 'F'}
        train_delay_times = get_mta_line_delay_times_dict()
        train_delay_times['F'].start()

        status = """"Trains Rerouted
                        D
                        N
                        Planned Work
                        2
                        5
                        E
                        SIR
                        Delays
                        A
                        B
                        C
                        Weekday Service
                        1
                        3
                        4
                        6
                        7
                        S
                        G
                        S
                        S
                        J
                        L
                        M
                        Q
                        R
                        W
                        Z
                        Trains Rerouted
                        D
                        N"""
        new_delayed_trains = parse_statuses(status, delayed_trains, train_delay_times)

        self.assertEqual(new_delayed_trains, {'A', 'B', 'C'})


def get_mta_line_delay_times_dict():
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