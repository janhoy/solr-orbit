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

from solrorbit.builder.models.host import Host


@dataclass
class Cluster:
    """A representation of the cluster used in the benchmark"""

    name: str
    hosts: List[Host]
