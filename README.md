# Datasift Graphite

[![Build Status](https://travis-ci.org/lextoumbourou/datasift-graphite.svg?branch=master)](https://travis-ci.org/lextoumbourou/datasift-graphite)

Graph your Datasift account metrics in Graphite.

## To do

* Installation guide.
* Examples.

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
