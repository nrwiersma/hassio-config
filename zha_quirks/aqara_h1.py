"""Xiaomi Aqara EU H1 wall switch devices with neutral."""
import logging

from zigpy.profiles import zha
from zigpy.zcl.clusters.general import (
    Basic,
    DeviceTemperature,
    GreenPowerProxy,
    Groups,
    Identify,
    MultistateInput,
    OnOff,
    Ota,
    Scenes,
    Time,
)

from zhaquirks.const import (
    ARGS,
    ATTR_ID,
    BUTTON,
    BUTTON_1,
    BUTTON_2,
    CLUSTER_ID,
    COMMAND_BUTTON_DOUBLE,
    COMMAND_BUTTON_HOLD,
    COMMAND_BUTTON_SINGLE,
    COMMAND_DOUBLE,
    COMMAND_SINGLE,
    DEVICE_TYPE,
    ENDPOINT_ID,
    ENDPOINTS,
    INPUT_CLUSTERS,
    MODELS_INFO,
    OUTPUT_CLUSTERS,
    PRESS_TYPE,
    PROFILE_ID,
    VALUE,
)
from zhaquirks.xiaomi import LUMI, BasicCluster, OnOffCluster, XiaomiCustomDevice
from zhaquirks.xiaomi.aqara.opple_switch import (
    BOTH_BUTTONS,
    MultistateInputCluster,
    OppleSwitchCluster,
)

_LOGGER = logging.getLogger(__name__)


class AqaraSwitchH1NeutralBase(XiaomiCustomDevice):
    """Aqara H1 switch device."""

    device_automation_triggers = {
        (COMMAND_BUTTON_SINGLE, BUTTON_1): {
            ENDPOINT_ID: 41,
            CLUSTER_ID: 18,
            # COMMAND: COMMAND_ATTRIBUTE_UPDATED,
            ARGS: {ATTR_ID: 0x0055, PRESS_TYPE: COMMAND_SINGLE, VALUE: 1},
        },
        (COMMAND_BUTTON_DOUBLE, BUTTON_1): {
            ENDPOINT_ID: 41,
            CLUSTER_ID: 18,
            # COMMAND: COMMAND_ATTRIBUTE_UPDATED,
            ARGS: {ATTR_ID: 0x0055, PRESS_TYPE: COMMAND_DOUBLE, VALUE: 2},
        },
        (COMMAND_BUTTON_HOLD, BUTTON): {
            ENDPOINT_ID: 1,
            CLUSTER_ID: 0xFCC0,
            # COMMAND: COMMAND_ATTRIBUTE_UPDATED,
            ARGS: {ATTR_ID: 0x00FC, VALUE: False},
        },
        (COMMAND_BUTTON_SINGLE, BUTTON_2): {
            ENDPOINT_ID: 42,
            CLUSTER_ID: 18,
            # COMMAND: COMMAND_ATTRIBUTE_UPDATED,
            ARGS: {ATTR_ID: 0x0055, PRESS_TYPE: COMMAND_SINGLE, VALUE: 1},
        },
        (COMMAND_BUTTON_DOUBLE, BUTTON_2): {
            ENDPOINT_ID: 42,
            CLUSTER_ID: 18,
            # COMMAND: COMMAND_ATTRIBUTE_UPDATED,
            ARGS: {ATTR_ID: 0x0055, PRESS_TYPE: COMMAND_DOUBLE, VALUE: 2},
        },
        #        (COMMAND_BUTTON_HOLD, BUTTON_2): {
        #            ENDPOINT_ID: 1,
        #            CLUSTER_ID: 0xFCC0,
        #            # COMMAND: COMMAND_ATTRIBUTE_UPDATED,
        #            ARGS: {ATTR_ID: 0x00FC, VALUE: False},
        #        },
        (COMMAND_BUTTON_SINGLE, BOTH_BUTTONS): {
            ENDPOINT_ID: 51,
            CLUSTER_ID: 18,
            # COMMAND: COMMAND_ATTRIBUTE_UPDATED,
            ARGS: {ATTR_ID: 0x0055, PRESS_TYPE: COMMAND_SINGLE, VALUE: 1},
        },
        (COMMAND_BUTTON_DOUBLE, BOTH_BUTTONS): {
            ENDPOINT_ID: 51,
            CLUSTER_ID: 18,
            # COMMAND: COMMAND_ATTRIBUTE_UPDATED,
            ARGS: {ATTR_ID: 0x0055, PRESS_TYPE: COMMAND_DOUBLE, VALUE: 2},
        },
        (COMMAND_BUTTON_HOLD, BOTH_BUTTONS): {
            ENDPOINT_ID: 1,
            CLUSTER_ID: 0xFCC0,
            # COMMAND: COMMAND_ATTRIBUTE_UPDATED,
            ARGS: {ATTR_ID: 0x00FC, VALUE: 0},
        },
    }


