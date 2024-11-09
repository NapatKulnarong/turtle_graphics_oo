Polygon Art Generator

Overview
This program generates different types of polygonal art using Turtle. The user can select a number between 1 and 9 
to generate various patterns made from polygons of different sizes, colors, and arrangements. The program utilizes 
three classes: Polygon, PolygonArt, and EmbeddedPolygon to perform the task.

Classes
1. Polygon: Represents a single polygon and includes methods for drawing and moving it to different locations on the screen.
2. PolygonArt: Manages the setup and execution of the art generation process, including generating random colors and prompting the user for input.
3. EmbeddedPolygon: A subclass of Polygon that generates nested polygons with smaller sizes at each level, creating an embedded effect.
________________________________________________________________________________________________________________________
HOW TO RUN THE PROGRAM

Requirements
- Python 3.X
- turtle graphics library 

How to use or modify this project
1. CLONE or DOWNLOAD this project.
2. OPEN the project in your preferred IDE.
3. RUN the program
4. the program will prompt you to ENTER a number between 1 and 9. Each choice generates a different type of pattern
   (1) Generate polygons with 3 sides (triangle) 
   (2) Generate polygons with 4 sides (square)
   (3) Generate polygons with 5 sides (pentagon)
   (4) Generate different types of polygon (mixed with 3, 4, and 5 sides)
   (5) Generate nested polygons with 3 sides (triangle)
   (6) Generate nested polygons with 4 sides (square)
   (7) Generate nested polygons with 5 sides (pentagon)
   (8) Generate different types of nested polygon (mixed with 3, 4, and 5 sides)
   (9) Generate different types of simple and nested polygon (mixed with 3, 4, and 5 sides)

Features
- Randomly generated colors using RGB values.
- Adjustable size, orientation, location, and border thickness for each polygon.
- Ability to generate both simple and embedded polygons with multiple levels of recursion.
________________________________________________________________________________________________________________________
