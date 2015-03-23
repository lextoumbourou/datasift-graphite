from nose.tools import assert_equals
import time

from ds_graphite import get_dpu_metrics


def test_get_dpu_metrics():
    ts = time.time()
    input_dpu_data = {
        'stream-1': {
            'dpu': 0.6,
            'detail': {
                'in': {
                    'count': 6,
                    'dpu': 0.6,
                    'targets': {
                        'interaction.title': {
                            'count': 1,
                            'dpu': 0.1}}}}}}

    assert_equals(
        sorted(get_dpu_metrics(input_dpu_data, ts=ts)),
        sorted([
            ('datasift.dpu.streams.stream-1.dpu', (ts, 0.6)),
            ('datasift.dpu.streams.stream-1.count', (ts, 6)),
            ('datasift.dpu.streams.stream-1.targets.interaction.title.count', (ts, 1)),
            ('datasift.dpu.streams.stream-1.targets.interaction.title.dpu', (ts, 0.1))
        ])
    )
