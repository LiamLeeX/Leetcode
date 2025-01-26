class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = start = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                start = i + 1
        return start
# 为什么if total < 0:就可以舍弃掉start到i中间这一段路程，这一段路程任何一个点都不可能成为起点？
# 假设中间一个点为m
# 在m前面的油量 > 0 ,对目前油量有贡献，
# 假设从m出发，此时油量为0，到达i的时候油量只会更少
# 可以在脑海中想象一个函数图像，没有之前存储的油量，到达i点只会整个图像都下移

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        min_sum = float('inf')
        min_idx = 0
        for i in range(len(gas)):
            total += gas[i] - cost[i]
            if total < min_sum:
                min_sum = total
                min_idx = i
        return (min_idx + 1) % len(gas)