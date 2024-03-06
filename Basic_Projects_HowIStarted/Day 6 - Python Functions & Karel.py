# Day 6
#Functions, Karel and While Loops

#escaping the maze
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def vai_robozim():
   if wall_in_front() and wall_on_right():
       turn_left()
   elif wall_in_front() and not wall_on_right():
       turn_right()
       move()
   elif front_is_clear() and right_is_clear():
       turn_right()
       move()
   elif front_is_clear():
       move()
        
while not at_goal():
    vai_robozim()