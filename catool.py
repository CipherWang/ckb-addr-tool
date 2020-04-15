#!/usr/bin/python3
'''
    ckb address convert tool
    cipher@nervos.org
'''
import sys
sys.path.append('./ckb-address-demo/')
import argparse
from ckb_addr_test import decodeAddress
from ckb_addr_test import generateShortAddress
from ckb_addr_test import generateFullAddress

def _fix_0x(hex):
    return hex[2:] if hex[:2] == "0x" else hex

if __name__ == "__main__":
    # argument parser
    parser = argparse.ArgumentParser()
    group = parser.add_mutually_exclusive_group()
    group.add_argument("-d", "--decode", 
        dest = "address", 
        help = "decode an address to lock script.")
    group.add_argument("-e", "--encode", 
        dest = "pkhash", 
        help = "encode pkhash to standard secp256k1 address.")
    parser.add_argument("-n", "--network", 
        dest = "network", 
        choices=['mainnet','testnet'], 
        default="mainnet")
    group.add_argument("-f", "--full", 
        dest = "lock_script", 
        help="input lock_script to encode a full address: code_hash,args,Type|Data.")
    group.add_argument("-s", "--short", 
        dest = "short_desc", 
        help="input short description of lock_script to encode: code_hash_index,args.")
    parser.add_argument("--example", 
        action="store_true",
        help="show usage examples.")
    args = parser.parse_args()
    # show examples
    if args.example:
        print("decode address:\n\t./catool.py -d ckt1qyqd4gse834etwgy9wfz0llrfxk253w7l7rsvjq0tr")
        print("encode standard address:\n\t./catool.py -e daa2193c6b95b9042b9227ffe349acaa45deff87 -n testnet")
        print("encode full address:\n\t./catool.py -f 0x709f3fda12f561cfacf92273c57a98fede188a3f1a59b1f888d113f9cce08649,0xb73961e46d9eb118d3de1d1e8f30b3af7bbf3160,data")
        print("encode short address:\n\t./catool.py -s 0,daa2193c6b95b9042b9227ffe349acaa45deff87")
        sys.exit(0)
    # decode
    if args.address:
        network = args.address[:4]
        if network != "ckb1" and network != "ckt1":
            print("Address format error!")
            sys.exit(-1)
        network = "mainnet" if network == "ckb1" else "testnet"
        print("network:\t", network)
        script = decodeAddress(args.address, network)
        if script == False:
            print("Address format error!")
            sys.exit(-1)
        if script[0] == "short":
            print("format:\t\t", script[0])
            print("code index:\t", script[1])
            print("args:\t\t", script[2])
        else:
            print("format:\t\t", script[0])
            print("code hash:\t", script[2])
            print("hash type:\t", script[1])
            print("args:\t\t", script[3])
    # encode
    elif args.pkhash:       # standard
        print(generateShortAddress(0x00, _fix_0x(args.pkhash), args.network))
    elif args.lock_script:  # full
        data = args.lock_script.split(",")
        hash_type = data[2].capitalize()
        code_hash = _fix_0x(data[0])
        largs = _fix_0x(data[1])
        print(generateFullAddress(hash_type, code_hash, largs, args.network))
    elif args.short_desc:   # short
        data = args.short_desc.split(",")
        code_index = int(data[0])
        largs = _fix_0x(data[1])
        print(generateShortAddress(code_index, largs, args.network))
    else:
        print("parameters error!")
        print(parser.parse_args(["-h"]))
        sys.exit(-1)