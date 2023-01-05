class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:
        ans = []
        pq = [] # min-heap 
        t = 0 # end of prev task 
        
        tasks.append([inf, inf])
        for (enq, prc), i in sorted(zip(tasks, range(len(tasks)))): # adding a sentinel
            while pq and t < enq: 
                tp, ii, te = heappop(pq)
                ans.append(ii)
                t = max(t, te) + tp # time finish processing this task
            heappush(pq, (prc, i, enq))
        return ans 