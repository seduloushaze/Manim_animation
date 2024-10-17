from manim import *

class Draft_1(ThreeDScene):
    def construct(self):
        
        self.set_camera_orientation(phi=0, theta=3 * PI/2)
        #spheres on same point
        sphere1 = Sphere(center=(-5, -1, 0), radius=0.1, resolution=(4, 4))
        sphere1.set_color(YELLOW_E)
        sphere2 = Sphere(center=(-5, -1, 0), radius=0.1, resolution=(4, 4))
        sphere2.set_color(YELLOW_E)
        sphere3 = Sphere(center=(-5, -1, 0), radius=0.1, resolution=(4, 4))
        sphere3.set_color(YELLOW_E)
        sphere4 = Sphere(center=(-5, -1, 0), radius=0.1, resolution=(4, 4))
        sphere4.set_color(YELLOW_E)
        sphere5 = Sphere(center=(-5, -1, 0), radius=0.1, resolution=(4, 4))
        sphere5.set_color(YELLOW_E)

        #dots
        dots=[]
        #col
        col = [-5 ,-3,-1, 1, 3, 5]
        #row values
        col_0 = [-1]
        col_1_5 = [0 , -1 , -2]
        col_2_3 = [1, 0,-1,-2,-3]
        col_4 = [0.5 , -0.5 ,-1.5 ,-2.5]
        #positioning dots
        for x in col:
            if x==-5:
                for y in col_0:
                    d = Dot(point=[x,y,0],radius = 0.05)
                    dots.append(d)
            if x==-3 or x==5:
                for y in col_1_5:
                    d = Dot(point=[x,y,0],radius = 0.05)
                    dots.append(d)
            elif x==-1 or x==1:
                for y in col_2_3:
                    d = Dot(point=[x,y,0],radius = 0.05)
                    dots.append(d)
            elif x==3:
                for y in col_4:
                    d = Dot(point=[x,y,0],radius = 0.05)
                    dots.append(d)
        
        columns = [
            dots[0],     # First column
            dots[1:4],   # Second column
            dots[4:9],   # Third column
            dots[9:14],  # Fourth column
            dots[14:18], # Fifth column
            dots[18:21]  #sixth column
        ]

        #adding lines using loops
        lines =[]
        for i in range(0,5):
            for x in columns[i]:
                for y in columns[i+1]:
                    l = Line(x,y)
                    l.set_color(DARK_GRAY)
                    lines.append(l)
                    self.add(l)

        #handwritten A
        A = ImageMobject("./7.png")
        A.scale(0.2)
        A.move_to([-7.4, -1 ,0])
        
        for dot in dots:
            self.add(dot)
        # adding and animating letter
        self.add(A)
        self.play(A.animate.shift(RIGHT*2).set_rate_func(smooth), run_time=1)

         # Add spheres to a VGroup
        spheres = VGroup(sphere1, sphere2, sphere3, sphere4, sphere5)
        self.add(spheres)  # Add the spheres as a group
        sphere5.set_color(BLUE_E)
        self.play(
            A.animate.shift(IN * 1).set_opacity(0),  # Shrink and fade out
            FadeIn(spheres),  # Fade in spheres
            run_time=1
        )
        # movement throught neural network
        self.play(sphere1.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  lines[2].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+DOWN*3).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+UP*3).set_rate_func(smooth),
                  lines[13].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+UP*3).set_rate_func(smooth), 
                  sphere3.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+DOWN*2).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  lines[19].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+UP*2.5).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+DOWN*1.5).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+DOWN*1.5).set_rate_func(smooth),
                  lines[49].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+DOWN*0.5).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+DOWN*0.5).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2+DOWN*0.5).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+DOWN*0.5).set_rate_func(smooth),
                  lines[71].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        
        
        #logo A 
        Letter_A = ImageMobject("./1.png")
        Letter_A.move_to([5.5,-2,0])
        Letter_A.scale(0.4)
        self.play(FadeIn(Letter_A))
        

        self.play(FadeOut(spheres) , run_time=1)
        sphere5.set_color(YELLOW_E)
        lines[2].set_color(DARK_GRAY)
        lines[13].set_color(DARK_GRAY)
        lines[19].set_color(DARK_GRAY)
        lines[49].set_color(DARK_GRAY)
        lines[71].set_color(DARK_GRAY)

        I = ImageMobject("./8.png")
        I.scale(0.2)
        I.move_to([-7.4, -1 ,0])

        self.add(I)
        self.play(I.animate.shift(RIGHT*2).set_rate_func(smooth), run_time=1)
        sphere1.move_to([-5, -1, 0])
        sphere2.move_to([-5, -1, 0])
        sphere3.move_to([-5, -1, 0])
        sphere4.move_to([-5, -1, 0])
        sphere5.move_to([-5, -1, 0])

        sphere3.set_color(BLUE_E)

        self.play(
            I.animate.shift(IN * 1).set_opacity(0),  # Shrink and fade out
            FadeIn(spheres),  # Fade in spheres
            run_time=1
        )
        # movement throught neural network
        self.play(sphere1.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  lines[1].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+DOWN*3).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+UP*3).set_rate_func(smooth),
                  lines[9].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+UP*3).set_rate_func(smooth), 
                  sphere3.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+DOWN*2).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  lines[25].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+UP*2.5).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+DOWN*1.5).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+DOWN*1.5).set_rate_func(smooth),
                  lines[52].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+DOWN*0.5).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+DOWN*0.5).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2+DOWN*0.5).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  lines[67].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        
        
        Letter_i = ImageMobject("./2.png")
        Letter_i.move_to([5.5,-1,0])
        Letter_i.scale(0.4)
        self.play(FadeIn(Letter_i))

        self.play(FadeOut(spheres) , run_time=1)
        sphere3.set_color(YELLOW_E)
        lines[1].set_color(DARK_GRAY)
        lines[9].set_color(DARK_GRAY)
        lines[25].set_color(DARK_GRAY)
        lines[52].set_color(DARK_GRAY)
        lines[67].set_color(DARK_GRAY)

        C = ImageMobject("./9.png")
        C.scale(0.2)
        C.move_to([-7.4, -1 ,0])

        self.play(C.animate.shift(RIGHT*2).set_rate_func(smooth), run_time=1)
        sphere1.move_to([-5, -1, 0])
        sphere2.move_to([-5, -1, 0])
        sphere3.move_to([-5, -1, 0])
        sphere4.move_to([-5, -1, 0])
        sphere5.move_to([-5, -1, 0])

        
        

        sphere1.set_color(BLUE_E)

        self.play(
            C.animate.shift(IN * 1).set_opacity(0),  # Shrink and fade out
            FadeIn(spheres),  # Fade in spheres
            run_time=1
        )
        # movement throught neural network
        self.play(sphere1.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  lines[0].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+DOWN*3).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+UP*3).set_rate_func(smooth),
                  lines[7].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+UP*1).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+UP*3).set_rate_func(smooth), 
                  sphere3.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+DOWN*2).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+DOWN*1).set_rate_func(smooth),
                  lines[41].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+UP*2.5).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+DOWN*1.5).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+DOWN*1.5).set_rate_func(smooth),
                  lines[55].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        self.play(sphere1.animate.shift(RIGHT*2+DOWN*0.5).set_rate_func(smooth),
                  sphere2.animate.shift(RIGHT*2+DOWN*0.5).set_rate_func(smooth),
                  sphere3.animate.shift(RIGHT*2+DOWN*0.5).set_rate_func(smooth),
                  sphere4.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  sphere5.animate.shift(RIGHT*2+UP*0.5).set_rate_func(smooth),
                  lines[63].animate.set_color(BLUE_E).set_rate_func(smooth),
                  run_time=1)
        
        
        Letter_C = ImageMobject("./3.png")
        Letter_C.move_to([5.5,0,0])
        Letter_C.scale(0.4)
        self.play(FadeIn(Letter_C))

        self.move_camera(phi=90 * DEGREES, theta=0 * DEGREES,run_time =1)

        dot_group = VGroup(*dots)   # Grouping all dots
        line_group = VGroup(*lines) # Grouping all lines

        self.play(
            Letter_C.animate.rotate(PI / 2 ,axis=RIGHT).set_rate_func(smooth).rotate(PI/2).set_rate_func(smooth),  # Smooth the transition
            Letter_i.animate.rotate(PI / 2 ,axis=RIGHT).set_rate_func(smooth).rotate(PI/2).set_rate_func(smooth),  
            Letter_A.animate.rotate(PI / 2 ,axis=RIGHT).set_rate_func(smooth).rotate(PI/2).set_rate_func(smooth),
            FadeOut(VGroup(dot_group, line_group,spheres)),
            run_time=1
        )
        
        self.play(
            Letter_A.animate.scale(4.9),
            Letter_i.animate.scale(4.9), 
            Letter_C.animate.scale(4.9).shift(DOWN*1)
        )
        
        logo = ImageMobject('./AIC_logo.jpg')
        logo.move_to([5,-1,0])
        self.add(logo)
        logo.scale(1)
        
        logo.rotate(PI / 2 ,axis=RIGHT).rotate(PI/2)
        
        self.play(
            FadeOut(Letter_A,Letter_i,Letter_C),
            FadeIn(logo),
            run_time=1
        )

        
        self.wait() 
