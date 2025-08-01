import pathlib

ROOT = (
    pathlib.Path(__file__).parent.parent.parent
)

SOFTWARE_DATA_FILE = (
    ROOT / "data" / "meta" / "software.yaml"
)

SERVER_DATA = (
    ROOT / "data" / "servers"
)

SERVER_ROOT = (
    ROOT / "data" / "servers"
)
