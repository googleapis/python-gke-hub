# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
import proto  # type: ignore

from google.protobuf import struct_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.gkehub.servicemesh.v1alpha',
    manifest={
        'FeatureState',
        'MembershipState',
        'AnalysisMessageBase',
        'AnalysisMessage',
    },
)


class FeatureState(proto.Message):
    r"""**Service Mesh**: State for the whole Hub, as analyzed by the
    Service Mesh Hub Controller.

    Attributes:
        analysis_messages (Sequence[google.cloud.gkehub.servicemesh_v1alpha.types.AnalysisMessage]):
            Output only. Results of running Service Mesh
            analyzers.
    """

    analysis_messages = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='AnalysisMessage',
    )


class MembershipState(proto.Message):
    r"""**Service Mesh**: State for a single Membership, as analyzed by the
    Service Mesh Hub Controller.

    Attributes:
        analysis_messages (Sequence[google.cloud.gkehub.servicemesh_v1alpha.types.AnalysisMessage]):
            Output only. Results of running Service Mesh
            analyzers.
    """

    analysis_messages = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='AnalysisMessage',
    )


class AnalysisMessageBase(proto.Message):
    r"""AnalysisMessageBase describes some common information that is
    needed for all messages.

    Attributes:
        type_ (google.cloud.gkehub.servicemesh_v1alpha.types.AnalysisMessageBase.Type):
            Represents the specific type of a message.
        level (google.cloud.gkehub.servicemesh_v1alpha.types.AnalysisMessageBase.Level):
            Represents how severe a message is.
        documentation_url (str):
            A url pointing to the Service Mesh or Istio
            documentation for this specific error type.
    """
    class Level(proto.Enum):
        r"""The values here are chosen so that more severe messages get
        sorted higher, as well as leaving space in between to add more
        later See istio.analysis.v1alpha1.AnalysisMessageBase.Level
        """
        LEVEL_UNSPECIFIED = 0
        ERROR = 3
        WARNING = 8
        INFO = 12

    class Type(proto.Message):
        r"""A unique identifier for the type of message. Display_name is
        intended to be human-readable, code is intended to be machine
        readable. There should be a one-to-one mapping between display_name
        and code. (i.e. do not re-use display_names or codes between message
        types.) See istio.analysis.v1alpha1.AnalysisMessageBase.Type

        Attributes:
            display_name (str):
                A human-readable name for the message type. e.g.
                "InternalError", "PodMissingProxy". This should be the same
                for all messages of the same type. (This corresponds to the
                ``name`` field in open-source Istio.)
            code (str):
                A 7 character code matching ``^IST[0-9]{4}$`` or
                ``^ASM[0-9]{4}$``, intended to uniquely identify the message
                type. (e.g. "IST0001" is mapped to the "InternalError"
                message type.)
        """

        display_name = proto.Field(
            proto.STRING,
            number=1,
        )
        code = proto.Field(
            proto.STRING,
            number=2,
        )

    type_ = proto.Field(
        proto.MESSAGE,
        number=1,
        message=Type,
    )
    level = proto.Field(
        proto.ENUM,
        number=2,
        enum=Level,
    )
    documentation_url = proto.Field(
        proto.STRING,
        number=3,
    )


class AnalysisMessage(proto.Message):
    r"""AnalysisMessage is a single message produced by an analyzer,
    and it used to communicate to the end user about the state of
    their Service Mesh configuration.

    Attributes:
        message_base (google.cloud.gkehub.servicemesh_v1alpha.types.AnalysisMessageBase):
            Details common to all types of Istio and
            ServiceMesh analysis messages.
        description (str):
            A human readable description of what the
            error means. It is suitable for non-
            internationalize display purposes.
        resource_paths (Sequence[str]):
            A list of strings specifying the resource identifiers that
            were the cause of message generation. A "path" here may be:

            -  MEMBERSHIP_ID if the cause is a specific member cluster
            -  MEMBERSHIP_ID/(NAMESPACE/)?RESOURCETYPE/NAME if the cause
               is a resource in a cluster
        args (google.protobuf.struct_pb2.Struct):
            A UI can combine these args with a template (based on
            message_base.type) to produce an internationalized message.
    """

    message_base = proto.Field(
        proto.MESSAGE,
        number=1,
        message='AnalysisMessageBase',
    )
    description = proto.Field(
        proto.STRING,
        number=2,
    )
    resource_paths = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    args = proto.Field(
        proto.MESSAGE,
        number=4,
        message=struct_pb2.Struct,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
