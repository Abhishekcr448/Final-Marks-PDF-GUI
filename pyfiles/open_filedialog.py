from tkinter import filedialog
import pandas as pd
import pyexcel_ods


def open_file():
    """
    This function opens a file using filedialog.askopenfilename() and returns a pandas dataframe.
    The file should either be in .xls (Excel) format or .ods (OpenOffice) format. 
    The returned dataframe has three columns - 'PaperID', 'Examiner Marks', 'Moderator One Marks', and a calculated 'Final Marks' column.

    """

    try:
        # Taking the excel file through input filedialog
        file_path = filedialog.askopenfilename()
        file_extension = file_path.split(".")[-1]
        if file_extension == 'xls':
            df = pd.read_excel(file_path)
        elif file_extension == 'ods':
            df = pd.DataFrame(pyexcel_ods.get_data(file_path)['Sheet1'])

        # Checking the number of columns
        assert len(df.columns) == 4, "Invalid number of columns"

        # converting columns to numeric values and handle errors
        df[1] = pd.to_numeric(df[1], errors='coerce')
        df[2] = pd.to_numeric(df[2], errors='coerce')

        # calculate the final marks based on the conditions
        df['Final Marks'] = df.apply(lambda x: x[1] if ((x[1] - x[2])/x[1])*100 <= 5 else
                                        x[2] if ((x[1] - x[2])/x[1])*100 <= 15 else
                                        (x[1] + x[2])/2 if ((x[1] - x[2])/x[1])*100 <= 25 else
                                        'Rechecking Required', axis=1)
    except Exception as e:
        return "continue"
    
    else:
        return df
