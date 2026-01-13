def calc_median(arr,d):
    more_temp = sorted(arr)
    if d & 1 == 0:
        half = int(d/2)
        return (more_temp[half] + more_temp[half-1])/2
    else:
        half = int((d+1)/2)
        return more_temp[half - 1]
        
    

def activityNotifications(expenditure, d):
    notices = 0
    print("array is",expenditure)
    for i in range (d,len(expenditure)):
        print(expenditure[i])
        temp_arr = expenditure[i - d : i]
        med = calc_median(temp_arr,d)
        print(temp_arr,expenditure[i], med)
        if (2 * med) < expenditure[i]:
            notices += 1
    return notices
