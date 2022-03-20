N = input("")
Swifts = list(map(int, input("").split()))
Semaphores = list(map(int, input("").split()))

swift_sum = 0
semaphores_sum = 0

for i in range(int(N)):
    swift_sum += Swifts[i]
    semaphores_sum += Semaphores[i]
    if swift_sum == semaphores_sum:
        print(i + 1)
        break
