import csv
import os
import re
from collections import defaultdict


class RunTest:
    def __init__(self):
        self.menu = None
        print("Initializing RunTest object")
        self.columns = None
        self.rows = list()
        self.test_name = {}

    def generate_signal_menu_mapping(self, data_list):
        result = defaultdict(list)
        for item in data_list:
            item = item.replace('-', '_')
            match = re.match(r'(\d+)', item)
            if match:
                key = match.group(0)
                result[key].append(item)
        result = {key: sorted(values) for key, values in result.items()}
        result = {value[0]: value for key, value in result.items()}
        return result

    def create_test_case_dict(self, csv_file_path, signal_name):
        print("Creating test case dict for signal: {} from CSV file: {}".format(signal_name, csv_file_path))
        try:
            with open(csv_file_path, mode='r') as file:
                self.rows = list(csv.reader(file))
                self.columns = self.rows[0][1:]
                values = self.rows[1][1:]
                if signal_name not in self.test_name:
                    self.test_name[signal_name] = {}
                for col_name, value in zip(self.columns, values):
                    self.test_name[signal_name][col_name] = value or 'None'
                print("Test case dict created for {}: {}".format(signal_name, self.test_name[signal_name]))
                self.menu = self.generate_signal_menu_mapping(self.columns)
        except Exception as e:
            print("Error occurred while reading the CSV: {}".format(e))

    def set_rigt_click_action_for_main_image(self, main_signal, wait_time=1):
        print("Setting right click action for main image: {}".format(main_signal))
        try:
            rightClick(Pattern("{}_R.png".format(main_signal)))
            type('H')
            wait(wait_time)
            type(Key.ENTER)
            wait(wait_time)
            print("Right click action set for main image: {}".format(main_signal))
        except Exception as e:
            print("Failed to set right click action for {}: {}".format(main_signal, e))

    def get_image_name(self, input_value):
        for key, values in self.menu.items():
            if input_value in values:
                return key
        return None

    def set_right_click_action_for_test_signal(self, test_signal, wait_time=1):
        print("Setting right click action for test signal: {}".format(test_signal))
        try:
            if test_signal.startswith("SH"):
                rightClick("{}_R.png".format(test_signal))
                type('H')
                type(Key.RIGHT)
                type(Key.ENTER)
                wait(5)
            else:
                print("menu++++++++", self.menu[signal_name][0], self.get_image_name(test_signal))
                position = self.menu[signal_name].index(test_signal) + 1
                rightClick(Pattern("{}_R.png".format(self.get_image_name(test_signal))))
                type('H')
                type(Key.RIGHT)
                for _ in range(position):
                    type('C')
                type(Key.ENTER)
                wait(wait_time)
            print("Right click action set for test signal: {}".format(test_signal))
        except Exception as e:
            print("Failed to set right click action for {}: {}".format(test_signal, e))

    def set_cancel_action(self, action_image, action, wait_time=1):
        print("Setting cancel action for {} with action {}".format(action_image, action))
        try:
            if exists(Pattern("{}_{}.png".format(action_image, action)).exact()):
                rightClick(Pattern("{}_{}.png".format(action_image, action)).exact())
                type('H')
                click('cancel.png')
                wait(wait_time)
                rightClick(Pattern("{}_R.png".format(action_image, action)).exact())
                type('H')
                click('release.png')
                wait(12)
            if exists(Pattern("{}_R.png".format(action_image)).exact()):
                print("cancel action for {} successful".format(action_image))
            else:
                print("cancel action for {} failed".format(action_image))
        except Exception as e:
            print("Failed to set cancel action for {}: {}".format(action_image, e))

    def create_and_run_action_for_test_case(self, csv_file_path, signal_name):
        self.create_test_case_dict(csv_file_path, signal_name)
        print("Creating actions for test cases")
        try:
            for signal_name in self.test_name.keys():
                print("Processing signal: {}".format(signal_name))
                print("{}_R.png".format(signal_name))
                if exists(Pattern("{}_R.png".format(signal_name))):
                    self.set_rigt_click_action_for_main_image(signal_name)
                    if exists(Pattern("{}_Y.png".format(signal_name))):
                        print(self.test_name, self.test_name[signal_name])
                        for test_signal, value in self.test_name[signal_name].items():
                            if value != 'None':
                                print("signal menu", signal_name)
                                self.set_right_click_action_for_test_signal(test_signal)
                                if value.lower() in ['p', 'x']:
                                    if not exists(Pattern("{}_R.png".format(test_signal))):
                                        print("Test case failed for test signal: {} with main signal {}".format(
                                            test_signal,
                                            signal_name))
                                    else:
                                        print("Test case passed for test signal: {} with main signal {}".format(
                                            test_signal,
                                            signal_name))
                                    self.set_cancel_action(test_signal, 'R')
                                else:
                                    if exists(Pattern("{}_Y.png".format(test_signal))):
                                        print("Test case passed for test signal: {} with main signal {}".format(
                                            test_signal,
                                            signal_name))
                                self.set_cancel_action(test_signal, 'Y')
                        self.set_cancel_action(signal_name, 'Y')
                    else:
                        print("Unable to set main signal {}".format(signal_name))
                else:
                    print("Error finding main signal image {}".format(signal_name))
        except Exception as e:
            print("Error occurred while creating actions for test cases: {}".format(e))


if __name__ == "__main__":
    test_runner = RunTest()
    csv_file_path = "D:\\signal\\test-signal\\test_signal\\Generate.sikuli\\signal_sheet.csv"
    signal_name = "1L1"
    test_runner.create_and_run_action_for_test_case(csv_file_path, signal_name)
