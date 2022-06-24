def compute_closest_to_zero(ts):
    # Write your code here
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)
    print(ts)
    return min(map(lambda x:abs(x), ts)) if len(ts) > 0 else 0
    
    
    
    
print(compute_closest_to_zero([3,2,3,6,4,1,2,3,2,-1,-2,2,2,1])) #,
