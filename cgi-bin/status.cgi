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
echo "<p>"

# Old graph type: new one uses gnuplot:
#/home/pi/house_monitor_files/prepplot.py >/var/www/data/tempdata.txt
#graph -T png -Y "Deg. F" -h .7 -w .7 -g 3 -X "Data point from table below"  /var/www/data/tempdata.txt >/var/www/data/tempdata.png
# Image files need to be in apache root (/var/www)
#echo "<img src=\"../data/tempdata.png\" height=\"600\" width=\"600\">"

# Build gnuplot graph of temperatures in
# /var/www/data directory: tempdata.gif
# from arduino records in /home/pi/house_monitor_files/homelog.txt
# creating intermediate files t1.txt, t2.txt

pushd /var/www/data >/dev/null

/home/pi/house_monitor_files/prep-gnuplot.py \
        /home/pi/house_monitor_files/homelog.txt t1.txt t2.txt
gnuplot /home/pi/house_monitor_files/tempplot.gp >tempdata.gif

popd >/dev/null

echo "<center>"
echo "<img src=\"../data/tempdata.gif\" >"
echo "</center>"
echo "</p>"

echo "<h2>Last 50 temperature records</h2>"
echo "<p>"

echo "<style>"
echo "li {font-size:0.9em;}"
echo "</style>"

# Get the last 50 temperature records in html
# list form and send to stdout:

/home/pi/house_monitor_files/gettemps.pl

echo "</p>"

echo "</body>"
echo </html>
