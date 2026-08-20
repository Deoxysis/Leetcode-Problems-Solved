class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        angle_mins = (minutes / 60) * 360
        if hour == 12: hour = 0
        angle_hrs = (hour) * (30) + (minutes / 60) * (30)

        a1 = abs(angle_hrs - angle_mins)
        a2 = abs(angle_mins - angle_hrs)
        a3 = abs(360 - angle_mins + angle_hrs)
        a4 = abs(360 - angle_hrs + angle_mins)
        return min(a1 ,a2 , a3, a4)
