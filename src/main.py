from apscheduler.schedulers.blocking import BlockingScheduler
from homie_helpers import MqttSettings

from Gios import Gios
from bootstrap.bootstrap import start_service

config, logger, timezone = start_service()

scheduler = BlockingScheduler(timezone=timezone)

device = Gios(config=config['gios'], mqtt_settings=MqttSettings.from_dict(config['mqtt']))

scheduler.add_job(device.refresh, 'interval', seconds=config['fetch-interval-seconds'])

scheduler.start()
