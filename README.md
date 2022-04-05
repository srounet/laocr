# Laocr

**Laocr**, an ocr library made for Lost Ark.

```python
from laocr.jobs import fishing
import time


while True:
    fishing.throw('e')
    while fishing.is_fishing():
        if fishing.is_bite_event_displayed():
            fishing.catch('e')
    time.sleep(3)

```

## Basic fishing example:

[![Laocr fishing](https://i.ibb.co/zJKJqjt/cbgpgc.jpg)](https://streamable.com/e/cbgpgc)

## Notes on laocr development

This is an experimental project, mainly focused on learning openCV through interfacing with Lost Ark MMO Action RPG.

At this early stage of development it has only been tested with 3440x1400 resolution and may not work out of the box
for other types of setup.


## Installing Laocr and Supported Versions

As of this early stage you can still install laocr in develop mode with pip:

```console
$ python -m pip -e .
```

Laocr will **be soon available on PyPI** (not available on pypy until basic features are implemented):

```console
$ python -m pip install laocr
```

laocr supports Python 3.7+ on windows only.
