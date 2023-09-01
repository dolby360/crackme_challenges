# Sample .gdbinit configuration

# Set a breakpoint at the specified address
# sVar3 = strcspn(B,"\n");
break *0x004009d2

# Automatically continue after hitting the breakpoint
c
