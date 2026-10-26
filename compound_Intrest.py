def fallingDistance(time):
    """
    Calculate the distance an object falls due to gravity in a given time.
    Formula: d = 0.5 * g * t^2
    where g = 9.8 m/s² (acceleration due to gravity)
    """
    g = 9.8
    distance = 0.5 * g * (time ** 2)
    return distance

# Main program to display falling distances for 1-10 seconds
print("Time (s)\tDistance (m)")
print("----------------------------")

for seconds in range(1, 11):
    distance = fallingDistance(seconds)
    print(f"{seconds}\t\t{distance:.2f}")