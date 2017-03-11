class OtContext:
    """Keeps the track of current program"""

    kernel_file = ""
    kernel_name = ""
    output_file = ""

    def __init__(self, kernel_file, kernel_name, output_file):
        OtContext.kernel_file = kernel_file
        OtContext.kernel_name = kernel_name
        OtContext.output_file = output_file
