#!/usr/bin/perl

open(TFILE, "/home/pi/house_monitor_files/homelog.txt");
# Count lines in file, and output at most last 50 lines
$cnt = 0;
while (<TFILE>) {
	$cnt++;
}
close(TFILE);


open(TFILE, "/home/pi/house_monitor_files/homelog.txt");
print "<ol>";
while (<TFILE>) {
	if ( $cnt-- < 50 ) {
		chomp;
		print "<li>$_</li>\n";
	}
}
print "</ol>\n";


