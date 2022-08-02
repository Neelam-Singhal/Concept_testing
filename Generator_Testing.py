import random
import time
import memory_profiler

name = ['a', 'b', 'c', 'd', 'e']
subjects = ['aa', 'bb', 'cc', 'dd', 'ee']


print("memory (Before) - {}".format(memory_profiler.memory_usage()))

def use_append(num_people):
    results = []
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(name),
            'subjects': random.choice(subjects)
        }
        results.append(person)
    return results

def use_generator(num_people):
    for i in range(num_people):
        person = {
            'id': i,
            'name': random.choice(name),
            'subjects': random.choice(subjects)
        }
        yield person       

start = time.time()
people = use_generator(1000000)
end=time.time()

print("memory (After) - {}".format(memory_profiler.memory_usage()))


print("time taken : {}".format(end-start))
#print((people))