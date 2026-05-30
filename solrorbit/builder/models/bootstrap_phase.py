# SPDX-License-Identifier: Apache-2.0
#
# Modifications by Apache Solr contributors; see git log for details.
# Licensed under the Apache License, Version 2.0.
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from enum import Enum


class BootstrapPhase(Enum):
    """
    An enum defining the valid phases of bootstrapping. A BootstrapPhase is used to define when a BootstrapHookHandler
    is executed during cluster creation.
    """
    POST_INSTALL = 10

    @classmethod
    def valid(cls, name):
        for n in BootstrapPhase.names():
            if n == name:
                return True
        return False

    @classmethod
    def names(cls):
        return [p.name for p in list(BootstrapPhase)]
