def do_stuff(s: str) -> int:
    # Initialize a list with values equivalent to Vec in C++
    vec = [0, 1, 2, 3, 4]
    
    # Index initialization
    idx = 0
    
    # Apply the conditions
    if len(s) > 5:
        idx += 1
    if "foo" in s:
        idx += 1
    if "bar" in s:
        idx += 1
    if "ouch" in s:
        idx += 1
    if "omg" in s:
        idx += 1
    
    # Return the corresponding value from vec
    return vec[idx]
