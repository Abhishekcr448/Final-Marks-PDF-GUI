def center(win):
    """
    centers a tkinter window
    :param win: the main window or Toplevel window to center

    """

    # Update any pending geometry management requests
    win.update_idletasks()

    # Get the width of the window
    width = win.winfo_width()

    # Get the width of the window frame
    frm_width = win.winfo_rootx() - win.winfo_x()

    # Calculate the total width of the window including the frame
    win_width = width + 2 * frm_width

    # Get the height of the window
    height = win.winfo_height()

    # Get the height of the title bar
    titlebar_height = win.winfo_rooty() - win.winfo_y()

    # Calculate the total height of the window including the title bar and frame
    win_height = height + titlebar_height + frm_width

    # Calculate the x-coordinate to center the window on the screen
    x = win.winfo_screenwidth() // 2 - win_width // 2

    # Calculate the y-coordinate to center the window on the screen
    y = win.winfo_screenheight() // 2 - win_height // 2

    # Set the window geometry to center the window on the screen
    win.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    # Make the window visible
    win.deiconify()
