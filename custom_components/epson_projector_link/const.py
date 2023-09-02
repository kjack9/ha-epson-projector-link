"""Constants for the epson integration."""
from datetime import timedelta

from .projector.const import PROPERTY_AUTO_IRIS_MODE
from .projector.const import PROPERTY_COLOR_MODE
from .projector.const import PROPERTY_COLOR_SPACE
from .projector.const import PROPERTY_DYNAMIC_RANGE
from .projector.const import PROPERTY_ERR
from .projector.const import PROPERTY_GAMMA_MODE
from .projector.const import PROPERTY_HDR10_PQ_CURVE
from .projector.const import PROPERTY_HLG_CURVE
from .projector.const import PROPERTY_LAMP_HOURS
from .projector.const import PROPERTY_LIGHT_OUTPUT
from .projector.const import PROPERTY_MUTE
from .projector.const import PROPERTY_POWER_CONSUMPTION_MODE
from .projector.const import PROPERTY_SIGNAL_STATUS
from .projector.const import PROPERTY_SOURCE
from .projector.const import PROPERTY_VOLUME

DOMAIN = "epson_projector_link"

CONF_POLL_PROPERTIES = "poll_properties"
CONF_PROPERTIES_SCAN_INTERVAL = "poll_properties_scan_interval"

DEFAULT_POWER_SCAN_INTERVAL = 600
DEFAULT_PROPERTIES_SCAN_INTERVAL = 60
POWER_TIMEOUT_RETRY_INTERVAL = timedelta(seconds=10)

# Update error messages in strings.json and translations/en.json
PROPERTY_TO_ATTRIBUTE_NAME_MAP = {
    PROPERTY_AUTO_IRIS_MODE: "auto_iris_mode",
    PROPERTY_COLOR_MODE: "color_mode",
    PROPERTY_COLOR_SPACE: "color_space",
    PROPERTY_DYNAMIC_RANGE: "dynamic_range",
    PROPERTY_ERR: "error",
    PROPERTY_GAMMA_MODE: "gamma_mode",
    PROPERTY_HDR10_PQ_CURVE: "hdr10_pq_curve",
    PROPERTY_HLG_CURVE: "hlg_curve",
    PROPERTY_LAMP_HOURS: "lamp_hours",
    PROPERTY_LIGHT_OUTPUT: "light_output",
    PROPERTY_MUTE: "is_volume_muted",
    PROPERTY_POWER_CONSUMPTION_MODE: "power_consumption_mode",
    PROPERTY_SIGNAL_STATUS: "signal_status",
    PROPERTY_SOURCE: "source",
    PROPERTY_VOLUME: "volume",
}

SERVICE_LOAD_LENS_MEMORY = "load_lens_memory"
SERVICE_LOAD_PICTURE_MEMORY = "load_picture_memory"
SERVICE_SELECT_AUTO_IRIS_MODE = "select_auto_iris_mode"
SERVICE_SELECT_COLOR_MODE = "select_color_mode"
SERVICE_SELECT_COLOR_SPACE = "select_color_space"
SERVICE_SELECT_DYNAMIC_RANGE = "select_dynamic_range"
SERVICE_SELECT_GAMMA_MODE = "select_gamma_mode"
SERVICE_SELECT_POWER_CONSUMPTION_MODE = "select_power_consumption_mode"
SERVICE_SET_HDR10_PQ_CURVE = "set_hdr10_pq_curve"
SERVICE_SET_HLG_CURVE = "set_hlg_curve"
SERVICE_SET_LIGHT_OUTPUT = "set_light_output"

SERVICE_SEND_COMMAND = "send_command"
