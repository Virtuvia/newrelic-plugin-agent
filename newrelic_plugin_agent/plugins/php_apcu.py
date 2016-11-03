"""
PHP APCU Support

"""
import logging

from newrelic_plugin_agent.plugins import base

LOGGER = logging.getLogger(__name__)


class APCU(base.JSONStatsPlugin):

    GUID = 'it.madisoft.newrelic_php_apcu_agent'

    def add_datapoints(self, stats):
        """Add all of the data points for a node

        :param dict stats: The stats content from APCU as a string

        """
        # APCU Stats
        apcu_stats = stats.get('apcu_stats', dict())
        self.add_gauge_value('APCu Cache/Slots', 'slots',
                             apcu_stats.get('nslots',
                                            apcu_stats.get('num_slots', 0)))
        self.add_gauge_value('APCu Cache/Entries', 'keys',
                             apcu_stats.get('nentries',
                                            apcu_stats.get('num_entries', 0)))
        self.add_gauge_value('APCu Cache/Size', 'bytes',
                             apcu_stats.get('mem_size', 0))
        self.add_gauge_value('APCu Cache/Expunges', 'keys',
                             apcu_stats.get('nexpunges',
                                            apcu_stats.get('expunges', 0)))

        hits = apcu_stats.get('nhits', apcu_stats.get('num_hits', 0))
        misses = apcu_stats.get('nmisses', apcu_stats.get('num_misses', 0))
        total = hits + misses
        if total > 0:
            effectiveness = float(float(hits) / float(total)) * 100
        else:
            effectiveness = 0
        self.add_gauge_value('APCu Cache/Effectiveness', 'percent',
                             effectiveness)

        self.add_derive_value('APCu Cache/Hits', 'keys', hits)
        self.add_derive_value('APCu Cache/Misses', 'keys', misses)
        self.add_derive_value('APCu Cache/Inserts', 'keys',
                              apcu_stats.get('ninserts',
                                             apcu_stats.get('num_inserts',0)))
