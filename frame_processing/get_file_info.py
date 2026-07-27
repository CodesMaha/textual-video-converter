""" determine data for video such as filename """

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