# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/description/

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        employees = defaultdict(list)

        for name, time in zip(keyName, keyTime):
            employees[name].append(int(time[:2])*60 + int(time[3:]))
        
        alerts = []
        for name in sorted(employees.keys()):
            times = sorted(employees[name])
            
            for i in range(2, len(times)):
                if times[i - 2] + 60 >= times[i]:
                    alerts.append(name)
                    break
        
        return alerts
        
