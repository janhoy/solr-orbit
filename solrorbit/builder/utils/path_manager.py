# SPDX-License-Identifier: Apache-2.0
#
# Modifications by Apache Solr contributors; see git log for details.
# Licensed under the Apache License, Version 2.0.
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
from solrorbit.exceptions import ExecutorError
from solrorbit.utils import io


class PathManager:
    def __init__(self, executor):
        self.executor = executor

    def create_path(self, host, path, create_locally=True):
        if create_locally:
            io.ensure_dir(path)
        self.executor.execute(host, "mkdir -m 0777 -p " + path)

    def is_path_present(self, host, path):
        try:
            self.executor.execute(host, f"test -e {path}")
            return True
        except ExecutorError:
            return False

    def delete_path(self, host, path):
        path_block_list = ["", "*", "/", None]
        if path in path_block_list:
            return

        self.executor.execute(host, "rm -r " + path)
