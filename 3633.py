class Solution:
    def earliestFinishTime(self, landStartTime: List[int], landDuration: List[int], waterStartTime: List[int], waterDuration: List[int]) -> int:
        
        ttime = 10000
        for i in range(len(landStartTime)):
            temp = landDuration[i] + landStartTime[i]
            
            min_duration_water = 1001
            for j in range(len(waterStartTime)):
                if temp >= waterStartTime[j]:
                    min_duration_water = min(min_duration_water, waterDuration[j])
                else:
                    min_duration_water = min(min_duration_water, waterStartTime[j] + waterDuration[j] - landStartTime[i] - landDuration[i])
            temp += min_duration_water
            ttime = min(temp, ttime)
        
        for i in range(len(waterStartTime)):
            temp = waterDuration[i] + waterStartTime[i]
            
            min_duration_water = 1001
            for j in range(len(landStartTime)):
                if temp >= landStartTime[j]:
                    min_duration_water = min(min_duration_water, landDuration[j])
                else:
                    min_duration_water = min(min_duration_water, landStartTime[j] + landDuration[j] - waterStartTime[i] - waterDuration[i])
            temp += min_duration_water
            ttime = min(temp, ttime)

        return ttime

