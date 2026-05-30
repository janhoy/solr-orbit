# SPDX-License-Identifier: Apache-2.0
#
# Modifications by Apache Solr contributors; see git log for details.
# Licensed under the Apache License, Version 2.0.
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from abc import ABC, abstractmethod


class Provisioner(ABC):
    """
    Provisioners are used to create and destroy any infrastructure required to construct a cluster.
    """
    def __init__(self):
        pass

    @abstractmethod
    def provision_infrastructure(self):
        """
        Provisions the necessary infrastructure for creating a cluster

        ;return hosts: A list of Host objects defining the hosts in a cluster
        """
        raise NotImplementedError

    @abstractmethod
    def tear_down_infrastructure(self, cluster):
        """
        Destroys the infrastructure created for a given cluster

        ;param cluster: A Cluster object representing the cluster to be torn down
        ;return None
        """
        raise NotImplementedError
