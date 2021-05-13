
# discord-autotyper-python
A python script to auto send commands in Discord or any other program.
<br>
<img alt="Python3" src="https://img.shields.io/badge/-Python3-3776AB?style=flat-square&logo=Python&logoColor=white" />
>DISCLAIMER
**Use at your own risk!** I am not responsible if you get banned for spamming or using autotype. I do not take responsibility for how you use this program nor do I recommend you use it in any way that may infringe on any software / buisness.

# Installation
Download the repo as a zip and extract it to a folder. Open a command prompt in that folder and and then run the command `pip install -r requirements.txt`  (needs Python3 and pip).

# Usage
- Rename the file `settings-example.json` to `settings.json`.
- Edit the `settings.json` as per your need (read settings.json section below)
- Open a command prompt in the folder and run `python autotyper.py`
- Now either go to the discord web app or desktop app and click on the textbox
- Finally press the hotkey to start the autotyping



## settings.json
This is the configuration file used by the program.

| Key         | Type    | Value                                                                                             |
| ----------- | ------- | ------------------------------------------------------------------------------------------------- |
| hotkey      | string  | The `KeyCode` of the key to start and stop the autotyping. eg. `Key.f5` or `Key.f6`               |
| exitkey     | string  | The `KeyCode` of the key used to exit the program. eg. `Key.f5` or `Key.f6`                       |
| showKeyCode | boolean | Used as a helper to show the `KeyCode` of the pressed key                                         |
| randomSkip  | float   | A value from 0 to 1 indicating whether to skip a command randomly to prevent ban and blacklisting |
| commands    | array   | An array of `command object`                                                                      |
| onetime     | object  | A JS object containing some settings. See `onetime object` below                                  |

#### command object
Each command is a object with three keys

| Key        | Type    | Value     |
| ---------- | ------- | --------- |
| text       | string  | The command you want to send |
| waittime   | integer | The time in seconds to wait before sending the command                                                                 |
| randomtime | boolean | If enabled, a random delay will be added to the `waittime` so as to reduce the chance of getting banned or blacklisted |

#### onetime object
| Key      | Type    | Value   |
| -------- | ------- | ------- |
| hotkey   | string  | The `KeyCode` of the key to start the onetime commands. eg. `Key.f7` or `Key.f8` |
| delay    | integer | The time in seconds to wait before sending each of the onetime commands          |
| commands | array   | An array of strings each containing the command text to be sent.                 |

## Examples
##### Single command
You want to send the command `pls beg` after every 45s with a random delay. You want a command to be skipped 10% of the time. The start/stop key is F5 and the exit key is F6. Then the following is the `setttings.json` file:
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
    ],
    "onetime": {
        "hotkey": "Key.f8",
        "delay": 3,
        "commands": []
    }
}
```
##### Multiple commands
You want to send the command `pls beg` after every 45s with a random delay, `pls fish` after 40s with no random delay and `pls hunt` after 40s with a random delay. You don't want a command to be skipped randomly. The start/stop key is F9 and the exit key is F10. Then the following is the `setttings.json` file:
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
    ],
    "onetime": {
        "hotkey": "Key.f8",
        "delay": 3,
        "commands": []
    }
}
```
##### Using onetime commands
You want the commands `pls sell fish all` , `pls sell deer all` and `pls sell bread all` to be sent when the `F7` key is pressed. The delay between each command is 4s.
The following will be the `onetime` object:
```json
{
    "key": "Key.f7",
    "delay": 4,
    "commands": [
        "pls sell fish all",
        "pls sell deer all",
        "pls sell bread all"
    ]
}
```
## Legal Warning
This application is not endorsed or affiliated with Discord or any bot for Discord. Usage of this application may also cause a violation of the agreed Terms of Service between you and Discord or a bot.

## Prevent Bans and Blacklisting
- Make a new server with a few channels and invite the bot you want to use the commands on.
- In `settings.json` make sure to set the `randomSkip` and enable `randomtime` for each command
- Pause the autotyper often and change channels

## Bugs / Suggestions
Report any bugs / glitch, or make a suggestion using the github issues section.

## Support
Join the Discord Server: [3ddelano Cafe](https://discord.gg/FZY9TqW)
<br>
<a href="https://www.buymeacoffee.com/3ddelano" target="_blank"><img height="41" width="174" src="https://cdn.buymeacoffee.com/buttons/v2/default-red.png" alt="Buy Me A Coffee" width="150" ></a>
