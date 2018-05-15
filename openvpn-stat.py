import argparse

from openvpn_status import parse_status
from prettytable import PrettyTable


def parse_args():
    """ Parse and validate the command line
    """
    parser = argparse.ArgumentParser(
        description=(
            "Display OpenVPN connected clients and routing information"
        )
    )

    parser.add_argument(
        "-iL",
        "-input--log",
        # uncomment the "default" option and comment the "dest" option
        # to enable monitoring of a given log file source (more user-firendly)
        # default="openvpn-status.log",
        dest="input_log",
        help="OpenVPN status log file",
        required=True,
        type=argparse.FileType("r")
    )

    subparsers = parser.add_subparsers(
        dest="subcommand"
    )
    subparsers.required = True

    client_parser = subparsers.add_parser("client")

    client_parser.add_argument(
        "-s",
        "--sort",
        choices=[
            "Real Address",
            "Common Name",
            "Bytes Received",
            "Bytes Sent",
            "Connected Since"
        ],
        default="Connected Since",
        dest="sort",
        help="sort table by selected field",
        required=False
    )

    routing_parser = subparsers.add_parser("routing")

    routing_parser.add_argument(
        "-s",
        "--sort",
        choices=[
            "Virtual Address",
            "Common Name",
            "Real Address",
            "Last Ref"
        ],
        default="Last Ref",
        dest="sort",
        help="sort table by selected field",
        required=False
    )

    return parser.parse_args()


def create_client_table(client):
    table = PrettyTable()

    table.field_names = [
        "Real Address",
        "Common Name",
        "Bytes Received",
        "Bytes Sent",
        "Connected Since"
    ]

    # the key is the real address
    # the value is the client
    for value in client.values():
        row = [
            value.real_address,
            value.common_name,
            value.bytes_received,
            value.bytes_sent,
            value.connected_since
        ]
        table.add_row(row)

    return table


def create_routing_table(routing):
    table = PrettyTable()

    table.field_names = [
        "Virtual Address",
        "Common Name",
        "Real Address",
        "Last Ref"
    ]

    # the key is the virtual address
    # the value is the routing
    for value in routing.values():
        row = [
            value.virtual_address,
            value.common_name,
            value.real_address,
            value.last_ref
        ]
        table.add_row(row)

    return table


def main():
    args = parse_args()
    status = parse_status(args.input_log.read())

    if args.subcommand == "client":
        table = create_client_table(status.client_list)
    elif args.subcommand == "routing":
        table = create_routing_table(status.routing_table)

    print("{} last update: {}".format(args.input_log.name, status.updated_at))

    default_sorts = ['Connected Since', 'Last Ref']

    if args.sort in default_sorts:
        table = table.get_string(
            sortby=args.sort,
            reversesort=True
        )
    else:
        table = table.get_string(
            sortby=args.sort,
            reversesort=False
        )

    print(table)


if __name__ == "__main__":
    main()
