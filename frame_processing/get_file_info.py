""" determine data for video such as filename """

from tkinter.filedialog import askopenfilename

def get_filename(file_types: tuple[tuple[str]]) -> str:
    """ use tk for file directory selection """
    fn: str = askopenfilename(
        title="select video", initialdir=".", 
        filetypes=file_types
    )
    if not fn:
        raise ValueError("no input video selected for conversion")

    return fn

def reformat_filename(
        filename: str, to_insert: str, f_extension: str
    ) -> str:
    """ args: fn is filename to convert.
    f_extension is later extension like .mp4. 
    to_insert is the change in name. \n
    example.gif -> example_textual.mp4
    """
    return "".join((
        filename.rsplit('.', 1)[0], 
        to_insert, f_extension
    ))