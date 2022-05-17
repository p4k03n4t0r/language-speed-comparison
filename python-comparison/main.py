import isolated
import returned
import shared

total_work = 100
concurrent = 100

results = [
    # isolated.isolated(total_work, concurrent),
    # returned.returned(total_work, concurrent),
    shared.shared(total_work, concurrent),
]
for result in results:
    for r in result:
        print(str(r))
