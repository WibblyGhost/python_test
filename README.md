# Council Intersection

**Timed challenge of 2 hours**

![General Developer Testing Link](general-developer-testing.pdf)

## Purpose

This project was a simple test provided as a part of an interview challenge, it contains a set of problems designed around a council intersection. This intersection can consist of many roads and each road will have a number of cars driving that road. The goal was to find the most efficient type of intersection to use for different types of flow rates.

## Thought Process Used

I decided that to allow for expandability of intersections and calculations that I should split the problem into two objects:

1. The intersections, which can contain a number of roads and each road can carry a particular flow rate.
2. The weighted values and decision process which divys up the types of intersections over certain flow rates. 

Whilst developing this program I wasn't able to implement every feature due to the time limit but I tried to at least attempt every extra problem.

## Possible Improvements

Given looking back at my program I would love to improve the user interaction. Having to rely on the user inputting unknown commands is a pain and I would like to make the program use prompts and be more usable.

The CSV reader was halted since there was some difficulty in deciding how to structure the CSV and convert the CSV into dictionaries, I would like to improve this since I know how to do so, just undecided in the time frame.

Creating some more depth to the calculation system would be nice, rather than using a set of if statements it would function better if we referred to a class/object which defined a table of decision units, maybe even input a config or CSV to define what the decision weights of an intersection is.

## Extension Problems (See PDF)

1. DONE - Done as a part of 2.
2. DONE - Needs more fleshing, can be done through "py -i" running Intersection().set_road(*args)
3. FIXME - Got the CSV reader working, need to flesh out converting list into dictionary then running the functions
4. TODO - Requires making a table or dictionaries within dictionaries, modeling data formats
5. DONE
6. DONE - Added new variables to the defined roads in the class, -> Basic version
