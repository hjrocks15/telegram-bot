This library provides a pure Python, asynchronous interface for the Telegram Bot API. It's compatible with Python versions 3.8+.

In addition to the pure API implementation, this library features several convenience methods and shortcuts as well as a number of high-level classes to make the development of bots easy and straightforward. These classes are contained in the telegram.ext submodule.

After installing the library, be sure to check out the section on working with PTB.

Telegram API support
All types and methods of the Telegram Bot API 7.8 are natively supported by this library. In addition, Bot API functionality not yet natively included can still be used as described in our wiki.

Notable Features
Fully asynchronous
Convenient shortcut methods, e.g. Message.reply_text
Fully annotated with static type hints
Customizable and extendable interface
Seamless integration with webhooks and polling
Comprehensive documentation and examples
Installing
You can install or upgrade python-telegram-bot via

$ pip install python-telegram-bot --upgrade
To install a pre-release, use the --pre flag in addition.

You can also install python-telegram-bot from source, though this is usually not necessary.

