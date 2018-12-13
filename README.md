# Faircon CVN bot _(faircoin-cvn-bot)_

[![standard-readme compliant](https://img.shields.io/badge/readme%20style-standard-brightgreen.svg?style=flat)](https://github.com/RichardLitt/standard-readme)

[![Snap Status](https://build.snapcraft.io/badge/elopio/faircoin-cvn-bot.svg)](https://build.snapcraft.io/user/elopio/zos-bot)

A monitor bot for the Faircoin Cooperatively Validated Nodes.

Also known as Thomas, the bot.

## Install

In any of the [supported Linux distros](https://snapcraft.io/docs/core/install):

```
sudo snap install faircoin-cvn-bot --edge
```

## Usage

```
FAIRCOIN_RPC_USER=${FAIRCOIN_RPC_USER} FAIRCOIN_RPC_PASSWORD=${FAIRCOIN_RPC_PASSWORD} FAIRCOIN_CVN_BOT_TELEGRAM_TOKEN=${FAIRCOIN_CVN_BOT_TELEGRAM_TOKEN} faircoin-cvn-bot &
```

Where `${FAIRCOIN_RPC_USER}` and `${FAIRCOIN_RPC_PASSWORD}` are the credentials
to connect through RPC to the FairCoin node, and
`${FAIRCOIN_CVN_BOT_TELEGRAM_TOKEN}` is the token for the Telegram bot.

### Actions

Every minute, the bot checks the latest block to and takes note of the CVNs
that didn't sign it.

### Available commands

None, yet.

## Maintainer

[@elopio](https://github.com/elopio/)

## Contribute

If you want to contribute, contact [@elopio](https://gitlab.com/elopio/) or
open an [issue](https://gitlab.com/jaquerespeis/faircoin-cvn-bot/issues).

## License

[GNU General Public License v3.0 or later](LICENSE) (C) 2018 JáquerEspeis
