from manimlib.imports import *

class TestScene3(Scene):
  def construct(self):
    text = TextMobject("Today we will study about Fractions")
    text.scale(1.5)

    self.play(Write(text))
    self.wait(4)
    self.play(FadeOut(text))

    text2 = TextMobject("Fractions are \"Part of a Whole\"")
    text2.scale(1.5)

    self.play(Write(text2))
    self.wait(3)
    self.play(FadeOut(text2))

    text3 = TextMobject("Let us take a few examples")
    text3.scale(1.5)

    self.play(Write(text3))
    self.wait(3)
    

    text4 = TextMobject("Let us take a few examples")
    text4.scale(1)

    text4.to_edge(UP)
    self.play(Transform(text3,text4))

    text5 = TextMobject("Why don't we try to paint half of a circle !")
    text5.scale(1.5)
    self.play(Write(text5))
    self.wait(3)

    self.play(FadeOut(text4))
    self.play(FadeOut(text3))
    text6 = TextMobject("Why don't we try to paint half of a circle !")
    text6.scale(1)
    text6.to_edge(UP)

    self.play(Transform(text5,text6))
    self.wait(1)
    #actually animating the shapes from here

    circle = Circle(color=YELLOW)
    self.play(FadeIn(circle))

    self.wait(3)

    sector = Sector(0,3.14159265)
    sector.set_fill(YELLOW,opacity=1)
    self.play(FadeIn(sector))

    self.wait(3)

    text7 = TextMobject("We just colored the upper half of the circle !")
    text7.scale(1)
    text7.to_edge(DOWN)

    self.wait(2)
    self.play(Write(text7))

    self.wait(3)
    self.play(FadeOut(text5))
    self.play(FadeOut(sector))
    self.play(FadeOut(circle))
    self.play(FadeOut(text7))

    self.wait(2)

    text8 = TextMobject("Next we color half of a square")
    text8.scale(1)
    text8.to_edge(UP)

    self.wait(2)
    self.play(Write(text8))

    #Now how the fuck do I draw a square

    square = Square(color=PINK)
    self.play(ShowCreation(square))
    self.wait(3)
    rectangle = Rectangle(color=PINK)
    rectangle.set_width(0.5)
    rectangle.set_height(1)
    rectangle.shift(0.5*UP)
    rectangle.set_fill(PINK,opacity=1)
    self.play(FadeIn(rectangle))
    self.wait(3)

    text9 = TextMobject("We just colored the upper half of the Square!")
    text9.scale(1)
    text9.to_edge(DOWN)

    self.play(Write(text9))
    self.wait(3)
    self.play(FadeOut(text8))
    self.play(FadeOut(text9))
    self.play(FadeOut(rectangle))
    self.play(FadeOut(square))
    self.wait(2)

    text10 = TextMobject("We could've also painted our circle this way")
    text10.scale(1)
    text10.to_edge(UP)
    self.play(Write(text10))

    circle2 = Circle(color=BLUE)
    self.play(ShowCreation(circle2))

    sector2 = Sector(0,3.14159265)
    sector2.rotate(-2*TAU/8)
    sector2.set_fill(BLUE,opacity=1)
    sector2.shift(0.5*RIGHT)
    sector2.shift(0.5*DOWN)
    self.play(FadeIn(sector2))
    self.wait(3)
    self.play(FadeOut(sector2))
    self.play(FadeOut(text10))
    self.wait(2)

    text11 = TextMobject("Or maybe even this way")
    text11.scale(1)
    text11.to_edge(UP)
    self.play(Write(text11))

    sector3 = Sector(0,3.14159265)
    sector3.rotate(-4*TAU/8)
    sector3.set_fill(BLUE,opacity=1)
    sector3.shift(DOWN)
    self.play(FadeIn(sector3))
    self.wait(3)
    self.play(FadeOut(sector3))
    self.play(FadeOut(circle2))
    self.play(FadeOut(text11))
    self.wait(2)

    text12 = TextMobject("Same for the square")
    text12.scale(1)
    text12.to_edge(UP)
    self.play(Write(text12))
    self.wait(2)
    square1 = Square(color=RED)
    self.play(ShowCreation(square1))
    self.wait(2)
    rectangle1 = Rectangle(color=RED)
    rectangle1.set_width(0.5)
    rectangle1.set_height(1)
    rectangle1.shift(0.5*DOWN)
    rectangle1.set_fill(RED,opacity=1)
    self.play(FadeIn(rectangle1))
    self.wait(4)
    self.play(FadeOut(text12))
    self.play(FadeOut(rectangle1))
    self.play(FadeOut(square1))
    
    text12 = TextMobject(r"Mathematically we can express it as $\frac{1}{2}$")
    self.play(Write(text12))
    self.wait(5)
    self.play(FadeOut(text12))

    text13 = TextMobject("Now lets look at a quarter of a circle")
    text13.to_edge(UP)
    self.play(Write(text13))
    self.wait(4)

    

    circle3 = Circle(color = PURPLE)
    self.play(ShowCreation(circle3))
   
    sector4 = Sector(0,1.57079)
    sector4.set_fill(PURPLE,opacity=1)
    self.play(ShowCreation(sector4))
    self.wait(3)
    self.play(FadeOut(sector4))

    sector5 = Sector(0,1.57079)
    sector5.set_fill(PURPLE,opacity=1)
    sector5.rotate(-4*TAU/8)
    sector5.shift(DOWN)
    sector5.shift(LEFT)
    self.play(ShowCreation(sector5))

    self.wait(3)
    self.play(FadeOut(sector5))
    self.play(FadeOut(text13))
    self.play(FadeOut(circle3))
    self.wait(3)
      
    text14 = TextMobject("Now lets look at a quarter of a square")
    text14.to_edge(UP)
    self.play(Write(text14))
    self.wait(1)

    square2 = Square(color = BLUE)
    self.play(ShowCreation(square2))

    square3 = Square(side_length=1,color=BLUE)
    square3.set_fill(BLUE,opacity =1)
    square3.shift(0.5*RIGHT)
    square3.shift(0.5*UP)
    self.play(ShowCreation(square3))
    self.wait(3)
    self.play(FadeOut(square3))

    square4 = Square(side_length=1,color=BLUE)
    square4.set_fill(BLUE,opacity =1)
    square4.shift(0.5*LEFT)
    square4.shift(0.5*DOWN)
    self.play(ShowCreation(square4))
    self.wait(3)
    self.play(FadeOut(square4))

    self.play(FadeOut(text14))
    self.play(FadeOut(square2))

    text15 = TextMobject(r"Mathematically we can express it as $\frac{1}{4}$")
    self.play(Write(text15))
    self.wait(5)
    self.play(FadeOut(text15))


    text16 = TextMobject("How about three quarters of a circle ?")
    text16.to_edge(UP)
    self.play(Write(text16))
    self.wait(2)

    

    circle4 = Circle(color = ORANGE)
    circle4.set_fill(ORANGE,opacity=1)
    self.play(ShowCreation(circle4))
    self.wait(2)
    sector6 = Sector(0,1.57079)
    sector6.set_fill(BLACK,opacity=1)
    self.play(ShowCreation(sector6))
    self.wait(5)
    self.play(FadeOut(circle4))
    self.play(FadeOut(sector6))
    self.play(FadeOut(text16))

    text17 = TextMobject("Or how about three quarters of a square ?")
    text17.to_edge(UP)
    self.play(Write(text17))
    self.wait(2)

    square5 = Square(color=ORANGE)
    square5.set_fill(ORANGE,opacity=1)
    self.play(ShowCreation(square5))
    

    square6 = Square(side_length=1,color=BLACK)
    square6.set_fill(BLACK,opacity =1)
    square6.shift(0.5*LEFT)
    square6.shift(0.5*DOWN)
    self.play(ShowCreation(square6))

    self.wait(5)

    self.play(FadeOut(text17))
    self.play(FadeOut(square5))
    self.play(FadeOut(square6))

    
    text18 = TextMobject(r"Mathematically we can express it as $\frac{3}{4}$")
    self.play(Write(text18))
    self.wait(5)
    self.play(FadeOut(text18))

    text19 = TextMobject("Anyways we conclude for today , thank you :)")
    self.play(Write(text19))
    self.wait(5)
    self.play(FadeOut(text19))

    
    

    

    

      

    

    
    
    

    
    

    

    

    

    
    

    
    
    
    
              
    
    
    
    
    

    
    
              
    
                        
