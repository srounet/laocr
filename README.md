# Laocr

**Laocr** an ocr library made for Lost Ark.

```python
>>> from laocr.jobs import fishing
>>>
>>> fishing.throw('e')
>>> while fishing.is_fishing():
>>>     if fishing.is_bite_event_displayed():
>>>         fishing.catch('e')
```

This is an experimental project, mainly focused on learning openCV through interfacing with Lost Ark MMO Action RPG.

At this early stage of development it has only been tested with 3440x1400 resolution and may not work out of the box
for other types of setup.


## Installing Laocr and Supported Versions

As of this early stage you can still install laocr in develop mode with pip:

```console
$ python -m pip -e .
```

Laocr will **be soon available on PyPI** (as of this early stage it is not available yet on pypy):

```console
$ python -m pip install laocr
```

Laocr supports Python 3.7+ on windows only.
