I wrote this code during the [University Physics Competition
2022](http://www.uphysicsc.com/2022contest.html). This code solves the
2<sup>nd</sup> -order ordinary coupled differential equations. The
problem was to find a suitable range of initial velocity and the spin of
the football from which the chance of getting a goal would increase in
penalty shots. By changing the initial velocity and spin we can observe
if the ball goes through the desired area. The desired area was assumed
to be the corner of the goalpost.  
The mathematical equations were mostly derived from this \[1\]. The
numerical development was done with help of this \[2\] paper also.
Starting from spin angular velocity $20\ rad.s^{- 1}$ with increment of
$10rad.s^{- 1}$ ,the code will run for 4 sets of initial spin angular
velocities. For each set of spin angular velocity there will be five
sets of initial velocities. I didn’t make an option for taking the
initial velocities from the user but if you want to modify it then make
a pull request.

The 2<sup>nd</sup>-order differential equations were solved by the
4<sup>th</sup>-order Runge-Kutta method with the help of Euler’s method.

<sup>1</sup>Myers, T. G., and Sarah Louise Mitchell. "A mathematical analysis of the
motion of an in-flight soccer ball." *Sports engineering* 16.1 (2013):
29-41.

<sup>2</sup> S. H¨orzer, C. Fuchs, R. Gastinger, A. Sabo, L. Mehnen, J.
Martinek, and M. Reichel.

Simulation of spinning soccer ball trajectories influenced by altitude.
Procedia Engineering,

2(2):2461–2466, 2010. The Engineering of Sport 8 - Engineering Emotion.
