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

    # client subparser
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
        dest="sort_by",
        help="sort table by selected field",
        required=False
    )

    client_parser.add_argument(
        "-rs",
        "--reverse-sort",
        action="store_true",
        dest="reverse_sort",
        help="enable reverse sort",
        required=False
    )

    # client subparser
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
        dest="sort_by",
        help="sort table by selected field",
        required=False
    )

    routing_parser.add_argument(
        "-rs",
        "--reverse-sort",
        action="store_true",
        dest="reverse_sort",
        help="enable reverse sort",
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

    # sort the table
    table = table.get_string(
        sortby=args.sort_by,
        reversesort=args.reverse_sort
    )
    print(table)


if __name__ == "__main__":
    main()
