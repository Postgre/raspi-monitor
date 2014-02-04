#!/bin/bash
# 
# Build house status web page with temperature plots
# and other ststus info, and send to stdout back to
# the web browser to render.
# 

echo -e "Content-type: text/html\n\n"

echo "<html>"
echo "<head>"
echo "<title>Zouck Home Status</title>"
echo "</head>"
echo "<body>"
echo "<h1 class="size"><center>Zouck Home Status</center></h1>"
echo "<p><center>Current time is `date`</center>"
echo "<center>Uptime: `uptime`</center>"
echo "<center>In directory: `pwd`</center>"
echo "</p>"

gnuplot /home/pi/house_monitor_files/tempplot.gp >/var/www/data/tempdata.gif

echo "<p>"
echo "<center>"
echo "<img src=\"../data/tempdata.gif\" >"
echo "</center>"
echo "</p>"

echo "<h2>Last 10 temperature records</h2>"
echo "<p>"

echo "<style>"
echo "li {font-size:0.9em;}"
echo "</style>"

# Get the last 10 temperature records in html
# list form and send to stdout:

/home/pi/house_monitor_files/gettemps-plot.pl

echo "</p>"

echo "</body>"
echo "</html>"
