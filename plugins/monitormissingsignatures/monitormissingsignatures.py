import os

import errbot

from bitcoinrpc import authproxy


_GROUP_FAIRCOIN_CVN_OPERATORS= '-114923528'
_POLL_FREQUENCY = 60  # 1 minute.
_FAIRCOIN_RPC_URL = 'http://{}:{}@127.0.0.1:8332'


class MonitorMissingSignatures(errbot.BotPlugin):

    def activate(self):
        super().activate()
        self['latest_block'] = 0
        self.start_poller(_POLL_FREQUENCY, self._check_latest_block)

    def _check_latest_block(self):
        user = self.build_identifier(_GROUP_FAIRCOIN_CVN_OPERATORS)
        self['latest_block'] = self._get_latest_block()
        return self.send(user, self['latest_block'])

    def _get_latest_block(self):
        rpc_connection = self._get_rpc_connection()
        return rpc_connection.getbestblockhash()

    def _get_rpc_connection(self):
        # XXX it seems that the connection is not kept alive.
        return authproxy.AuthServiceProxy(
            _FAIRCOIN_RPC_URL.format(
                os.environ.get('FAIRCOIN_RPC_USER'),
                os.environ.get('FAIRCOIN_RPC_PASSWORD')))
