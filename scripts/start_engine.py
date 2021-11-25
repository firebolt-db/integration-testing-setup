from sys import argv

from firebolt.common.settings import Settings
from firebolt.service.manager import ResourceManager

if __name__ == "__main__":
    rm = ResourceManager(Settings())

    if len(argv) < 2:
        raise RuntimeError("db_name argument should be provided")
    database_name = argv[1]
    engine_name = database_name
    database = rm.databases.get_by_name(database_name)
    engine = rm.engines.create(engine_name, scale=1, spec="m5d.4xlarge")
    engine.attach_to_database(database, True)
    engine.start()

    # No start needed, stopped engine should always be stopped
    stopped_engine_name = engine_name + "_stopped"
    stopped_engine = rm.engines.create(stopped_engine_name, scale=1, spec="m5d.4xlarge")
    stopped_engine.attach_to_database(database, True)

    print(engine.name, engine.endpoint, stopped_engine.name, stopped_engine.endpoint)
