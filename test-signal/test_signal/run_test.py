import csv


class RunTest:
    def __init__(self):
        print("Initializing RunTest object")
        self.columns = None
        self.rows = list()
        self.test_name = {}
        self.test_signal = {}

    def create_test_case_dict(self, csv_file_path, signal_name):
        print("Creating test case dict for signal: {} from CSV file: {}".format(signal_name, csv_file_path))
        try:
            with open(csv_file_path, mode='r', newline='') as file:
                self.rows = list(csv.reader(file))
                self.columns = self.rows[0][1:]
                values = self.rows[1]
                self.rows = self.rows[1:]
                if signal_name not in self.test_signal:
                    self.test_signal[signal_name] = list()
                for col_name, value in zip(self.columns, values):
                    if signal_name not in self.test_name:
                        self.test_name[signal_name] = {}
                    self.test_name[signal_name][col_name] = value
                print("Test case dict created for {}: {}".format(signal_name, self.test_name[signal_name]))
        except Exception as e:
            print("Error occurred while reading the CSV: {}".format(e))

    def set_rigt_click_action_for_main_image(self, main_signal, wait_time=1):
        print("Setting right click action for main image: {}".format(main_signal))
        try:
            rightClick(Pattern("{}_R.png".format(main_signal)))
            type('H')
            wait(wait_time)
            type('1')
            wait(wait_time)
            print("Right click action set for main image: {}".format(main_signal))
        except Exception as e:
            print("Failed to set right click action for {}: {}".format(main_signal, e))

    def set_right_click_action_for_test_signal(self, test_signal, wait_time=1):
        print("Setting right click action for test signal: {}".format(test_signal))
        try:
            rightClick("{}.png".format(test_signal))
            type('H')
            type(Key.RIGHT)
            type(Key.ENTER)
            wait(5)
            print("Right click action set for test signal: {}".format(test_signal))
        except Exception as e:
            print("Failed to set right click action for {}: {}".format(test_signal, e))

    def set_cancel_action(self, action_image, action, wait_time=1):
        print("Setting cancel action for {} with action {}".format(action_image, action))
        try:
            if exists(Pattern("{}_{}.png".format(action_image, action)).exact()):
                rightClick(Pattern("{}_{}.png".format(action_image, action)).exact())
                type('D')
                type('C')
                wait(2)
                rightClick(Pattern("{}_R.png".format(action_image)).exact())
                type('D')
                type('E')
                wait(2)
                print("Cancel action set for {} with action {}".format(action_image, action))
        except Exception as e:
            print("Failed to set cancel action for {}: {}".format(action_image, e))

    def create_and_run_action_for_test_case(self):
        print("Creating actions for test cases")
        try:
            for signal_name in self.test_name.keys():
                print("Processing signal: {}".format(signal_name))
                if exists(Pattern("{}_R.png".format(signal_name))):
                    self.set_rigt_click_action_for_main_image(signal_name)
                    main_signal_check = exists(Pattern("{}_Y.png".format(signal_name)))
                    if main_signal_check:
                        for test_signal, value in self.test_signal[signal_name]:
                            self.set_right_click_action_for_test_signal(test_signal)
                            if value.lower() in ['p', 'x']:
                                if not exists(Pattern("{}_R.png".format(test_signal))):
                                    print("Test case failed for test signal: {} with main signal {}".format(test_signal, signal_name))
                                else:
                                    print("Test case passed for test signal: {} with main signal {}".format(test_signal, signal_name))
                                self.set_cancel_action(test_signal, 'R')
                            else:
                                if exists(Pattern("{}_Y.png".format(test_signal))):
                                    print("Test case passed for test signal: {} with main signal {}".format(test_signal, signal_name))
                                self.set_cancel_action(test_signal, 'Y')
        except Exception as e:
            print("Error occurred while creating actions for test cases: {}".format(e))


if __name__ == "__main__":
    test_runner = RunTest()
    csv_file_path = "signal_sheet.csv"
    signal_name = "S26"
    test_runner.create_test_case_dict(csv_file_path, signal_name)
    test_runner.create_and_run_action_for_test_case()
