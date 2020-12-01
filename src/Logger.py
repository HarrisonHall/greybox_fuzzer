class Logger():
    def __init__(self):
        self.branch_counts = []

    def log(self, run, branch):
        self.branch_counts.append(branch)

    def __str__(self):
        return self.__repr__()

    def __repr__(self):
        return str(self.branch_counts)

    def csv(self):
        for i, count in enumerate(self.branch_counts):
            print(f"{i},{count}")
