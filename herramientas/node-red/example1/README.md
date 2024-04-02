# Ejemplo 1

* https://nodered.org/docs/user-guide/nodes



example1.json

```Json
[
    {
        "id": "b5b31cbd9a910d1b",
        "type": "tab",
        "label": "example1",
        "disabled": false,
        "info": "",
        "env": []
    },
    {
        "id": "408cd02b9585379f",
        "type": "debug",
        "z": "b5b31cbd9a910d1b",
        "name": "msg.payload",
        "active": true,
        "tosidebar": true,
        "console": false,
        "tostatus": false,
        "complete": "payload",
        "targetType": "msg",
        "statusVal": "",
        "statusType": "auto",
        "x": 610,
        "y": 280,
        "wires": []
    },
    {
        "id": "96b7b0162ed368ce",
        "type": "inject",
        "z": "b5b31cbd9a910d1b",
        "name": "Hello",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "Hello World!",
        "payloadType": "str",
        "x": 370,
        "y": 200,
        "wires": [
            [
                "408cd02b9585379f"
            ]
        ]
    },
    {
        "id": "7a06a46064df7070",
        "type": "inject",
        "z": "b5b31cbd9a910d1b",
        "name": "measure",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "{\"Temp\":62,\"Level\":5.31,\"Time Stamp\":\"March 28th 2024, 10:30:19 pm\"}",
        "payloadType": "json",
        "x": 360,
        "y": 280,
        "wires": [
            [
                "408cd02b9585379f"
            ]
        ]
    },
    {
        "id": "99756383619b607e",
        "type": "inject",
        "z": "b5b31cbd9a910d1b",
        "name": "",
        "props": [
            {
                "p": "payload"
            },
            {
                "p": "topic",
                "vt": "str"
            }
        ],
        "repeat": "",
        "crontab": "",
        "once": false,
        "onceDelay": 0.1,
        "topic": "",
        "payload": "",
        "payloadType": "date",
        "x": 360,
        "y": 360,
        "wires": [
            [
                "408cd02b9585379f"
            ]
        ]
    }
]
```

## Referencias

1. https://www.digikey.com/en/maker/tutorials/2022/how-to-install-and-get-started-with-node-red