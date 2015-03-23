import pickle
import struct
import time
import argparse
import socket

from datasift.client import Client


def get_balance_metrics(balance, args, ts=time.time()):
    """Return a list of metrics parsed from the [balance](
        http://dev.datasift.com/docs/api/1/balance) endpoint.
    """
    return [
        ('datasift.balance.credit', (ts, balance['balance']['credit']))
    ]


def get_usage_metrics(client, args, ts=time.time()):
    """Return a list of metrics parsed from the [usage](
        http://dev.datasift.com/docs/api/1/usage) endpoint.
    """
    output = []
    total_streams = len(client['streams'].keys())
    output.append(
        ('datasift.streams.total_streams', (ts, total_streams)))

    pass


def get_dpu_data(client, streams):
    """Return a list of streams and their DPU credits.

    Warning: this may chew through you Rate Limiting credits, if you
    have enough streams.
    """
    output = {}
    for stream in streams:
        output[stream] = client.dpu(stream)

    return output


def get_dpu_metrics(dpu_data, ts=time.time()):
    """Parse a dict of DPU items returned from ``get_dpu_data``
    as a list of metrics.
    """
    output = []

    for name, data in dpu_data.items():
        output.append((
            'datasift.dpu.streams.{}.dpu'.format(name), (ts, data['dpu'])))
        output.append((
            'datasift.dpu.streams.{}.count'.format(name),
            (ts, data['detail']['in']['count'])))

        for stream_name, stream_data in (
            data['detail']['in']['targets'].items()
        ):
            output.append((
                'datasift.dpu.streams.{}.targets.{}.dpu'.format(
                    name, stream_name),
                (ts, stream_data['dpu'])))
            output.append((
                'datasift.dpu.streams.{}.targets.{}.count'.format(
                    name, stream_name),
                (ts, stream_data['count'])))

    return output


def send_to_graphite(metrics, args):
    """Send data to Graphite using the [pickle protocol](
        http://graphite.readthedocs.org/en/1.0/
        feeding-carbon.html#the-pickle-protocol).
    """
    payload = pickle.dumps(metrics)
    header = struct.pack('!L', len(payload))
    sock = socket.socket()
    sock.connect((args.graphite_host, args.graphite_port))
    sock.sendall('{}{}'.format(header, payload))
    return sock.close()


def get_args():
    """Register and retrieve arguments."""
    parser = argparse.ArgumentParser(
        description='Send account-related Datasift metrics to Graphite.')
    parser.add_argument(
        '-u', '--user', help='username for the DataSift platform',
        required=True)
    parser.add_argument(
        '-k', '--apikey', help='API key for the DataSift platform',
        required=True)
    parser.add_argument(
        '-g', '--graphite-host',
        help='Graphite hostname', required=True)
    parser.add_argument(
        '-p', '--graphite-port',
        help='Graphite port', default=2004, type=int)
    parser.add_argument(
        '-d', '--include-dpu-stats',
        help=(
            'Include DPU stats? Warning: with a lot of streams this could '
            'chew through your Rate Limit credits.'), default=False, type=bool)
    return parser.parse_args()


def main():
    """Main loop."""
    args = get_args()
    c = Client(user=args.user, apikey=args.apikey)

    balance_metrics = get_balance_metrics(c.balance(), args)
    send_to_graphite(balance_metrics, args)

    if args.include_dpu_stats:
        client_hourly = c.usage('hourly')
        streams = client_hourly['streams'].keys()
        dpu_data = get_dpu_data(c, streams)
        dpu_metrics = get_dpu_metrics(dpu_data)
        send_to_graphite(dpu_metrics, args)

    usage_metrics = get_usage_metrics(client_hourly, args)
    send_to_graphite(usage_metrics, args)


if __name__ == '__main__':
    main()
