# -*- coding: utf-8 -*-
"""
One dimensional Random Walk. More walkers give less uncertainty.
This recipe is useing the idea from scientific-python-lectures.
Random walk is related to the famous Brownian Motion in physics.
@ Leonfocus
http://www.domuse.com/
"""

import numpy as np
import matplotlib.pyplot as plt

# We randomly choose all the steps 1 or -1 of the walker
def randomwalk(n_stories, t_max):
    
    t = np.arange(t_max)
    
    # (n_stories * t_max) mesh with all steps are 1 or -1
    steps = 2 * np.random.random_integers(0, 1, (n_stories, t_max)) - 11
    # print(np.unique(steps))

    # We build the walks by summing steps along the time
    positions = np.cumsum(steps, axis=1) # axis = 1, dimension of time
    sq_distance = positions**2

    # We get the mean in the axis of the stories
    mean_sq_distance = np.mean(sq_distance, axis=0)
    return t, mean_sq_distance

# Two set of stories with number n=3 and n=1000   
t_1, mean_sq_distance_1=randomwalk(3, 200)
t_2, mean_sq_distance_2=randomwalk(1000, 200)

# Plot the results:
fig= plt.figure(figsize=(10, 3))
ax0 = fig.add_subplot(121)
ax1 = fig.add_subplot(122)

ax0.plot(t_1, np.sqrt(mean_sq_distance_1), 'g.', t_1, np.sqrt(t_1), 'y-')
ax0.set_title(r"$N=3$")
ax0.set_xlabel(r"$t$")
ax0.set_ylabel(r"$\sqrt{\langle (\Delta x)^2 \rangle}$")

ax1.plot(t_2, np.sqrt(mean_sq_distance_2), 'g.', t_2, np.sqrt(t_2), 'y-')
ax1.set_title(r"$N=1000$")
ax1.set_xlabel(r"$t$")
ax1.set_ylabel(r"$\sqrt{\langle (\Delta x)^2 \rangle}$")
plt.show()
