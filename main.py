###This code will not work in repl.it as there is no access to the colorgram package here.###
##We talk about this in the video tutorials##
import colorgram

rgb_colors = []
colors = colorgram.extract('image.jpg', 30)
for color in colors:
    rgb_tuple = (color.rgb.r, color.rgb.g, color.rgb.b)
    rgb_colors.append(rgb_tuple)

rgb_colors =  rgb_colors[5:]
print(rgb_colors)

