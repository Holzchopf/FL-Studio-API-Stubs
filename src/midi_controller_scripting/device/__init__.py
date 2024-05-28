"""
{{module_title[device]}}

The `device` module is used to handle communication with FL Studio's MIDI
interface. This includes sending messages to the connected device, as well as
to other scripts.

## Contents

* {{docs_url_page("Device", "midi_controller_scripting/device/device")}}:
  communicate with the connected MIDI controller.

* {{docs_url_page("Dispatch", "midi_controller_scripting/device/dispatch")}}:
  communicate with the other MIDI scripts running within FL Studio.

* {{docs_url_page("FL", "midi_controller_scripting/device/fl")}}:
  communicate with low-level FL Studio features such as control ID links.

* {{docs_url_page("Utilities", "midi_controller_scripting/device/util")}}:
  various utility functions for controlling script interaction with the
  connected device.
"""

__all__ = [
    'isAssigned',
    'isMidiOutAssigned',
    'getPortNumber',
    'getName',
    'midiOutMsg',
    'midiOutNewMsg',
    'midiOutSysex',
    'sendMsgGeneric',
    'directFeedback',
    'repeatMidiEvent',
    'stopRepeatMidiEvent',
    'setMasterSync',
    'getMasterSync',
    'processMIDICC',
    'forwardMIDICC',
    'findEventID',
    'getLinkedValue',
    'getLinkedValueString',
    'getLinkedParamName',
    'getLinkedInfo',
    'dispatch',
    'dispatchReceiverCount',
    'dispatchGetReceiverPortNumber',
    'createRefreshThread',
    'destroyRefreshThread',
    'fullRefresh',
    'isDoubleClick',
    'getDeviceID',
    'getLinkedChannel',
    'linkToLastTweaked',
    'getIdleElapsed',
    'setHasMeters',
    'baseTrackSelect',
    'hardwareRefreshMixerTrack',
]

from .__device import (
    isAssigned,
    isMidiOutAssigned,
    getPortNumber,
    getName,
    midiOutMsg,
    midiOutNewMsg,
    midiOutSysex,
    sendMsgGeneric,
    directFeedback,
    repeatMidiEvent,
    stopRepeatMidiEvent,
    setMasterSync,
    getMasterSync,
    getDeviceID,
)
from .__fl import (
    processMIDICC,
    forwardMIDICC,
    findEventID,
    getLinkedValue,
    getLinkedValueString,
    getLinkedParamName,
    getLinkedInfo,
    getLinkedChannel,
    linkToLastTweaked,
    getIdleElapsed,
)
from .__dispatch import (
    dispatch,
    dispatchReceiverCount,
    dispatchGetReceiverPortNumber,
)
from .__util import (
    createRefreshThread,
    destroyRefreshThread,
    fullRefresh,
    isDoubleClick,
    setHasMeters,
    baseTrackSelect,
    hardwareRefreshMixerTrack,
)
