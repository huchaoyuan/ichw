"""planets.py: The trajectory of the six planets in the solar system.

__author__ = "HuChaoyuan"
__pkuid__  = "1800011776"
__email__  = "huchaoyuan@pku.edu.cn"
"""
import turtle
import math
wn=turtle.Screen()
wn.bgcolor('black')
planets=['mercury','venus','earth','mars','jupiter','saturn','sun']
colors=['grey','yellow','blue','red','purple','orange','white']
ass=[65,85,95,160,170,250,-35] # transverse axis
bs=[50,70,120,135,215,200] # longitudinal axis
ws=[1,0.8,0.65,0.49,0.34,0.29] # angle of movement
sizes=[0.3,0.4,0.8,0.6,1.0,1.2,2] # planetary size
for i in range(7):
    planets[i]=turtle.Turtle()
    planets[i].speed(0)
    planets[i].color(colors[i])
    planets[i].shape('circle')
    planets[i].shapesize(sizes[i])
    planets[i].penup()
    planets[i].goto(ass[i], 0)
    planets[i].pendown()
def rotate(p,a,b,wt):
    '''
    The matched rotation of the matched planet.
    :param p: planets
    :param a: the horizontal axis of the planetary trajectory
    :param b: the longitudinal axis of the planetary trajectory
    :param wt: corresponding angles in parametric equations
    :return: execution of planetary movement
    '''
    p.goto(a*math.cos(math.radians(wt)),b*math.sin(math.radians(wt)))
    pass
def main():
    for x in range(10000):
        for i in range(6):
            rotate(planets[i],ass[i],bs[i],x*ws[i])
if __name__ == '__main__':
    main()
