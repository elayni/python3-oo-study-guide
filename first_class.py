# class name must start with letter or underscore
# can only be comprised of letters, underscores or numbers
class MyFirstClass:  # Pep 8 recommends that classes should ne named using CapWord
    pass

class Point: # class with no data or behaviors, too
    pass

# instances
p1 = Point()
p2 = Point()

# assing a value to an attribute on an object
# <object>.<attribute> = <value>  this is a dot notation

p1.x = 5
p1.y = 4

p2.x = 3
p2.y = 6

print(p1.x, p1.y)
print(p2.x, p2.y)

class Coordinate:
    def reset(self):
        self.x = 0
        self.y = 0

p = Coordinate()
p.reset()
print(p.x, p.y) #the output is 0 0

