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


__protobuf__ = proto.module(
    package="google.cloud.gkehub.multiclusteringress_v1", manifest={"FeatureSpec",},
)


class FeatureSpec(proto.Message):
    r"""**Multi-cluster Ingress**: The configuration for the
    MultiClusterIngress feature.

    Attributes:
        config_membership (str):
            Fully-qualified Membership name which hosts the
            MultiClusterIngress CRD. Example:
            ``projects/foo-proj/locations/global/memberships/bar``
    """

    config_membership = proto.Field(proto.STRING, number=1,)


__all__ = tuple(sorted(__protobuf__.manifest))
