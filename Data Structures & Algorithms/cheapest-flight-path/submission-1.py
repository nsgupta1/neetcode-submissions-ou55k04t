class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
            Using optimized BellMan's ford algorithm for Shortest Path Faster algo
            Maintain a prices array from 0 to n and initialize with infinity
            use a queue to put edges layer by layer like BFS, however, stop exploring next layer
            and optimizing price if stops is greater than K,
            Maintain Adjacency list for initial BFS
        '''
        adjMap = {}
        prices = [float('inf')] * n
        prices[src] = 0
        queue = deque()
        queue.append((0, src, 0)) # cost, node, stops
        for i in range(n):
            adjMap[i] = []
        
        for u, v, w in flights:
            adjMap[u].append((v, w))
        
        while queue:
            cst, node, stops = queue.popleft()
            if stops > k:
                continue
            
            for v, w in adjMap[node]:
                nextCost = cst + w
                if nextCost < prices[v]:
                   prices[v] = nextCost
                   queue.append((nextCost, v, stops+1))
        
        return -1 if prices[dst] == float('inf') else prices[dst]



        


        
        