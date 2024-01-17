---
title: "Elevator Paradox"
categories:
tags:
last_modified_at: 2023-04-11
image: 
  path: https://images.unsplash.com/photo-1596711684682-2f3ea5d2d739?q=80&w=2938&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
  thumbnail: https://images.unsplash.com/photo-1596711684682-2f3ea5d2d739?q=80&w=2938&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D
---
Does it occur to you, when waiting for an elevator, that elevators always seem to be going the wrong way?

Yogendra is a product manager who has an office on the second floor of a seven-story building in Bangalore, and Shobhit(Data scientist) has an office on the sixth floor of the same building. The two generally visit quite a bit because they are college friends.

Shobhit, whenever he uses an elevator to go down to Yogendra's office, finds that all the elevators seem to be going up. Yogendra, on his way up to Shobhit's office, found that elevators were always going down. Two people, in the same building, noticed that the elevators were always moving in opposite directions.  

At first sight, this created the impression that perhaps elevator cars were being manufactured in the middle of the building and sent upwards to the roof or downwards to the basement to be dismantled. You can observe the same phenomenon in most tall buildings, and there are no elves involved. Do you see why it occurs?

Suppose you are at one of the bottom floors of a building. In this case, a single elevator spends most of its time in the top section of the building. If we start waiting for an elevator at a random point in time, it will thus be more likely that the first elevator approaches from above and continues downwards. The opposite is true if we are at one of the top floors of the building.

## Mathematical explanation:

### Idealizing assumptions: 

Suppose each elevator travels independently in continuous cycles from the bottom floor to the top and back again, moving with constant speed and with the same average waiting time on each floor. Thus at the time a button is pushed on any floor, we can assume that each elevator is at a random point in its cycle.

## For a single elevator, What is the probability that the elevator arriving on your floor will move up?

Shobhit, on the sixth floor, has five floors below and one above; therefore the probability is 5/6 that the elevator is below him and will be moving up when it arrives. Yogendra, on the second floor, has five floors above and one below; therefore the probability is 5/6 that the elevator is above him and will reach his floor on its way down.

## If there is more than one elevator, does the probabilities remain the same?

That is not true at all! Indeed, as the number of elevators approaches infinity the probability that the first elevator to stop on any floor (except the top or bottom floors) is going up (or down) approaches exactly 1/2 a rather unexpected result. Yet the probability (for, say, the second floor) remains 5/6 for every individual elevator and all elevators are equally likely to be the next to arrive.

The solution for two or more elevators is complicated by conditional probabilities. Where the condition is the choice of which elevator is first to arrive on the second floor is partly contingent on whether it was above us or below, since an elevator that is below the second floor when we begin to wait is likely to arrive ahead of an elevator that is above (all other things being equal).

Mathematical derivation for more than one elevator problem is complex, so here I use the final result and verify the result by simulation.

```python
P = 1/2 + (1/2) * (1-2p) * |1-2p|^(n-1)
```

where P --> The probability that the First elevator to arrive on the given floor will be going down. p --> Distance from the given floor to the bottom floor divided by the distance from the top floor to the given floor(The probability that the elevator arriving on your floor moves up when there is a single elevator) n --> Number of elevators.

Probability (P) approaches 1/2 as n(number of elevators), approaches infinity.

For a seven-story building, the probability that the first elevator to arrive on the second floor(Yogendra's office) will be going down when n=3 is,

```python
p = (1/6) and n = 3 => P = 1/2 + (1/2)(1-2/6)^3 = 0.648148
```

```python
//python simulation code//
**********************************************************************************

import numpy as np
import random
G=1/6
n=int(input("How many elevator"))
totalgoingdown=0
elevator=np.zeros([n, 4])
```

```python
for loop in range(1000000):
    for j in range(n):
        d=random.uniform(0, 1)
        if d<0.5:
            elevator[j,0]=0
        else:
            elevator[j,0]=1
        elevator[j,1]=random.uniform(0, 1)
        if elevator[j,1]<G:
            if elevator[j,0] == 0:
                elevator[j,2]=G+elevator[j,1]
            else:
                elevator[j,2]=G-elevator[j,1]
            elevator[j,3] = 1
        else:
            if elevator[j,0] == 0:
                elevator[j,2] =elevator[j,1]-G
            else:
                elevator[j,2] = (11/6)-elevator[j,1]
            elevator[j,3] = 0;
    min = elevator[0,2]
    index = 0
    for k in range(1,n):
        if elevator[k,2]<min:
            min = elevator[k,2]
            index = k
    if elevator[index,3] == 0:
        totalgoingdown= totalgoingdown+1
```
 
```python
print(totalgoingdown/1000000)

**********************************************************************************
//simulation result is:// 
  for n = 3
  0.648894 (similar to the theoretical result)
```

We imagine that the height of the building is scaled so that floor 1 (the bottom stop of an elevator) is at height 0 and floor 7 (the highest stop of an elevator) is at height 1. Thus, Yogendra’s elevator stop on the second floor is at height G = 1/6.

The n-by-4 array is called the elevator, in which the jth row describes the state of the jth elevator. Specifically,

elevator(j,0) = direction (up or down) the jth elevator is moving when Yogendra requests service;

elevator(j,1) = height of the jth elevator when Yogendra requests service;

elevator(j,2) = distance the jth elevator has to travel to reach Yogendra’s stop;

elevator(j,3) = direction (up or down) the jth elevator is moving when that elevator reaches Yogendra’s stop(“down’’ is coded as 0 and “up’’ is coded as 1)

We can now deduce the following four rules, for each elevator.

1. if the height < G and the initial elevator direction is down, then the travel distance to Gamow’s stop is G +height, and the arrival direction is up;
2. if the height < G and the initial elevator direction is up, then the travel distance to Gamow’s stop is G −height, and the arrival direction is up;
3. if the height > G and the initial elevator direction is down, then the travel distance to Gamow’s stop is height−G, and the arrival direction is down;
4. if the height > G and the initial elevator direction is up, then the travel distance to Gamow’s stop is (1−height)+ 5/6= (11/6−height), and the arrival direction is down.
