class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
    
        #assign a component id to connected components

        #nums is ascending
        # nums[i] + maxdiff >= nums[j]
        component = 0
        component_ids = [0] * n
        for i in range(1, len(nums)):
            curr = nums[i]
            prev_ = nums[i - 1]

            if curr - prev_ > maxDiff:            
                component += 1

            component_ids[i] = component
        ans = list()
        for q in queries:
            node1 = q[0]
            node2 = q[1]
            if component_ids[node1] == component_ids[node2]:
                ans.append(True)
            else:
                ans.append(False)
        return ans




