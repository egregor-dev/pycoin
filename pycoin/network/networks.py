
import binascii

MAINNET = dict(
    MAGIC_HEADER=binascii.unhexlify('CF0567EA'),
    DNS_BOOTSTRAP=[
        "saffroncoin.com", "saffroncoin.com"
        "182.18.175.110", "182.18.175.110",
    ]
)

TESTNET = dict(
    MAGIC_HEADER=binascii.unhexlify('0B110907'),
    DNS_BOOTSTRAP=[
        "bitcoin.petertodd.org", "testnet-seed.bitcoin.petertodd.org",
        "bluematt.me", "testnet-seed.bluematt.me"
    ]
)
