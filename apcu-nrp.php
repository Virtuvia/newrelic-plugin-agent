<?php
/**
 * PHP APCU Data for NewRelic Plugin Agent
 *
 */
Header('Content-Type: application/json');
echo json_encode(array('apcu_stats' => apc_cache_info('user', true) ?: new stdClass) ?: new stdClass);
