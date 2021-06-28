# Copyright (c) Microsoft Corporation.
# Licensed under the MIT license.

"""Model benchmark example for RDMA loopback performance.

Commands to run:
  python3 examples/benchmarks/rdma_loopback_performance_performance.py
"""

from superbench.benchmarks import BenchmarkRegistry
from superbench.common.utils import logger

if __name__ == '__main__':
    parameters = '--ib_index 0 --numa 1'
    context = BenchmarkRegistry.create_benchmark_context('rdma-loopback', parameters=parameters)

    benchmark = BenchmarkRegistry.launch_benchmark(context)
    if benchmark:
        logger.info(
            'benchmark: {}, return code: {}, result: {}'.format(
                benchmark.name, benchmark.return_code, benchmark.result
            )
        )
