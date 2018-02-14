
# from the other end, run:  time { dd if=/dev/zero bs=1000000 count=5000 | nc px.bot.nu 1888; }  
socat  tcp-l:1888,fork exec:'sh -c "{ cat | wc -c; } " '
