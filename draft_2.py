from manim import *

class Draft_1(ThreeDScene):
    def construct(self):
        #
        self.set_camera_orientation(phi=0, theta=3 * PI/2)

        sphere1 = Sphere(center=(-6, 0, 0), radius=0.1, resolution=(25, 25))
        sphere1.set_color(YELLOW_E)
        sphere2 = Sphere(center=(-6, -1, 0), radius=0.1, resolution=(25, 25))
        sphere2.set_color(YELLOW_E)
        sphere3 = Sphere(center=(-6, -2, 0), radius=0.1, resolution=(25, 25))
        sphere3.set_color(YELLOW_E)
        sphere4 = Sphere(center=(-6, -1, 0), radius=0.1, resolution=(25, 25))
        sphere4.set_color(YELLOW_E)
        sphere5 = Sphere(center=(-6, -2, 0), radius=0.1, resolution=(25, 25))
        sphere5.set_color(YELLOW_E)

        #dots
        dots=[]
        #col
        col = [-5 ,-3,-1, 1, 3]
        #row values
        col_1_5 = [0 , -1 , -2]
        col_2_3 = [1, 0,-1,-2,-3]
        col_4 = [0.5 , -0.5 ,-1.5 ,-2.5]

        for x in col:
            if x==-5 or x==3:
                for y in col_1_5:
                    d = Dot(point=[x,y,0],radius = 0.05)
                    dots.append(d)
            elif x==-3 or x==-1:
                for y in col_2_3:
                    d = Dot(point=[x,y,0],radius = 0.05)
                    dots.append(d)
            else:
                for y in col_4:
                    d = Dot(point=[x,y,0],radius = 0.05)
                    dots.append(d)
        
        columns = [
            dots[0:3],   # First column
            dots[3:8],   # Second column
            dots[8:13],  # Third column
            dots[13:17], # Fourth column
            dots[17:20]  # Fifth column
        ]
        for i in range(0,4):
            for x in columns[i]:
                for y in columns[i+1]:
                    l = Line(x,y)
                    l.set_color(DARK_GRAY)
                    self.add(l)

        # Add spheres to a VGroup
        spheres = VGroup(sphere1, sphere2, sphere3, sphere4, sphere5)
        self.add(spheres)  # Add the spheres as a group

        for dot in dots:
            self.add(dot)
        
        # Animate the spheres moving together
        self.play(spheres.animate.shift(RIGHT * 1), run_time=2)
        #sphere1 animation
        self.play(sphere1.animate.shift(RIGHT*2+DOWN*4) , run_time=2)
        self.play(sphere1.animate.shift(RIGHT*2+UP*1) , run_time=2)
        self.play(sphere1.animate.shift(RIGHT*2+UP*2.5) , run_time=2)
        self.play(sphere1.animate.shift(RIGHT*2+DOWN*0.5) , run_time=2)

        #sphere2 animation
        self.play(sphere2.animate.shift(RIGHT*2+DOWN*1) , run_time=2)
        self.play(sphere2.animate.shift(RIGHT*2+UP*3) , run_time=2)
        self.play(sphere2.animate.shift(RIGHT*2+DOWN*1.5) , run_time=2)
        self.play(sphere2.animate.shift(RIGHT*2+DOWN*0.5) , run_time=2)

        #sphere3 animation
        self.play(sphere3.animate.shift(RIGHT*2+UP*1) , run_time=2)
        self.play(sphere3.animate.shift(RIGHT*2+DOWN*1) , run_time=2)
        self.play(sphere3.animate.shift(RIGHT*2+UP*0.5) , run_time=2)
        self.play(sphere3.animate.shift(RIGHT*2+UP*0.5) , run_time=2)

        #sphere4 animation
        self.play(sphere4.animate.shift(RIGHT*2+UP*4) , run_time=2)
        self.play(sphere4.animate.shift(RIGHT*2+DOWN*1) , run_time=2)
        self.play(sphere4.animate.shift(RIGHT*2+DOWN*1.5) , run_time=2)
        self.play(sphere4.animate.shift(RIGHT*2+DOWN*0.5) , run_time=2)

        #sphere5 animation
        self.play(sphere5.animate.shift(RIGHT*2+UP*1) , run_time=2)
        self.play(sphere5.animate.shift(RIGHT*2+DOWN*2) , run_time=2)
        self.play(sphere5.animate.shift(RIGHT*2+UP*0.5) , run_time=2)
        self.play(sphere5.animate.shift(RIGHT*2+UP*1.5) , run_time=2)
        self.wait()