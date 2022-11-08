# Max Heap applicartion
# Leetcode 621: https://leetcode.com/problems/task-scheduler/


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        maxHeap = [-i for i in count.values()]
        heapq.heapify(maxHeap)
        q = collections.deque()
        time = 0

        while q or maxHeap:
            time += 1

            if maxHeap:
                cnt = heapq._heappop_max(maxHeap) + 1
                if cnt:
                    q.append([cnt, time+n])
            
            if q and q[0][1] == time:
                heapq.heappush(maxHeap, q.popleft()[0])

        return time
                


