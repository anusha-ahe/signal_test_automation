import csv
import os
import re
from collections import defaultdict
from datetime import datetime


class RunTest:
    def __init__(self):
        self.c_menu = None
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

    def generate_c_signal_menu_mapping(self, data_list):
        result = defaultdict(list)
        for item in data_list:
            if item.startswith('C-'):
                base_item = item[2:].replace('-', '_')
                match = re.match(r'(\d+)', base_item)
                if match:
                    key = match.group(0)
                    result[key].append(item)
        result = {key: sorted(values) for key, values in result.items()}
        result = {value[0].split('C-')[-1]: [x.replace('-', '_') for x in value] for key, value in result.items()}
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
                self.c_menu = self.generate_c_signal_menu_mapping(self.columns)
                print("menu", self.menu)
                print(self.columns)
                print("c_menu", self.c_menu)
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

    def get_image_name(self, input_value, c_menu=None):
        if c_menu:
            menu = self.c_menu
        else:
            menu = self.menu
        for key, values in menu.items():
            if input_value in values:
                return key
        return None

    def set_right_click_action_for_test_signal(self, test_signal, wait_time=1):
        print("Setting right click action for test signal: {}".format(test_signal))
        try:
            test_signal = test_signal.replace('-', '_')
            if test_signal.startswith('C'):
                image_name = self.get_image_name(test_signal, True)
                position = self.c_menu[image_name].index(test_signal) + 1
            else:
                image_name = self.get_image_name(test_signal)
                position = self.menu[image_name].index(test_signal) + 1
            print("-----", image_name, self.menu)
            print("menu++++++++", self.menu[signal_name][0], image_name, self.menu[image_name])
            print("position", position)
            rightClick(Pattern("{}_R.png".format(image_name)))
            if test_signal.startswith('C'):
                type('C')
            else:
                type('H')
            type(Key.RIGHT)
            for _ in range(position):
                type('C')
            type(Key.ENTER)
            wait(wait_time)
            print("Right click action set for test signal: {}".format(test_signal))
        except Exception as e:
            print("Failed to set right click action for test signal {}: {}".format(test_signal, e))

    def set_cancel_action(self, action_image, action, wait_time=1, test_signal=True):
        action_image = action_image.replace('-', '_')
        if test_signal == True:
            if action_image.startswith('C'):
                action_image = self.get_image_name(action_image, True)
            else:
                action_image = self.get_image_name(action_image)
        print("Setting cancel action for {} with action {}".format(action_image, action))
        try:
            if exists(Pattern("{}_{}.png".format(action_image, action)).exact()):
                rightClick(Pattern("{}_{}.png".format(action_image, action)).exact())
                if action_image.startswith('C'):
                    type('C')
                else:
                    type('H')
                click('cancel.png')
                wait(wait_time)
                rightClick(Pattern("{}_R.png".format(action_image, action)).exact())
                if action_image.startswith('C'):
                    type('C')
                else:
                    type('H')
                click('release.png')
                wait(12)
            else:
                print("no signal set found for {}_{}.png".format(action_image, action))
            if exists(Pattern("{}_R.png".format(action_image)).exact()):
                print("cancel action for {} successful".format(action_image))
            else:
                print("cancel action for {} failed".format(action_image))
        except Exception as e:
            print("Failed to set cancel action for {}: {}".format(action_image, e))

    def log_with_timestamp(self, message, log_file):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_file.write("[{}] {}\n".format(timestamp, message))

    def create_and_run_action_for_test_case(self, csv_file_path, signal_name, log_file_path):
        with open(log_file_path, 'a') as log_file:
            self.create_test_case_dict(csv_file_path, signal_name)
            print("Creating actions for test cases")
            try:
                for signal_name in self.test_name.keys():
                    signal_name = signal_name.replace('-', '_')
                    print("Processing signal: {}".format(signal_name))
                    print("{}_R.png".format(signal_name))
                    if exists(Pattern("{}_R.png".format(signal_name))):
                        self.set_rigt_click_action_for_main_image(signal_name)
                        if exists(Pattern("{}_Y.png".format(signal_name))):
                            print(self.test_name, self.test_name[signal_name])
                            for test_signal, value in self.test_name[signal_name].items():
                                print("here++++++", test_signal)
                                test_signal = test_signal.replace('-', '_')
                                self.set_right_click_action_for_test_signal(test_signal)
                                if value.lower() in ['p', 'x']:
                                    if test_signal.startswith('C'):
                                        image_name = self.get_image_name(test_signal, True)
                                    else:
                                        image_name = self.get_image_name(test_signal)
                                    if not exists(Pattern("{}_R.png".format(image_name))):
                                        self.log_with_timestamp(
                                            "Test case failed for test signal as it is not red {}: {} with main signal {}".format(
                                                value.lower(), test_signal, signal_name), log_file)
                                    else:
                                        self.log_with_timestamp(
                                            "Test case passed for test signal: {} with main signal as it is red value {} {}".format(
                                                value.lower(), test_signal, signal_name), log_file)
                                    self.set_cancel_action(test_signal, 'Y', test_signal=True)
                                else:
                                    if test_signal.startswith('C'):
                                        image_name = self.get_image_name(test_signal, True)
                                    else:
                                        image_name = self.get_image_name(test_signal)
                                    if exists(Pattern("{}_Y.png".format(image_name))):
                                        self.log_with_timestamp(
                                            "Test case passed for test signal as {}: {} with main signal as {}".format(
                                                value, test_signal, signal_name), log_file)
                                self.set_cancel_action(test_signal, 'Y', test_signal=True)
                            self.set_cancel_action(signal_name, 'Y')
                        else:
                            print("Unable to set main signal {}".format(signal_name))
                    else:
                        print("Error finding main signal image {}".format(signal_name))
            except Exception as e:
                print("Error occurred while creating actions for test cases: {}".format(e))


if __name__ == "__main__":
    test_runner = RunTest()
    csv_file_path = "D:\\signal\\test-signal\\test_signal\\Generate.sikuli\\signal_sheet1.csv"
    log_file = "D:\\signal\\test-signal\\test_signal\\Generate.sikuli\\log.txt"
    signal_name = "1L1"
    test_runner.create_and_run_action_for_test_case(csv_file_path, signal_name, log_file)
