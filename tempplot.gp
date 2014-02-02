# Plot temperatures and send output to stdout
#
# Use:
#
#   $ gnuplot tempplot.gp >temps.gif
#
set title "Home Temperature Record"
set terminal gif
# set output "temps.gif"
set xdata time
set timefmt "%Y-%m-%d %H:%M:%S"
set format x "%a\n%H:%M" 
set size ratio .5
set ytics font "sans,10"
set xtics font "sans,10"
set ylabel "Deg. F" font "sans, 10"
set key font "sans,10"
set grid

plot "t1.txt" using 1:3 title "Outdoor Temp" with line, "t2.txt" using 1:3 title "Indoor Temp" with line

