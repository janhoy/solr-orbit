# SPDX-License-Identifier: Apache-2.0
#
# Modifications by Apache Solr contributors; see git log for details.
# Licensed under the Apache License, Version 2.0.
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from solrorbit.builder.executors.shell_executor import ShellExecutor
from solrorbit.exceptions import ExecutorError


class ExceptionHandlingShellExecutor(ShellExecutor):
    def __init__(self, executor):
        self.executor = executor

    def execute(self, host, command, **kwargs):
        try:
            return self.executor.execute(host, command, kwargs)
        except Exception as e:
            raise ExecutorError(f"Command \"{command}\" on host \"{host}\" failed to execute", e)
