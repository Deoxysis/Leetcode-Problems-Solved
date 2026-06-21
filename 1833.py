class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        counts = [0 for i in range(max(costs))]
        ans = 0
        for i in costs:
            counts[ i - 1] += 1 #since arr is 0 indexed but min cost is 1
        
        for i in range(len(counts)):
            if counts[i] == 0: 
                continue

            price = i + 1
            segment = price * counts[i] 
            
            # If we have enough coins to buy ALL ice creams at this price
            if coins >= segment:
                ans += counts[i]
                coins -= segment
            
            # If we CANNOT afford all of them, buy as many as possible and stop
            else:
                ans += coins // price
                break  
        return ans

