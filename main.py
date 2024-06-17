# Python's built-in support for JSON
import json
# Python turtle library for creating designs and images ONLY gifs
import turtle
# Python module for fetching URLs
import urllib.request
# Python module for time-related functions
import time
# Python module for opening URLs in a web browser
import webbrowser
# Python module for retrieving latitude and longitude
import geocoder

# load the current status of the ISS in real-time
url = "http://api.open-notify.org/astros.json"
response = urllib.request.urlopen(url)
result = json.loads(response.read())
# print(result)
# print(result.keys())

# Create.txt file for astronauts info
file = open("iss.txt", "w")
file.write("There are currently " + str(result["number"]) + " astronauts on the ISS: \n\n")
people = result["people"]

# prints names of crew
for p in people:
    file.write(p['name'] + " - on board" + "\n")
# print long and lat
g = geocoder.ip('me')
file.write("\nYour current lat / long is: " + str(g.latlng))
file.close()
webbrowser.open("iss.txt")

# Setting Up The World Map
screen = turtle.Screen()
screen.setup(1280, 720)
# load the world map image
screen.bgpic("images/map.gif")
screen.setworldcoordinates(-180, -90, 180, 90)

# Create the turtle
map_turtle = turtle.Turtle()
map_turtle.speed(0)  # Set the turtle speed to the maximum


# Function to draw longitude and latitude lines
def draw_grid():
    # Draw longitude lines
    for longitude in range(-180, 181, 15):
        map_turtle.penup()
        map_turtle.goto(longitude, -90)
        map_turtle.pendown()
        map_turtle.goto(longitude, 90)

    # Draw latitude lines
    for latitude in range(-90, 91, 15):
        map_turtle.penup()
        map_turtle.goto(-180, latitude)
        map_turtle.pendown()
        map_turtle.goto(180, latitude)


# Draw the grid
draw_grid()

# Hide the turtle after drawing
map_turtle.hideturtle()

# Finish drawing
turtle.done()

screen.register_shape("images/iss.gif")
iss = turtle.Turtle()
iss.shape("images/iss.gif")
iss.setheading(45)
iss.penup()

while True:
    # load the current status of the ISS in real-time
    url = "http://api.open-notify.org/iss-now.json"
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    # Extract the ISS location
    location = result["iss_position"]
    lat = location['latitude']
    lon = location['longitude']

    # Output lon and lat to the terminal in the float format
    lat = float(lat)
    lon = float(lon)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(lon))

    # Update the ISS location on the map
    iss.goto(lon, lat)

    # Refresh each 5 seconds
    time.sleep(10)


