# Week 1.5, Session 1: Task 3
import math
class Point:
    """
    A Point in 2D space.
    """
    #create a point with self
    def __init__(self, x, y):
        self.x = x
        self.y = y

     # Distance from (0, 0)
    def distance(self):
        answer = math.sqrt(self.x * self.x + self.y * self.y)
        return answer

    # Distance between two points
    def distance_to(self, other):
        x = self.x - other.x
        y = self.y - other.y

        answer = math.sqrt(x * x + y * y)
        return answer


    # Create two points
   p = Point(3, 4)
q = Point(6, 8)

# Print the results
print("Point 1:", p.x, p.y)
print("Point 2:", q.x, q.y)

print("Distance from origin:", p.distance())
print("Distance between points:", p.distance_to(q))


    # Add constructor here

    # Add distance() method here

    # Add distance_to() method here
    # (This will need a parameter representing another point)



# Finally, add code here to demonstrate use of Point
