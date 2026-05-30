# SPDX-License-Identifier: Apache-2.0
#
# Modifications by Apache Solr contributors; see git log for details.
# Licensed under the Apache License, Version 2.0.
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from solrorbit.builder.launchers.launcher import Launcher


class NoOpLauncher(Launcher):
    def start(self, host, node_configurations):
        pass

    def stop(self, host, nodes):
        pass
