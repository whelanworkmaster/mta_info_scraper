from timer import Timer


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
