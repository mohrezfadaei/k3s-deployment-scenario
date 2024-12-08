#!/usr/bin/env python3

import sys
import yaml
import math


def generate_inventory(ipaddrs: list[str]):
    if len(ipaddrs) < 1:
        print("Usage: ./generate_inventory <ip1> <ip2> <ip3> [...]")
        sys.exit(1)

    num_masters = math.ceil(len(ipaddrs) / 3)
    master_ips = ipaddrs[:num_masters]
    worker_ips = ipaddrs[num_masters:]

    nodes = {f"node{i+1}": {"ansible_host": ip} for i, ip in enumerate(ipaddrs)}

    inventory = {
        "all": {
            "children": {
                "nodes": {
                    "hosts": nodes,
                },
                "masters": {"hosts": {f"node{i+1}": {} for i in range(num_masters)}},
                "workers": {
                    "hosts": {
                        f"node{i+1}": {} for i in range(num_masters, len(ipaddrs))
                    }
                },
            }
        }
    }

    with open("inventory/inventory.yml", "w") as file:
        yaml.dump(inventory, file, default_flow_style=False, sort_keys=False)
    print("inventory.yml has been generated.")


if __name__ == "__main__":
    generate_inventory(sys.argv[1:])
