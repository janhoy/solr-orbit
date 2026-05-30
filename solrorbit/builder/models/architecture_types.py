# SPDX-License-Identifier: Apache-2.0
#
# Modifications by Apache Solr contributors; see git log for details.
# Licensed under the Apache License, Version 2.0.
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from enum import Enum


class ArchitectureTypes(Enum):
    """
    Represents a machine's architecture type

    :param hardware_name: The value returned by the machine when querying the architecture. Obtained via `uname -m` for unix machines
    :param artifact_name: The value used by artifacts to represent the architecture
    """

    def __init__(self, hardware_name, artifact_name):
        self.hardware_name = hardware_name
        self.artifact_name = artifact_name

    ARM = "aarch64", "arm64"
    x86 = "x86_64", "x64"

    @staticmethod
    def get_from_hardware_name(hardware_name):
        for arch_type in ArchitectureTypes:
            if arch_type.hardware_name == hardware_name:
                return arch_type

        raise ValueError
