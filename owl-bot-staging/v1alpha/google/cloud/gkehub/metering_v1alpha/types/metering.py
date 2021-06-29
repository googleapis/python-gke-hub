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

from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.gkehub.metering.v1alpha',
    manifest={
        'MembershipState',
    },
)


class MembershipState(proto.Message):
    r"""**Metering**: Per-Membership Feature State.
    Attributes:
        last_measurement_time (google.protobuf.timestamp_pb2.Timestamp):
            The time stamp of the most recent measurement
            of the number of vCPUs in the cluster.
        precise_last_measured_cluster_vcpu_capacity (float):
            The vCPUs capacity in the cluster according
            to the most recent measurement (1/1000
            precision).
    """

    last_measurement_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    precise_last_measured_cluster_vcpu_capacity = proto.Field(
        proto.FLOAT,
        number=3,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
