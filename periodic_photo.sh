#!/bin/bash
#
# Script to be run by www-data user cron to take and save
# photo in /var/www/data so it is available from web site.

raspistill -vf -hf -w 300 -h 300 -o "/var/www/data/image_`date +%Y-%m-%d_%H:%M:%S`.jpg"

