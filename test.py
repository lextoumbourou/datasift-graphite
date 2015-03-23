"""Module provides tests for the datasift_graphite."""

from nose.tools import assert_equals
import time

from datasift_graphite import get_dpu_metrics, get_usage_metrics


def test_get_dpu_metrics():
    """Test for the ``get_dpu_metrics`` function."""
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
            ('datasift.dpu.streams.stream-1.targets.interaction.title.count',
             (ts, 1)),
            ('datasift.dpu.streams.stream-1.targets.interaction.title.dpu',
             (ts, 0.1))
        ])
    )


def test_get_usage_metrics():
    """Test for the ``get_usage_metrics`` function."""
    ts = time.time()

    input_client_data = {
        'streams': {
            'stream1': {
                'seconds': 10,
                'licenses': {'gender': 2}}}}

    assert_equals(
        sorted(get_usage_metrics(input_client_data, ts=ts)),
        sorted([
            ('datasift.usage.total_streams', (ts, 1)),
            ('datasift.usage.streams.stream1.seconds', (ts, 10)),
            ('datasift.usage.streams.stream1.licenses.gender', (ts, 2))
        ])
    )
