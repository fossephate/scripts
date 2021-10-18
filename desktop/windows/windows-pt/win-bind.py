import keyboard
# keyboard.add_hotkey('space', lambda: print('space was pressed!'))
# # If the program finishes, the hotkey is not in effect anymore.

# # Don't do this! This will use 100% of your CPU.
# #while True: pass

# # Use this instead
# keyboard.wait()



def on_win_key(e):
    print("win-key-pressed")
    print(e)


# keyboard.hook_key("win", on_win_key, suppress=True)




keyboard.wait()