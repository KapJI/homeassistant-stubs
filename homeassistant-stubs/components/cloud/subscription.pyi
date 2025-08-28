from .client import CloudClient as CloudClient
from .const import REQUEST_TIMEOUT as REQUEST_TIMEOUT
from _typeshed import Incomplete
from hass_nabucasa import Cloud as Cloud, MigratePaypalAgreementInfo as MigratePaypalAgreementInfo, SubscriptionInfo as SubscriptionInfo

_LOGGER: Incomplete

async def async_subscription_info(cloud: Cloud[CloudClient]) -> SubscriptionInfo | None: ...
async def async_migrate_paypal_agreement(cloud: Cloud[CloudClient]) -> MigratePaypalAgreementInfo | None: ...
