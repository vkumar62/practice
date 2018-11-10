import pdb

class Solution(object):
    def maxVacationDays(self, flights, days):
        """
        :type flights: List[List[int]]
        :type days: List[List[int]]
        :rtype: int
        """
        
        def max_vacation_helper(week, city):
            if week >= K:
                return 0
            
            if vacation_sums[city][week] == -1:
                for next_city, flight in enumerate(flights[city]):
                    if flight == 1 or next_city == city:
                        vacations = days[next_city][week] + max_vacation_helper(week+1, next_city)
                        vacation_sums[city][week] = max(vacations, vacation_sums[city][week])
            return vacation_sums[city][week] 
        
        #pdb.set_trace()
        if not days:
            return 0
        
        K = len(days[0])
        
        vacation_sums = [[-1 for _ in range(K)] for _ in range(len(days))]
        return max_vacation_helper(0, 0)

    def maxVacationDays(self, flights, days):
        if not days:
            return 0
        
        K = len(days[0])
        vacation_sums = [[0 for _ in range(len(days))] for _ in range(K+1)]

        for week in reversed(range(K)):
            for city, city_flights in enumerate(flights):
                for next_city, flight in enumerate(city_flights):
                    if flight == 1 or next_city == city:
                        vacations = days[next_city][week] + vacation_sums[week+1][next_city]
                        vacation_sums[week][city] = max(vacations, vacation_sums[week][city])
        return vacation_sums[0][0] 


flights = [[0,1,0,0,0],[0,0,1,0,0],[0,0,0,1,0],[0,1,1,0,0],[1,1,0,1,0]]
days = [[5,4,3,0,4],[0,6,4,3,6],[4,2,0,2,6],[4,6,1,4,3],[5,0,4,0,5]]
print(Solution().maxVacationDays(flights, days))
