#!/usr/bin/perl
# 
# Get last several temperatures from t1.txt and t2.txt
# and send to stdout
#
open(T1FILE, "/home/pi/house_monitor_files/t1.txt");
open(T2FILE, "/home/pi/house_monitor_files/t2.txt");

# Count lines in file, and output at most last 50 lines
# Assume t1.txt and t2.txt have same # lines...

$nlines = 0;
while (<T1FILE>) {
	$nlines++;
}
close(T1FILE);
close(T2FILE);

open(T1FILE, "/home/pi/house_monitor_files/t1.txt");
open(T2FILE, "/home/pi/house_monitor_files/t2.txt");

print "<ol>\n";
print "<pre>\n";
$n = $nlines;
while ( $n-- > 0) {
	$t1 = <T1FILE>;
	chomp( $t1 );
	$t2 = <T2FILE>;
	chomp( $t2 );
	if ( $n < 10 ) {
		print ("<li>T1: $t1            T2: $t2</li>\n");
	}
}
print "</pre>\n";
print "</ol>\n";


