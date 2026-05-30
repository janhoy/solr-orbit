# SPDX-License-Identifier: Apache-2.0
#
# Modifications by Apache Solr contributors; see git log for details.
# Licensed under the Apache License, Version 2.0.
#
# The OpenSearch Contributors require contributions made to
# this file be licensed under the Apache-2.0 license or a
# compatible open source license.
class PluginDistributionRepositoryProvider:
    def __init__(self, plugin, repository_url_provider):
        self.plugin = plugin
        self.repository_url_provider = repository_url_provider

    def get_download_url(self, host):
        distribution_repository = self.plugin.variables["distribution"]["repository"]

        default_key = f"distribution.{distribution_repository}.remote.repo.url"
        return self.repository_url_provider.render_url_for_key(host, self.plugin.variables, default_key, mandatory=False)
