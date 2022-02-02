import os
from abc import abstractmethod
import numpy as np

class Analysis():
    '''
    Analysis object that performs some operation on your *data*
    after calling *main* method.
    '''
    def __init__(self, name : str, description : str = '') -> None:
        self.name = name
        self.description = description
        self.complete = False
        self.results = None

    def load_data(self, data : np.ndarray):
        self.data = data
    
    @abstractmethod
    def run(self):
        pass
    
    def check_if_completed(self):
        return self.complete is True

    def set_complete(self, status : bool):
        self.complete = status

    def details(self) -> str:
        return self.description

    def __str__(self) -> str:
        desc = f' ({self.description}) ' if len(self.description) > 0 else ' '
        return f'Analysis {self.name}{desc}\n' +\
            str(self.results) + '\n' + '-' * 5

class AnalysisCounter(Analysis):

    def run(self):
        '''This counts number of occurences in a vector'''
        from collections import Counter
        self.results = Counter(self.data)

class Report(object):
    '''
    Report collects and prints out the results of all analyses.
    '''
    def __init__(self, name : str) -> None:
        self.name = name
        self.analyses = []

    def add_analysis(self, analysis : Analysis):
        self.analyses.append(analysis)

    def generate(self, only_completed : bool = True):
        # Print analysis results only if it is completed
        for a in self.analyses:
            if only_completed and a.check_if_completed():
                print(a)
                continue
            print(a)

# example of how to use Analysis and Report
ac = AnalysisCounter('counter', 'This counts number of occurences in a vector')
ac.load_data(np.array([1,4,1,3,5,6,7,3]))
ac.run()
ac.set_complete(True)

report = Report('my final report')
report.add_analysis(ac)

report.generate()