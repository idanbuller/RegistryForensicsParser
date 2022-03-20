import pandas as pd
import csv
from collections import Counter
from matplotlib import pyplot as plt
from matplotlib import cycler
from prettytable import PrettyTable


class AppCompatCacheParserAnalysis:

    def __init__(self):  # More features will be added
        self.data = pd.read_csv("Registry.csv")
        self.colors = cycler('color',
                             ['#EE6666', '#3388BB', '#9988DD',
                              '#EECC55', '#88BB44', '#FFBBBB'])

    def exe_currentVersion(self):
        values = self.data['ValueData'].tolist()
        keys = self.data['KeyPath'].tolist()
        values_to_table = []
        keys_to_table = []
        for i in values:
            if '.exe' in str(i):
                if "ROOT\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" not in keys[values.index(i)]:
                    continue
                else:
                    values_to_table.append(str(i))
                    keys_to_table.append(keys[values.index(i)])

        executablesTable = PrettyTable()
        columns = ["Key Path", "Value Data"]
        executablesTable.add_column(columns[0], keys_to_table)
        executablesTable.add_column(columns[1], values_to_table)
        print(executablesTable)

    def dll_currentVersion(self):
        values = self.data['ValueData'].tolist()
        keys = self.data['KeyPath'].tolist()
        values_to_table = []
        keys_to_table = []
        for i in values:
            if '.dll' in str(i):
                if "ROOT\SOFTWARE\Microsoft\Windows\CurrentVersion\Run" not in keys[values.index(i)]:
                    continue
                else:
                    values_to_table.append(str(i))
                    keys_to_table.append(keys[values.index(i)])

        executablesTable = PrettyTable()
        columns = ["Key Path", "Value Data"]
        executablesTable.add_column(columns[0], keys_to_table)
        executablesTable.add_column(columns[1], values_to_table)
        print(executablesTable)

    def userAssist(self):
        values = self.data['ValueData'].tolist()
        keys = self.data['KeyPath'].tolist()
        values_to_table = []
        keys_to_table = []
        for i in values:
            if '.exe' in str(i):
                if "userassist" not in keys[values.index(i)]:
                    continue
                else:
                    values_to_table.append(str(i))
                    keys_to_table.append(keys[values.index(i)])

        executablesTable = PrettyTable()
        columns = ["Key Path", "Value Data"]
        executablesTable.add_column(columns[0], keys_to_table)
        executablesTable.add_column(columns[1], values_to_table)
        print(executablesTable)

    def stats(self):
        hives_counter = Counter()
        pathes_counter = Counter()
        valueData_counter = Counter()
        hives = self.data['HivePath'].tolist()
        pathes = self.data['KeyPath'].tolist()
        valueData = self.data['ValueData'].tolist()
        hives_counter.update(hives)
        pathes_counter.update(pathes)
        valueData_counter.update(valueData)

        executablesTable = PrettyTable()
        columns = ["Top 3 Hives Pathes", "Top 3 Pathes", "Top 3 Values"]
        executablesTable.add_column(columns[0], hives_counter.most_common(3))
        executablesTable.add_column(columns[1], pathes_counter.most_common(3))
        executablesTable.add_column(columns[2], valueData_counter.most_common(3))
        print(executablesTable)


executor = AppCompatCacheParserAnalysis()
while True:
    user_input = str(input("""
    What would you like to analyze?
    1 - Executable files running from with startup
    2 - DLL files running from with startup
    3 - Executable files running from with GUI startup
    4 - Keys Stats
    >> """))
    if user_input == "1":
        print("Executable files running from with startup")
        executor.exe_currentVersion()
    if user_input == "2":
        print("DLL files running from with startup")
        executor.dll_currentVersion()
    if user_input == "3":
        print("Executable files running from with GUI startup")
        executor.userAssist()
    if user_input == "4":
        print("Keys Stats")
        executor.stats()
