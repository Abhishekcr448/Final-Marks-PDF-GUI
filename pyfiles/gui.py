import tkinter as tk
from tkinter import messagebox
from pyfiles import open_filedialog, center_window, create_pdf


def create_window():
    """
    Create GUI using Tkinter

    This function creates a GUI window using Tkinter library. The window has a button to open a file dialog
    and another button to show information about the app.

    Attributes:
    root (tk.Tk): The main window for GUI
    canvas1 (tk.Canvas): The canvas for background image and buttons
    photo (tk.PhotoImage): Image to be displayed on the info button
    info_button (tk.Button): Button to show information about the app
    generate_pdf_button (tk.Button): Button to open the file dialog and generate pdf
    info_button_canvas (int): The canvas window for the info button
    button1_canvas (int): The canvas window for the generate pdf button

    """

    def info_msg():
        """
        info_msg - A function to show the information message about the app

        This function shows a messagebox with information about the app. The message details the expected columns in the excel file and the calculation of final marks based on the difference between the examiner and moderator marks. The font size of the messagebox is also set using the option_add method.

        """
        # Set the font size of the messagebox to 14 using the '*font' option
        root.option_add('*font', 'Helvetica -14')

        # Show a messagebox with the information about the app
        messagebox.showinfo("Info", "The excel file should have columns as:-'PaperID', 'Examiner Marks','Moderator One Marks', 'Remarks'\n\nIf the difference between the 'Examiner Marks' and 'Moderator One Marks' is \n1)0-5 % then final marks is 'Examiner Marks'.\n2) 5-15% then the final marks is 'Moderator One Marks'.\n3)15-25% then the final marks is average of both examiner and moderator marks .\n4)25-100% then final mark is 'Rechecking required'.")

        # Clear the font size set previously using option_add method
        root.option_clear()


    show = True

    def on_click():
        """
        This function is responsible for the hiding and un-hiding of the entry field,
        according to the checkbox value

        """

        nonlocal show

        # Determine if the checkbox is hidden or not
        if show:
            canvas1.itemconfig(7, state='normal')
            show = False
        else:
            canvas1.itemconfig(7, state='hidden')
            show = True

    # Create the main window of the GUI using tkinter
    root = tk.Tk()

    # Set the minimum and maximum size of the window
    root.minsize(400, 200)
    root.maxsize(400, 200)

    # Center the window on the screen
    center_window.center(root)

    # Load the background image from a file
    bg = tk.PhotoImage(file="Resources/bg1.png")

    # Set the title of the window
    root.title("Marksheet Generator")

    # Create a canvas to display the background image and other widgets
    canvas1 = tk.Canvas(root, width=400, height=200)
    canvas1.pack(fill="both", expand=True)

    # Display the background image on the canvas
    canvas1.create_image(0, 0, image=bg, anchor="nw")

    # Load photo image
    photo = tk.PhotoImage(file="Resources/infoImage.png")

    # Create Info button
    info_button = tk.Button(root, image=photo, command=info_msg)
    canvas1.create_window(380, 20, window=info_button)

    # Create Generate PDF button
    generate_pdf_button = tk.Button(text="Generate PDF",
                                    command=lambda: create_pdf.generate_pdf(open_filedialog.open_file(), entry.get(), root), font=("TkDefaultFont", 14))

    canvas1.create_window(200, 170, window=generate_pdf_button)

    # Adding text of steps on the canvas1
    canvas1.create_text(200, 20, text="Step 1: Tap on Generate PDF")
    canvas1.create_text(
        200, 50, text="Step 2: Select your required excel file")
    canvas1.create_text(
        200, 80, text="Step 3: Save it on your desired location")

    # Adding entry field
    chekbox_var = tk.IntVar()
    entry = tk.Entry(root)
    canvas1.create_window(250, 120, window=entry)
    canvas1.itemconfig(7, state='hidden')

    # Adding checkbox
    checkbox_entry = tk.Checkbutton(
        root, text="Add Title", variable=chekbox_var, command=on_click)
    canvas1.create_window(100, 120, window=checkbox_entry)

    # Looping the window
    root.mainloop()
