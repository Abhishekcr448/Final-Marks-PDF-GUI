from fpdf import FPDF
from tkinter import filedialog, messagebox


def generate_pdf(df, entry_text, root):
    """
    Generates a PDF file from a given DataFrame.

    Parameters:
    df (DataFrame): The DataFrame to generate the PDF from.

    Returns:
    None
    """


    def error_msg():
        """
        This msg is generated if there exsist an issue in reading the given excel sheet

        The msg guides to read the info_msg to give a suitable excel

        """
        # Set the font size of the messagebox to 14 using the '*font' option
        root.option_add('*font', 'Helvetica -14')

        # Show a error messagebox due to invalid excel file
        messagebox.showerror("Invalid Excel File", "The given execel file is unvalid.\n\nPlease read the info message about the requirments of the excel file")

        # Clear the font size set previously using option_add method
        root.option_clear()


    # If error occured in the file open_filedialog.py, error_mgs will be displayed
    if str(df) == "continue": 
        error_msg()
        return


    # Create a new PDF object
    pdf = FPDF()

    # Add a page to the PDF
    pdf.add_page()

    # Set the font for the PDF to Arial with a size of 11
    pdf.set_font("Arial", size=11)

    # Add the title text given in the entry box
    if entry_text != "":
        pdf.text(100-int(len(entry_text)/2), 5, entry_text)

    # Define the columns to be used in the PDF
    columns = ['PaperID', 'Examiner Marks',
               'Moderator One Marks', 'Remarks', 'Final Marks']

    # Loop over the columns and add a header cell for each column
    for i in range(len(columns)):
        pdf.cell(200/len(columns), 10, str(columns[i]), 1, align='C')

    # Add a line break after the headers
    pdf.ln()

    # Loop over the rows in the DataFrame
    for i in range(len(df.index)):
        # Loop over the columns in the DataFrame
        for j in range(len(df.columns)):
            # Add a cell for each value in the row
            pdf.cell(200/len(columns), 10, str(df.iloc[i, j]), 1, align='C')
        # Add a line break after each row
        pdf.ln()

    # Get the file path from the user to save the PDF
    file_path = filedialog.asksaveasfilename(defaultextension='.pdf')

    # Save the PDF to the specified file path
    pdf.output(file_path)
