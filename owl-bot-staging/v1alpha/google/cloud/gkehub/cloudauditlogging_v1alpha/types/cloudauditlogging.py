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
    package='google.cloud.gkehub.cloudauditlogging.v1alpha',
    manifest={
        'FeatureSpec',
    },
)


class FeatureSpec(proto.Message):
    r"""**Cloud Audit Logging**: Spec for Audit Logging Allowlisting.
    Attributes:
        allowlisted_service_accounts (Sequence[str]):
            Service account that should be allowlisted to
            send the audit logs; eg cloudauditlogging@gcp-
            project.iam.gserviceaccount.com. These accounts
            must already exist, but do not need to have any
            permissions granted to them. The customer's
            entitlements will be checked prior to
            allowlisting (i.e. the customer must be an
            Anthos customer.)
    """

    allowlisted_service_accounts = proto.RepeatedField(
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
