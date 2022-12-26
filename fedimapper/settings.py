import os
from typing import List

from pydantic import BaseSettings

from .utils import queuerunner


class Settings(queuerunner.Settings):
    project_name: str = "fedimapper"
    database_url: str = "sqlite:///./test.db"
    stale_rescan_hours: float = 0.90
    unreachable_rescan_hours: float = 24
    debug: bool = False
    evil_domains: List[str] = ["activitypub-troll.cf", "gab.best"]
    spam_domain_threshold: int = 100
    bootstrap_instances: List = [
        # "Official" instance of the org that manages Mastodon.
        "mastodon.social",
    ]


settings = Settings()

UNREADABLE_STATUSES = ["unreachable", "unknown_service", "no_dns"]
