from aspects.player import Player
import time

start = time.time()
p = Player()
position_store = {}
iterations = 1000000
for _ in range(iterations):
    pos = p.play()
    if pos in position_store.keys():
        position_store[pos] += 1
    else:
        position_store[pos] = 1

for key in sorted(position_store):
    print("%s: %s%%" % (key, position_store[key] * 100/iterations))

print("\nCompleted in %s s" % str(round(time.time() - start, 2)))