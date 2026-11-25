waypoints = [
    (0.0, 0.0),
    (3.0, 4.0),   # Distance = 5.0
    (8.0, 4.0),   # Distance = 5.0
    (8.0, 16.0),  # Distance = 12.0 (longest)
]

if len(waypoints) < 2:
    print("At least two waypoints are required to form a route.")
else:
    total_distance = 0.0
    max_segment_dist = -1.0
    longest_segment_info = ""

    print("--- Route Segments ---")
    for i in range(len(waypoints) - 1):
        x1, y1 = waypoints[i]
        x2, y2 = waypoints[i + 1]

        dx = x2 - x1
        dy = y2 - y1
        segment_dist = (dx ** 2 + dy ** 2) ** 0.5
        total_distance += segment_dist

        print(f"Segment {i + 1} {waypoints[i]} -> {waypoints[i + 1]}: {segment_dist:.2f} units")

        if segment_dist > max_segment_dist:
            max_segment_dist = segment_dist
            longest_segment_info = f"Segment {i + 1} {waypoints[i]} -> {waypoints[i + 1]} ({segment_dist:.2f} units)"

    print(f"\nTotal Route Distance: {total_distance:.2f} units")
    print(f"Longest Segment: {longest_segment_info}")
