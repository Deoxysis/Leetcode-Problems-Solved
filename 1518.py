class Solution(object):
    def numWaterBottles(self, numBottles, numExchange):
        """
        :type numBottles: int
        :type numExchange: int
        :rtype: int
        """
        def bottles(numbottles, empty, exchange):
            if(numbottles+empty)<exchange: return numbottles
            else: return numbottles + bottles((numbottles + empty)/exchange, (numbottles + empty)%exchange, exchange )
        return bottles(numBottles, 0, numExchange)

        