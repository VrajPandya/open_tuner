class OtContext:
    """Keeps the track of current program"""

    def __init__(self, kernel_file, kernel_name, output_file):
        self.kernel_file = kernel_file
        self.kernel_name = kernel_name
        self.output_file = output_file
