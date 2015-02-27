from rrutil import *

send_gdb('break string_store\n')
expect_gdb('Breakpoint 1')

# string_store 1-byte forwards
send_gdb('c\n')
expect_gdb('Breakpoint 1')
send_gdb('finish\n')
send_gdb('watch -l p[1000000]\n')
expect_gdb('watchpoint')
send_gdb('reverse-continue\n')
expect_gdb('Old value = 97')
expect_gdb('New value = 0')
send_gdb('p p[999999]\n')
expect_gdb('= 97')
send_gdb('p p[1000000]\n')
expect_gdb('= 0')
send_gdb('p p[1000001]\n')
expect_gdb('= 0')
send_gdb('disable\n')
send_gdb('enable 1\n')

# string_store 1-byte backwards
send_gdb('c\n')
expect_gdb('Breakpoint 1')
send_gdb('finish\n')
send_gdb('watch -l p[1000000]\n')
expect_gdb('watchpoint')
send_gdb('reverse-continue\n')
expect_gdb('Old value = 98')
expect_gdb('New value = 97')
send_gdb('p p[1000001]\n')
expect_gdb('= 98')
send_gdb('p p[1000000]\n')
expect_gdb('= 97')
send_gdb('p p[999999]\n')
expect_gdb('= 97')
send_gdb('disable\n')
send_gdb('enable 1\n')

# string_store 2-bytes forwards
send_gdb('c\n')
expect_gdb('Breakpoint 1')
send_gdb('finish\n')
send_gdb('watch -l p[1000001]\n')
expect_gdb('watchpoint')
send_gdb('reverse-continue\n')
expect_gdb('Old value = 97')
expect_gdb('New value = 0')
send_gdb('p p[999999]\n')
expect_gdb('= 97')
send_gdb('p p[1000000]\n')
expect_gdb('= 0')
send_gdb('p p[1000001]\n')
expect_gdb('= 0')
send_gdb('disable\n')
send_gdb('enable 1\n')

# string_store 2-bytes backwards
# Check that a watch at the end of the loop is OK
send_gdb('c\n')
expect_gdb('Breakpoint 1')
send_gdb('finish\n')
send_gdb('watch -l p[0]\n')
expect_gdb('watchpoint')
send_gdb('reverse-continue\n')
expect_gdb('Old value = 98')
expect_gdb('New value = 97')
send_gdb('p p[0]\n')
expect_gdb('= 97')
send_gdb('disable\n')
send_gdb('enable 1\n')

# string_store 4-bytes forwards
# Just check that the late-watchpoint quirk is suppressed
send_gdb('c\n')
expect_gdb('Breakpoint 1')
send_gdb('watch -l p[800000]\n')
expect_gdb('watchpoint')
send_gdb('continue\n')
expect_gdb('Old value = 0')
expect_gdb('New value = 97')
send_gdb('p p[800003]\n')
expect_gdb('= 97')
send_gdb('p p[800004]\n')
expect_gdb('= 0')

ok()
