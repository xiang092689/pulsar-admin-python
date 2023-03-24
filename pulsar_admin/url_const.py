class UrlConst:
    BASE_URL_V2 = "/admin/v2"
    CLUSTERS = BASE_URL_V2 + "/clusters"
    BROKERS = BASE_URL_V2 + "/brokers"
    TENANTS = BASE_URL_V2 + "/tenants"
    NAMESPACES = BASE_URL_V2 + "/namespaces"
    PERSISTENT = BASE_URL_V2 + "/persistent"
    BACKLOG_QUOTA_MAP = "/backlogQuotaMap"
    BACKLOG_QUOTA = "/backlogQuota"
    BACKLOG = "/backlog"
    BACKLOG_SIZE = "/backlogSize"
    RETENTION = "/retention"
    CLEAR_BACKLOG = "/clearBacklog"
    MESSAGE_TTL = "/messageTTL"
    COMPACTION_THRESHOLD = "/compactionThreshold"
    PARTITIONS = "/partitions"
    PARTITIONED = "/partitioned"
    CREATE_MISSED_PARTITIONS = "/createMissedPartitions"
    LAST_MESSAGE_ID = "/lastMessageId"
    HEALTHCHECK = BROKERS + "/health"
