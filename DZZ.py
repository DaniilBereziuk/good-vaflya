from colorama import Fore, Back, Style
print(Fore.BLUE + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
print('')

# Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
# Style: DIM, NORMAL, BRIGHT, RESET_ALL


print(f'Function Fore do TEXT with diffrent colors like {Fore.RED + 'red text'}{Fore.RESET + ' this or'} {Fore.BLUE + 'blue text'}{Fore.RESET + ' this'}')
print(f'Function Back do BACK TEXT with diffrent colors like {Back.YELLOW + 'yellow back'}{Back.RESET + ' this or'} {Back.WHITE + 'white back'}{Back.RESET + ' this'}')

print('')

# ESC [ 0 m       # reset all (colors and brightness)
# ESC [ 1 m       # bright
# ESC [ 2 m       # dim (looks same as normal brightness)
# ESC [ 22 m      # normal brightness
#
# # FOREGROUND:
# ESC [ 30 m      # black
# ESC [ 31 m      # red
# ESC [ 32 m      # green
# ESC [ 33 m      # yellow
# ESC [ 34 m      # blue
# ESC [ 35 m      # magenta
# ESC [ 36 m      # cyan
# ESC [ 37 m      # white
# ESC [ 39 m      # reset
#
# # BACKGROUND
# ESC [ 40 m      # black
# ESC [ 41 m      # red
# ESC [ 42 m      # green
# ESC [ 43 m      # yellow
# ESC [ 44 m      # blue
# ESC [ 45 m      # magenta
# ESC [ 46 m      # cyan
# ESC [ 47 m      # white
# ESC [ 49 m      # reset
#
# # cursor positioning
# ESC [ y;x H     # position cursor at x across, y down
# ESC [ y;x f     # position cursor at x across, y down
# ESC [ n A       # move cursor n lines up
# ESC [ n B       # move cursor n lines down
# ESC [ n C       # move cursor n characters forward
# ESC [ n D       # move cursor n characters backward
#
# # clear the screen
# ESC [ mode J    # clear the screen
#
# # clear the line
# ESC [ mode K    # clear the line

print('\033[31m' + 'some red text')
print('\033[39m') # and reset to default color




