class AqaraSwitchH1Neutral_2G(AqaraSwitchH1NeutralBase):
    """Aqara double key switch device."""

    signature = {
        MODELS_INFO: [
            (LUMI, "lumi.switch.l2aeu1"),
        ],
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[0, 2, 3, 4, 5, 6, 18, 64704]
            # output_clusters=[10, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    DeviceTemperature.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    MultistateInput.cluster_id,
                    OppleSwitchCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[0, 3, 4, 5, 6, 18, 64704]
            # output_clusters=[]>
            2: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    MultistateInput.cluster_id,
                    OppleSwitchCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[18]
            # output_clusters=[]>
            41: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    MultistateInput.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[18]
            # output_clusters=[]>
            42: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    MultistateInput.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[18]
            # output_clusters=[]>
            51: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    MultistateInput.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=1 profile=41440 device_type=97
            # device_version=1
            # input_clusters=[]
            # output_clusters=[33]>
            242: {
                PROFILE_ID: 41440,
                DEVICE_TYPE: 97,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[0, 2, 3, 4, 5, 6, 18, 64704]
            # output_clusters=[10, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    BasicCluster,
                    DeviceTemperature.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOffCluster,
                    MultistateInputCluster,
                    OppleSwitchCluster,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[0, 3, 4, 5, 6, 18, 64704]
            # output_clusters=[]>
            2: {
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    BasicCluster,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOffCluster,
                    MultistateInputCluster,
                    OppleSwitchCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[18]
            # output_clusters=[]>
            41: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    MultistateInputCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[18]
            # output_clusters=[]>
            42: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    MultistateInputCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[18]
            # output_clusters=[]>
            51: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    MultistateInputCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=1 profile=41440 device_type=97
            # device_version=1
            # input_clusters=[]
            # output_clusters=[33]>
            242: {
                PROFILE_ID: 41440,
                DEVICE_TYPE: 97,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }


class AqaraSwitchH1Neutral_1G(AqaraSwitchH1NeutralBase):
    """Aqara double key switch device."""

    signature = {
        MODELS_INFO: [
            (LUMI, "lumi.switch.l1aeu1"),
        ],
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[0, 2, 3, 4, 5, 6, 18, 64704]
            # output_clusters=[10, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    Basic.cluster_id,
                    DeviceTemperature.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOff.cluster_id,
                    MultistateInput.cluster_id,
                    OppleSwitchCluster.cluster_id,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[18]
            # output_clusters=[]>
            41: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    MultistateInput.cluster_id,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=1 profile=41440 device_type=97
            # device_version=1
            # input_clusters=[]
            # output_clusters=[33]>
            242: {
                PROFILE_ID: 41440,
                DEVICE_TYPE: 97,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }

    replacement = {
        ENDPOINTS: {
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[0, 2, 3, 4, 5, 6, 18, 64704]
            # output_clusters=[10, 25]>
            1: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    BasicCluster,
                    DeviceTemperature.cluster_id,
                    Identify.cluster_id,
                    Groups.cluster_id,
                    Scenes.cluster_id,
                    OnOffCluster,
                    MultistateInputCluster,
                    OppleSwitchCluster,
                ],
                OUTPUT_CLUSTERS: [Time.cluster_id, Ota.cluster_id],
            },
            # <SimpleDescriptor endpoint=1 profile=260 device_type=256
            # device_version=1
            # input_clusters=[18]
            # output_clusters=[]>
            41: {
                PROFILE_ID: zha.PROFILE_ID,
                DEVICE_TYPE: zha.DeviceType.ON_OFF_LIGHT,
                INPUT_CLUSTERS: [
                    MultistateInputCluster,
                ],
                OUTPUT_CLUSTERS: [],
            },
            # <SimpleDescriptor endpoint=1 profile=41440 device_type=97
            # device_version=1
            # input_clusters=[]
            # output_clusters=[33]>
            242: {
                PROFILE_ID: 41440,
                DEVICE_TYPE: 97,
                INPUT_CLUSTERS: [],
                OUTPUT_CLUSTERS: [GreenPowerProxy.cluster_id],
            },
        },
    }
