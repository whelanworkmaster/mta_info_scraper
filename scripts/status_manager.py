from collections import defaultdict


def parse_statuses(statuses: str):
    statuses_dict = defaultdict(list)
    lines = iter(statuses.splitlines())

    current_key = ''

    for line in lines:
        line = line.lstrip()

        if len(line) > 7:
            current_key = line
            continue
        else:
            current_val = line

        if current_key and current_val:
            statuses_dict[current_key].append(current_val)

    return statuses_dict


def get_new_delayed_trains_and_update_times(statuses: dict, delayed_trains: set, train_delay_times: dict):
    new_delayed_trains = set()

    delayed_train_lines = []
    if 'Delayed' in statuses:
        delayed_train_lines = statuses['Delayed']

    for line in delayed_train_lines:
        new_delayed_trains.add(line)
        train_delay_times[line].start()
        if line not in delayed_trains:
            print(f'Line {line} is experiencing delays')

    no_longer_delayed = delayed_trains.difference(new_delayed_trains)
    for line in no_longer_delayed:
        train_delay_times[line].stop()
        print(f'Line {line} is now recovered')

    return new_delayed_trains
