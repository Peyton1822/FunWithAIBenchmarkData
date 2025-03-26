# File Name : dataVisualization.py
# Student Name: Peyton Bock
# email:  bockps@mail.uc.edu
# Assignment Number: Assignment 08 
# Due Date:   3/27/2025
# Course #/Section:   4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  add an image of our team mascot and visualize some data from the repo. 
# Brief Description of what this module does. Use IDE, develop code using outside problems and recourses
# Citations: I used ChatGPT and Gemini

import csv
import collections
import turtle

def read_csv(filename):
    """Reads the CSV file and extracts the correct answers from column 5."""
    correct_answers = []
    with open(filename, 'r', newline='', encoding='utf-8') as file:
        reader = csv.reader(file)
        for row in reader:
            if len(row) > 5:
                correct_answers.append(row[5])
    return correct_answers

def count_answers(correct_answers):
    """Counts the frequency of each correct answer."""
    return collections.Counter(correct_answers)

def draw_bar_chart(answer_counts):
    """Draws a bar chart using the turtle module."""
    screen = turtle.Screen()
    screen.title("Most Common Correct Answers")
    screen.bgcolor("white")
    
    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-200, -200)
    t.pendown()
    
    max_count = max(answer_counts.values())
    bar_width = 50
    spacing = 20
    x_start = -200
    
    for i, (answer, count) in enumerate(answer_counts.items()):
        t.penup()
        t.goto(x_start + i * (bar_width + spacing), -200)
        t.pendown()
        t.fillcolor("blue")
        t.begin_fill()
        for _ in range(2):
            t.forward(bar_width)
            t.left(90)
            t.forward(count * (200 / max_count))  # Normalize height
            t.left(90)
        t.end_fill()
        
        # Label the bars
        t.penup()
        t.goto(x_start + i * (bar_width + spacing) + 10, -220)
        t.write(answer, align="left", font=("Arial", 10, "normal"))
    
    turtle.done()

def visualize_data(filename):
    """Runs the full pipeline to read, count, and visualize the data."""
    correct_answers = read_csv(filename)
    answer_counts = count_answers(correct_answers)
    draw_bar_chart(answer_counts)