# SPDX-License-Identifier: Apache-2.0
#
# Modifications by Apache Solr contributors; see git log for details.
# Licensed under the Apache License, Version 2.0.
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from solrorbit.builder.models.architecture_types import ArchitectureTypes


class ArtifactVariablesProvider:
    def __init__(self, executor):
        self.executor = executor

    def get_artifact_variables(self, host, version=None):
        return {
            "VERSION": version,
            "OSNAME": self._get_os_name(host),
            "ARCH": self._get_arch(host)
        }

    def _get_os_name(self, host):
        os_name = self.executor.execute(host, "uname", output=True)[0]
        return os_name.lower()

    def _get_arch(self, host):
        arch = self.executor.execute(host, "uname -m", output=True)[0]
        return ArchitectureTypes.get_from_hardware_name(arch.lower()).artifact_name
