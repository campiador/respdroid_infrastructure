#Saving data as files on disk

# Always keep the last experiment id
def save_experiment_id(a):
    with open('./storage/experiment_id', 'w') as f:
        f.write(str(a))


def load_experiment_id():
    try:
        with open('./storage/experiment_id', 'r') as f:
            a = int(f.read())
    except IOError:
        print "IO Warning: No previous experiments found, setting counter to 0."
        a = 0
    return a