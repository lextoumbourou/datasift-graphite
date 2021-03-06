# Datasift Graphite

[![Build Status](https://travis-ci.org/lextoumbourou/datasift-graphite.svg?branch=master)](https://travis-ci.org/lextoumbourou/datasift-graphite)
[![Latest Version](https://img.shields.io/pypi/v/datasift-graphite.svg)](https://pypi.python.org/pypi/datasift-graphite/)
[![License](https://img.shields.io/pypi/l/datasift-graphite.svg)](https://pypi.python.org/pypi/datasift-graphite/)
[![Downloads](https://img.shields.io/pypi/dm/datasift-graphite.svg)](https://pypi.python.org/pypi/datasift-graphite/)

Graph your Datasift account metrics in Graphite.

## Installation

```
> (sudo) pip install datasift-graphite
```

Chuck it in a [virtualenv](https://virtualenv.pypa.io/en/latest/) if you want.

## Usage

Run ``datasift-graphite --help`` for a full list of options, however, get started like this:

```
> datasift-graphite \
  --user lex \
  --apikey abc123 \
  --graphite-host graphite.company.co \
  --include-dpu-stats
```

To keep it running in the background, I'd recommend something like [Supervisor](http://supervisord.org/). Here's how I do it in Ubuntu 14:

1. ```> sudo apt-get install supervisor```

2. ```> vi /etc/supervisor/conf.d/datasift-graphite.conf```

    ```
    [program:datasift-graphite]
    command=datasift-graphite --user lex --apikey abc123 --graphite-host graphite.company.co --include-dpu-stats
    redirect_stderr=true
    stdout_logfile=/var/log/datasift-graphite.log
    autostart=true
    autorestart=true
    ```
3. ```> sudo service supervisor restart```

You can use whatever you like, though. I won't be offended.

## Examples

* Keep an eye on your Datasift PAYG credits: ```datasift.balance.credit```

* Track your Datasift usage per object: ``sumSeriesWithWildcards(aliasByNode(datasift.usage.streams.*.licenses.*, 5), 1)``

* Track your DPU costs: ``sumSeriesWithWildcards(aliasByNode(datasift.dpu.streams.*.dpu, 4), 1)``

*Note: I'm a bit of a Graphite noob, at the time of writing, so if you've got some better ideas, hit me up.*

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
* ``datasift.dpu.streams.<stream_id>.targets.<target_name>.dpu`` - DPU count per stream, per target.
* ``datasift.dpu.streams.<stream_id>.targets.<target_name>.count`` - DPU count per stream, per target.

*Note: for targets and licenses, ``.`` will be replaced with ``-``, eg ``links.meta.description`` becomes ``links-meta-description``.*
