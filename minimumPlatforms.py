def minimum_platforms(arrivals, departures):
    arr = sorted([int(a.replace(":", "")) for a in arrivals])
    dep = sorted([int(d.replace(":", "")) for d in departures])
    
    platforms_needed, max_platforms = 0, 0
    i, j = 0, 0
    
    while i < len(arr) and j < len(dep):
        if arr[i] <= dep[j]:
            platforms_needed += 1
            i += 1
        else:
            platforms_needed -= 1
            j += 1
        max_platforms = max(max_platforms, platforms_needed)
    
    return max_platforms


arrivals = ["9:00", "9:40", "9:50", "11:00", "15:00", "18:00"]
departures = ["9:10", "12:00", "11:20", "11:30", "19:00", "20:00"]
print(minimum_platforms(arrivals, departures))
