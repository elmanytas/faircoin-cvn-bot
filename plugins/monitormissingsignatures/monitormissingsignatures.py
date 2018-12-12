from bitcoinrpc import authproxy
from errbot import BotPlugin


class MonitorMissingSignatures(BotPlugin):

    def activate(self):
        super().activate()
        self.rpc_connection = AuthServiceProxy(
            'http://{}:{}@127.0.0.1:8332'.format(
                os.environ.get('FAIRCOIN_RPC_USER'),
                os.environ.get('FAIRCOIN_RPC_PASSWORD'))
        self.start_poller(60, self.check_latest_block)

    def check_latest_block(self):
        user =  self.build_identifier('43624396')
        return self.send(user, self.rpc_connection.getbestblockhash())
