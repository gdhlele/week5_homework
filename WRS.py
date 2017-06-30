import random

def weighted_choice(weights):
    totals = []
    running_total = 0

    for w in weights:
        running_total += w
        totals.append(running_total)

    rnd = random.random() * running_total
    for i, total in enumerate(totals):
        if rnd < total:
            return i




sample_camps = {}
sample_camps_weights = [4, 5, 1]                       #specify weights
total_freq = 0

for i in range(1000):
    sample_camps_id = weighted_choice(sample_camps_weights)
    total_freq += 1
    if sample_camps_id in sample_camps:
        sample_camps[sample_camps_id] += 1
    else:
        sample_camps[sample_camps_id] = 1

for sample_id in sample_camps:
    print(
    "sample_id:", sample_id, ",freq distribution:", sample_camps[sample_id] * 1.0 / total_freq)
