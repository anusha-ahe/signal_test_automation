import csv
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    handlers=[logging.StreamHandler()])


class RunTest:
    def __init__(self):
        logging.info("Initializing RunTest object")
        self.columns = None
        self.rows = list()
        self.test_name = {}
        self.test_signal = {}

    def create_test_case_dict(self, csv_file_path, signal_name):
        logging.debug(f"Creating test case dict for signal: {signal_name} from CSV file: {csv_file_path}")
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
                logging.info(f"Test case dict created for {signal_name}: {self.test_name[signal_name]}")
        except Exception as e:
            logging.error(f"Error occurred while reading the CSV: {e}")

    def set_rigt_click_action_for_main_image(self, main_signal, wait_time=1):
        logging.debug(f"Setting right click action for main image: {main_signal}")
        try:
            rightClick(Pattern(f"{main_signal}_R.png"))
            type('H')
            wait(wait_time)
            type('1')
            wait(wait_time)
            logging.info(f"Right click action set for main image: {main_signal}")
        except Exception as e:
            logging.error(f"Failed to set right click action for {main_signal}: {e}")

    def set_right_click_action_for_test_signal(self, test_signal, wait_time=1):
        logging.debug(f"Setting right click action for test signal: {test_signal}")
        try:
            rightClick(f"{test_signal}.png")
            type('H')
            type(Key.RIGHT)
            type(Key.ENTER)
            wait(5)
            logging.info(f"Right click action set for test signal: {test_signal}")
        except Exception as e:
            logging.error(f"Failed to set right click action for {test_signal}: {e}")

    def set_cancel_action(self, action_image, action, wait_time=1):
        logging.debug(f"Setting cancel action for {action_image} with action {action}")
        try:
            if exists(Pattern(f"{action_image}_{action}.png").exact()):
                rightClick(Pattern(f"{action_image}_{action}.png").exact())
                type('D')
                type('C')
                wait(2)
                rightClick(Pattern(f"{action_image}_R.png").exact())
                type('D')
                type('E')
                wait(2)
                logging.info(f"Cancel action set for {action_image} with action {action}")
        except Exception as e:
            logging.error(f"Failed to set cancel action for {action_image}: {e}")

    def create_and_run_action_for_test_case(self):
        logging.debug("Creating actions for test cases")
        try:
            for signal_name in self.test_name.keys():
                logging.debug(f"Processing signal: {signal_name}")
                if exists(Pattern(f"{signal_name}_R.png")):
                    self.set_rigt_click_action_for_main_image(signal_name)
                    main_signal_check = exists(Pattern(f"{signal_name}_Y.png"))
                    if main_signal_check:
                        for test_signal, value in self.test_signal[signal_name]:
                            self.set_right_click_action_for_test_signal(test_signal)
                            if value.lower() in ['p', 'x']:
                                if not exists(Pattern(f"{test_signal}_R.png")):
                                    logging.error(f"Test case failed for test signal: {test_signal} with main signal {signal_name}")
                                else:
                                    logging.info((f"Test case passed for test signal: {test_signal} with main signal {signal_name}"))
                                self.set_cancel_action(test_signal, 'R')
                            else:
                                if exists(Pattern(f"{test_signal}_Y.png")):
                                    logging.error(
                                        f"Test case passed for test signal: {test_signal} with main signal {signal_name}")
                                self.set_cancel_action(test_signal, 'Y')
        except Exception as e:
            logging.error(f"Error occurred while creating actions for test cases: {e}")


if __name__ == "__main__":
    test_runner = RunTest()
    csv_file_path = "signal_sheet.csv"
    signal_name = "S26"
    test_runner.create_test_case_dict(csv_file_path, signal_name)
    test_runner.create_and_run_action_for_test_case()

