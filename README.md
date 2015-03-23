# Datasift Graphite

A simple script to graph account-related data in Graphite.

## Status

WIP.

## To do

1. Setup logging.
2. Installation guide.
3. Examples.

## Metrics exposed

### balance

* ``datasift.balance.credit`` - The credit remaining on plan.

### usage

* ``datasift.usage.total_streams`` - Total number of streams.
* ``datasift.usage.streams.<stream_id>.seconds`` - Seconds connected.
* ``datasift.usage.streams.<stream_id>.licenses.<license_name>`` - number of objects of each type delivered.

### dpu

* ``datasift.dpu.streams.<stream_id>.dpu`` - DPU value for a stream.
* ``datasift.dpu.streams.<stream_id>.count`` - DPU count for a stream.
* ``datasift.dpu.streams.<stream_id>.price`` - (DPU count * price per DPU) for a stream.

* ``datasift.dpu.streams.<stream_id>.targets.<target_name>.dpu`` - DPU count per stream, per target.
* ``datasift.dpu.streams.<stream_id>.targets.<target_name>.count`` - DPU count per stream, per target.
* ``datasift.dpu.streams.<stream_id>.targets.<target_name>.price`` - DPU count per stream, per target.
