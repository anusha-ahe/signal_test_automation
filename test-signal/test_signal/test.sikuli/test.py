from sikuli import *

# Define the actions in a dictionary
actions = {
    "S28": {
        "check_pattern": "1727620639651.png",
        "right_click": "S28R.png",
        "type_sequence": ['H', Key.RIGHT, Key.ENTER],
        "fail_pattern": "S28Y.png",
        "fail_actions": ['H', 'C'],
        "success_message": "S28 PASS ROUTE NOT SET"
    },
    "S24": {
        "check_pattern": "S26Y.png",
        "right_click": "S24_R.png",
        "type_sequence": ['H', Key.RIGHT, Key.DOWN, Key.DOWN, Key.DOWN, Key.ENTER],
        "fail_pattern": "S24Y.png",
        "fail_actions": ['H', 'C'],
        "success_message": "S24 PASS ROUTE NOT SET"
    },
    "SH218": {
        "check_pattern": "S26Y.png",
        "right_click": "SH218R.png",
        "type_sequence": ['D', Key.ENTER],
        "fail_pattern": "SH218Y.png",
        "fail_actions": ['D', 'C'],
        "success_message": "SH218 PASS ROUTE NOT SET"
    }
}

# Initial right-click action
rightClick(Pattern("1727620298733.png").similar(0.81))
type('H')
wait(2)
type('1')
wait(2)

# Function to execute actions based on the dictionary
def execute_actions(key):
    if exists(Pattern(actions[key]["check_pattern"]).similar(0.97)):
        rightClick(actions[key]["right_click"])
        for action in actions[key]["type_sequence"]:
            type(action)
        wait(5)
        
        if exists(Pattern(actions[key]["fail_pattern"]).exact()):
            print(actions[key]["success_message"])
            rightClick(actions[key]["fail_pattern"])
            for action in actions[key]["fail_actions"]:
                type(action)
            wait(2)
            rightClick(actions[key]["right_click"])
            for action in ['H', 'E']:
                type(action)
            wait(2)
        else:
            print("fail")
    else:
        print("fail")

# Execute the defined actions
execute_actions("S28")
execute_actions("S24")
execute_actions("SH218")
