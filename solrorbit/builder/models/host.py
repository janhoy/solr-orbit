# SPDX-License-Identifier: Apache-2.0
#
# Modifications by Apache Solr contributors; see git log for details.
# Licensed under the Apache License, Version 2.0.
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from dataclasses import dataclass

from solrorbit.builder.models.node import Node


@dataclass
class Host:
    """A representation of a host within a cluster"""

    name: str
    address: str
    metadata: dict
    node: Node
