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

from google.cloud.gkehub_v1alpha.types import feature
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.gkehub.v1alpha',
    manifest={
        'ListFeaturesRequest',
        'ListFeaturesResponse',
        'GetFeatureRequest',
        'CreateFeatureRequest',
        'DeleteFeatureRequest',
        'UpdateFeatureRequest',
        'OperationMetadata',
    },
)


class ListFeaturesRequest(proto.Message):
    r"""Request message for ``GkeHub.ListFeatures`` method.
    Attributes:
        parent (str):
            The parent (project and location) where the Features will be
            listed. Specified in the format ``projects/*/locations/*``.
        page_size (int):
            When requesting a 'page' of resources, ``page_size``
            specifies number of resources to return. If unspecified or
            set to 0, all resources will be returned.
        page_token (str):
            Token returned by previous call to ``ListFeatures`` which
            specifies the position in the list from where to continue
            listing the resources.
        filter (str):
            Lists Features that match the filter expression, following
            the syntax outlined in https://google.aip.dev/160.

            Examples:

            -  Feature with the name "servicemesh" in project
               "foo-proj":

               name =
               "projects/foo-proj/locations/global/features/servicemesh"

            -  Features that have a label called ``foo``:

               labels.foo:\*

            -  Features that have a label called ``foo`` whose value is
               ``bar``:

               labels.foo = bar
        order_by (str):
            One or more fields to compare and use to sort
            the output. See
            https://google.aip.dev/132#ordering.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )
    filter = proto.Field(
        proto.STRING,
        number=4,
    )
    order_by = proto.Field(
        proto.STRING,
        number=5,
    )


class ListFeaturesResponse(proto.Message):
    r"""Response message for the ``GkeHub.ListFeatures`` method.
    Attributes:
        resources (Sequence[google.cloud.gkehub_v1alpha.types.Feature]):
            The list of matching Features
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListFeatures`` method. The value of an empty string means
            that there are no more resources to return.
    """

    @property
    def raw_page(self):
        return self

    resources = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message=feature.Feature,
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class GetFeatureRequest(proto.Message):
    r"""Request message for ``GkeHub.GetFeature`` method.
    Attributes:
        name (str):
            The Feature resource name in the format
            ``projects/*/locations/*/features/*``
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateFeatureRequest(proto.Message):
    r"""Request message for the ``GkeHub.CreateFeature`` method.
    Attributes:
        parent (str):
            The parent (project and location) where the Feature will be
            created. Specified in the format ``projects/*/locations/*``.
        feature_id (str):
            The ID of the feature to create.
        resource (google.cloud.gkehub_v1alpha.types.Feature):
            The Feature resource to create.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    feature_id = proto.Field(
        proto.STRING,
        number=2,
    )
    resource = proto.Field(
        proto.MESSAGE,
        number=3,
        message=feature.Feature,
    )
    request_id = proto.Field(
        proto.STRING,
        number=4,
    )


class DeleteFeatureRequest(proto.Message):
    r"""Request message for ``GkeHub.DeleteFeature`` method.
    Attributes:
        name (str):
            The Feature resource name in the format
            ``projects/*/locations/*/features/*``.
        force (bool):
            If set to true, the delete will ignore any outstanding
            resources for this Feature (that is,
            ``FeatureState.has_resources`` is set to true). These
            resources will NOT be cleaned up or modified in any way.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    force = proto.Field(
        proto.BOOL,
        number=2,
    )
    request_id = proto.Field(
        proto.STRING,
        number=3,
    )


class UpdateFeatureRequest(proto.Message):
    r"""Request message for ``GkeHub.UpdateFeature`` method.
    Attributes:
        name (str):
            The Feature resource name in the format
            ``projects/*/locations/*/features/*``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Mask of fields to update.
        resource (google.cloud.gkehub_v1alpha.types.Feature):
            Only fields specified in update_mask are updated. If you
            specify a field in the update_mask but don't specify its
            value here that field will be deleted. If you are updating a
            map field, set the value of a key to null or empty string to
            delete the key from the map. It's not possible to update a
            key's value to the empty string. If you specify the
            update_mask to be a special path "*", fully replaces all
            user-modifiable fields to match ``resource``.
        request_id (str):
            Optional. A request ID to identify requests.
            Specify a unique request ID so that if you must
            retry your request, the server will know to
            ignore the request if it has already been
            completed. The server will guarantee that for at
            least 60 minutes after the first request.
            For example, consider a situation where you make
            an initial request and the request times out. If
            you make the request again with the same request
            ID, the server can check if original operation
            with the same request ID was received, and if
            so, will ignore the second request. This
            prevents clients from accidentally creating
            duplicate commitments.
            The request ID must be a valid UUID with the
            exception that zero UUID is not supported
            (00000000-0000-0000-0000-000000000000).
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )
    resource = proto.Field(
        proto.MESSAGE,
        number=3,
        message=feature.Feature,
    )
    request_id = proto.Field(
        proto.STRING,
        number=4,
    )


class OperationMetadata(proto.Message):
    r"""Represents the metadata of the long-running operation.
    Attributes:
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation was
            created.
        end_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time the operation finished
            running.
        target (str):
            Output only. Server-defined resource path for
            the target of the operation.
        verb (str):
            Output only. Name of the verb executed by the
            operation.
        status_detail (str):
            Output only. Human-readable status of the
            operation, if any.
        cancel_requested (bool):
            Output only. Identifies whether the user has requested
            cancellation of the operation. Operations that have
            successfully been cancelled have [Operation.error][] value
            with a [google.rpc.Status.code][google.rpc.Status.code] of
            1, corresponding to ``Code.CANCELLED``.
        api_version (str):
            Output only. API version used to start the
            operation.
    """

    create_time = proto.Field(
        proto.MESSAGE,
        number=1,
        message=timestamp_pb2.Timestamp,
    )
    end_time = proto.Field(
        proto.MESSAGE,
        number=2,
        message=timestamp_pb2.Timestamp,
    )
    target = proto.Field(
        proto.STRING,
        number=3,
    )
    verb = proto.Field(
        proto.STRING,
        number=4,
    )
    status_detail = proto.Field(
        proto.STRING,
        number=5,
    )
    cancel_requested = proto.Field(
        proto.BOOL,
        number=6,
    )
    api_version = proto.Field(
        proto.STRING,
        number=7,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
