# SPDX-License-Identifier: Apache-2.0
#
# Modifications by Apache Solr contributors; see git log for details.
# Licensed under the Apache License, Version 2.0.
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from dataclasses import dataclass
from typing import List

from solrorbit.telemetry import Telemetry


@dataclass
class Node:
    """A representation of a node within a host"""

    name: str
    port: int
    pid: int
    root_dir: str
    binary_path: str
    log_path: str
    heap_dump_path: str
    data_paths: List[str]
    telemetry: Telemetry
