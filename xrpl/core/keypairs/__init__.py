"""
Low-level functions for creating and using cryptographic keys with the XRP
Ledger.
"""
from hashlib import algorithms_available

from xrpl.core.keypairs.exceptions import XRPLKeypairsException
from xrpl.core.keypairs.main import (
    derive_classic_address,
    derive_keypair,
    generate_seed,
    is_valid_message,
    sign,
)


if "ripemd160" in algorithms_available:
    ripemd160 = lambda x: hashlib.new("ripemd160", x).digest()
else:
    try:
        from Crypto.Hash import RIPEMD
        ripemd160 = lambda x: RIPEMD.new(x).digest()
    except ImportError:
        raise ImportError("""Your OpenSSL implementation does not include the RIPEMD160 """
                          """algorithm, which is required by XRPL, or pycrypto """
                          """needs installing""")

__all__ = [
    "derive_classic_address",
    "derive_keypair",
    "generate_seed",
    "is_valid_message",
    "sign",
    "XRPLKeypairsException",
    "ripemd160",
]
