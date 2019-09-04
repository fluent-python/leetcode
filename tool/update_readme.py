
README = '../README.md'

with open(README, 'r') as f:
    lines = [line for line in f.readlines() if line.startswith('-')]
    print("lines: {}".format(lines))
