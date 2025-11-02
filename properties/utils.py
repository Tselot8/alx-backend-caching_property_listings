from django.core.cache import cache
from .models import Property
import logging
from django_redis import get_redis_connection

def get_all_properties():
    properties = cache.get('all_properties')
    if not properties:
        properties = Property.objects.all()
        cache.set('all_properties', properties, 3600)
    return properties

logger = logging.getLogger(__name__)

def get_redis_cache_metrics():
    # Connect to Redis
    redis_conn = get_redis_connection("default")

    # Fetch INFO statistics
    info = redis_conn.info()

    # Extract keyspace metrics
    hits = info.get("keyspace_hits", 0)
    misses = info.get("keyspace_misses", 0)

    # Calculate hit ratio safely
    total = hits + misses
    hit_ratio = (hits / total) if total > 0 else 0

    # Log metrics
    logger.info(f"Redis Cache Metrics - Hits: {hits}, Misses: {misses}, Hit Ratio: {hit_ratio:.2f}")

    # Return metrics as dictionary
    return {
        "keyspace_hits": hits,
        "keyspace_misses": misses,
        "hit_ratio": hit_ratio,
    }
