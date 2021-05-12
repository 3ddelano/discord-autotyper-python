
# discord-autotyper-python
A python script to auto send commands in Discord or any other program.

>DISCLAIMER
**Use at your own risk!** I am not responsible if you get banned for spamming or using autotype. I do not take responsibility for how you use this program nor do I recommend you use it in any way that may infringe on any software / buisness.

# Installation
Download the repo as a zip and extract it to a folder. Open a command prompt in that folder and and then run the command `pip install -r requirements.txt`  (needs Python3 and pip).

# Usage
- Rename the file `settings-example.json` to `settings.json`.
- Edit the `settings.json` as per your need (read settings.json section below)
- Finally run `python autotyper.py`



## settings.json
This is the configuration file used by the program.

| Key         | Type    | Value   |
| ----------- | ------- | ------- |
| hotkey      | string  | The `KeyCode` of the key to start and pause the autotyping. eg. `Key.f5` or `Key.f6` |
| exitkey | string  | The `KeyCode` of the key used to exit the program. eg. `Key.f5` or `Key.f6` |
| showKeyCode | boolean | Used as a helper to show the `KeyCode` of the pressed key |
| randomSkip | float | A value from 0 to 1 indicating whether to skip a command randomly to prevent ban and blacklisting |
| commands    | array   | An array of `command object` |

###### `command object`
Each command is a object with three keys
| Key | Type | Value  |
| ---------- | ------- | ------- |
| text       | string  | The command you want to send |
| waittime   | integer | The time in seconds to wait before sending the command |
| randomtime | boolean | If enabled, a random delay will be added to the `waittime` so as to reduce the chance of getting banned or blacklisted |



## Examples
##### Single command
You want to send the command `pls beg` after every 45s with a random delay. You want a command to be skipped 10% of the time. The start/pause key is F5 and the exit key is F6. Then the following is the `setttings.json` file:
```json
{
    "hotkey": "Key.f5",
    "exitkey": "Key.f6",
    "showKeyCode": false,
    "randomSkip": 0.1,
    "commands": [
        {
            "text": "pls beg",
            "waittime": 45,
            "randomtime": true
        }
    ]
}
```
##### Multiple commands
You want to send the command `pls beg` after every 45s with a random delay, `pls fish` after 40s with no random delay and `pls hunt` after 40s with a random delay. You don't want a command to be skipped randomly. The start/pause key is F9 and the exit key is F10. Then the following is the `setttings.json` file:
```json
{
    "hotkey": "Key.f9",
    "exitkey": "Key.f10",
    "showKeyCode": false,
    "randomSkip": 0,
    "commands": [
        {
            "text": "pls beg",
            "waittime": 45,
            "randomtime": true
        },
        {
            "text": "pls fish",
            "waittime": 40,
            "randomtime": false
        },
        {
            "text": "pls hunt",
            "waittime": 40,
            "randomtime": true
        }
    ]
}
```
## Legal Warning
This application is not endorsed or affiliated with Discord or any bot for Discord. Usage of this application may also cause a violation of the agreed Terms of Service between you and Discord or a bot.

## Bugs / Suggestions
Report any bugs / glitch, or make a suggestion using the github issues section.