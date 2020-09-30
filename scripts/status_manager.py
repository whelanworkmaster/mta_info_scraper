def parse_statuses(statuses, delayed_trains, train_delay_times):
    are_delayed_trains = False
    lines = iter(statuses.splitlines())
    new_delayed_trains = set()

    for line in lines:
        line = "".join(line.split())
        if are_delayed_trains:
            if len(line) < 8:
                new_delayed_trains.add(line)
                train_delay_times[line].start()
                if line not in delayed_trains:
                    print(f'Line {line} is experiencing delays')
            else:
                are_delayed_trains = False

        if line == 'Delays':
            are_delayed_trains = True

    no_longer_delayed = delayed_trains.difference(new_delayed_trains)
    for line in no_longer_delayed:
        train_delay_times[line].stop()
        print(f'Line {line} is now recovered')

    return new_delayed_trains
