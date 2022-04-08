W = 100
N = 6
weights = list(map(int, "50 30 10 10 40 50".split()))

num = 0
bridge = []
for i in weights:
    bridge.insert(0, i)
    if len(bridge) > 4:
        bridge.pop()
    if sum(bridge) > W:
        print(num)
        break
    else:
        num += 1

# Queue data structure
