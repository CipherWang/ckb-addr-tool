# ckb-addr-tool
## usage
usage: cat.py [-h] [-d ADDRESS] [-e PKHASH] [-n {mainnet,testnet}]
              [-f LOCK_SCRIPT] [-s SHORT_DESC] [--example]

optional arguments:
  -h, --help            show this help message and exit
  -d ADDRESS, --decode ADDRESS
                        decode an address to lock script.
  -e PKHASH, --encode PKHASH
                        encode pkhash to standard secp256k1 address.
  -n {mainnet,testnet}, --network {mainnet,testnet}
  -f LOCK_SCRIPT, --full LOCK_SCRIPT
                        input lock_script to encode a full address:
                        code_hash,args,Type|Data.
  -s SHORT_DESC, --short SHORT_DESC
                        input short description of lock_script to encode:
                        code_hash_index,args.
  --example             show usage examples.

## examples
decode address:
        ./cat.py -d ckt1qyqd4gse834etwgy9wfz0llrfxk253w7l7rsvjq0tr
encode standard address:
        ./cat.py -e daa2193c6b95b9042b9227ffe349acaa45deff87 -n testnet
encode full address:
        ./cat.py -f 0x709f3fda12f561cfacf92273c57a98fede188a3f1a59b1f888d113f9cce08649,0xb73961e46d9eb118d3de1d1e8f30b3af7bbf3160,data
encode short address:
        ./cat.py -s 0,daa2193c6b95b9042b9227ffe349acaa45deff87