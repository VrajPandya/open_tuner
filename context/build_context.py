class OtContext:
    """Keeps the track of build system process and variables """

    def __init__(self, root_dir, cwd):
        self.root_dir = root_dir
        self.cwd = cwd

