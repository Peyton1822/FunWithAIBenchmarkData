# File Name : image.py
# Student Name: Peter Phan
# email:  phanpv@mail.uc.edu
# Assignment Number: Assignment 08
# Due Date:   03/27/2025
# Course #/Section:   IS4010-001
# Semester/Year:   Spring 2025
# Brief Description of the assignment:  Display image of our team name that should be around 200x200 pixels.
#                                       and perform something interesting with the data visually. 

# Brief Description of what this module does. Learn how to access databases and manipulate data from them 
# Citations: I used Gemini
# Anything else that's relevant:

from PIL import Image, ImageDraw, ImageFont
import requests
from io import BytesIO

def display_team_image():
    """Displays an image indicative of the team's name using Pillow."""
    try:
        image_url = "https://static.wikia.nocookie.net/sifsbeastiary/images/4/43/Bulbasaur.png/revision/latest?cb=20140504214415"

        response = requests.get(image_url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)

        img = Image.open(BytesIO(response.content))
        img.show()  # Display the image directly

    except requests.exceptions.RequestException as e:
        print(f"Error fetching image: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

