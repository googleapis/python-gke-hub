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

from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore


__protobuf__ = proto.module(
    package='google.cloud.gkehub.v1alpha2',
    manifest={
        'Membership',
        'MembershipEndpoint',
        'KubernetesResource',
        'ResourceOptions',
        'GkeCluster',
        'KubernetesMetadata',
        'Authority',
        'MembershipState',
        'ListMembershipsRequest',
        'ListMembershipsResponse',
        'GetMembershipRequest',
        'CreateMembershipRequest',
        'DeleteMembershipRequest',
        'UpdateMembershipRequest',
        'GenerateConnectManifestRequest',
        'GenerateConnectManifestResponse',
        'ConnectAgentResource',
        'ResourceManifest',
        'TypeMeta',
        'InitializeHubRequest',
        'InitializeHubResponse',
        'OperationMetadata',
    },
)


class Membership(proto.Message):
    r"""Membership contains information about a member cluster.
    Attributes:
        name (str):
            Output only. The full, unique name of this Membership
            resource in the format
            ``projects/*/locations/*/memberships/{membership_id}``, set
            during creation.

            ``membership_id`` must be a valid RFC 1123 compliant DNS
            label:

            1. At most 63 characters in length
            2. It must consist of lower case alphanumeric characters or
               ``-``
            3. It must start and end with an alphanumeric character

            Which can be expressed as the regex:
            ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``, with a maximum length of
            63 characters.
        labels (Sequence[google.cloud.gkehub_v1alpha2.types.Membership.LabelsEntry]):
            Optional. GCP labels for this membership.
        description (str):
            Output only. Description of this membership, limited to 63
            characters. Must match the regex:
            ``[a-zA-Z0-9][a-zA-Z0-9_\-\.\ ]*``

            This field is present for legacy purposes.
        endpoint (google.cloud.gkehub_v1alpha2.types.MembershipEndpoint):
            Optional. Endpoint information to reach this
            member.
        state (google.cloud.gkehub_v1alpha2.types.MembershipState):
            Output only. State of the Membership
            resource.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Membership was created.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Membership was last
            updated.
        delete_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. When the Membership was deleted.
        external_id (str):
            Optional. An externally-generated and managed ID for this
            Membership. This ID may be modified after creation, but this
            is not recommended. For GKE clusters, external_id is managed
            by the Hub API and updates will be ignored.

            The ID must match the regex:
            ``[a-zA-Z0-9][a-zA-Z0-9_\-\.]*``

            If this Membership represents a Kubernetes cluster, this
            value should be set to the UID of the ``kube-system``
            namespace object.
        authority (google.cloud.gkehub_v1alpha2.types.Authority):
            Optional. How to identify workloads from this
            Membership. See the documentation on Workload
            Identity for more details:
            https://cloud.google.com/kubernetes-
            engine/docs/how-to/workload-identity
        last_connection_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. For clusters using Connect, the
            timestamp of the most recent connection
            established with Google Cloud. This time is
            updated every several minutes, not continuously.
            For clusters that do not use GKE Connect, or
            that have never connected successfully, this
            field will be unset.
        unique_id (str):
            Output only. Google-generated UUID for this resource. This
            is unique across all Membership resources. If a Membership
            resource is deleted and another resource with the same name
            is created, it gets a different unique_id.
        infrastructure_type (google.cloud.gkehub_v1alpha2.types.Membership.InfrastructureType):
            Optional. The infrastructure type this
            Membership is running on.
    """
    class InfrastructureType(proto.Enum):
        r"""Specifies the infrastructure type of a Membership.
        Infrastructure type is used by Hub to control infrastructure-
        specific behavior, including pricing.
        Each GKE distribution (on-GCP, on-Prem, on-X,...) will set this
        field automatically, but Attached Clusters customers should
        specify a type during registration.
        """
        INFRASTRUCTURE_TYPE_UNSPECIFIED = 0
        ON_PREM = 1
        MULTI_CLOUD = 2

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    labels = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=2,
    )
    description = proto.Field(
        proto.STRING,
        number=3,
    )
    endpoint = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof='type',
        message='MembershipEndpoint',
    )
    state = proto.Field(
        proto.MESSAGE,
        number=5,
        message='MembershipState',
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=7,
        message=timestamp_pb2.Timestamp,
    )
    delete_time = proto.Field(
        proto.MESSAGE,
        number=8,
        message=timestamp_pb2.Timestamp,
    )
    external_id = proto.Field(
        proto.STRING,
        number=9,
    )
    authority = proto.Field(
        proto.MESSAGE,
        number=10,
        message='Authority',
    )
    last_connection_time = proto.Field(
        proto.MESSAGE,
        number=11,
        message=timestamp_pb2.Timestamp,
    )
    unique_id = proto.Field(
        proto.STRING,
        number=12,
    )
    infrastructure_type = proto.Field(
        proto.ENUM,
        number=13,
        enum=InfrastructureType,
    )


class MembershipEndpoint(proto.Message):
    r"""MembershipEndpoint contains information needed to contact a
    Kubernetes API, endpoint and any additional Kubernetes metadata.

    Attributes:
        gke_cluster (google.cloud.gkehub_v1alpha2.types.GkeCluster):
            Optional. GKE-specific information. Only
            present if this Membership is a GKE cluster.
        kubernetes_metadata (google.cloud.gkehub_v1alpha2.types.KubernetesMetadata):
            Output only. Useful Kubernetes-specific
            metadata.
        kubernetes_resource (google.cloud.gkehub_v1alpha2.types.KubernetesResource):
            Optional. The in-cluster Kubernetes Resources that should be
            applied for a correctly registered cluster, in the steady
            state. These resources:

            -  Ensure that the cluster is exclusively registered to one
               and only one Hub Membership.
            -  Propagate Workload Pool Information available in the
               Membership Authority field.
            -  Ensure proper initial configuration of default Hub
               Features.
    """

    gke_cluster = proto.Field(
        proto.MESSAGE,
        number=1,
        message='GkeCluster',
    )
    kubernetes_metadata = proto.Field(
        proto.MESSAGE,
        number=2,
        message='KubernetesMetadata',
    )
    kubernetes_resource = proto.Field(
        proto.MESSAGE,
        number=3,
        message='KubernetesResource',
    )


class KubernetesResource(proto.Message):
    r"""KubernetesResource contains the YAML manifests and
    configuration for Membership Kubernetes resources in the
    cluster. After CreateMembership or UpdateMembership, these
    resources should be re-applied in the cluster.

    Attributes:
        membership_cr_manifest (str):
            Input only. The YAML representation of the
            Membership CR. This field is ignored for GKE
            clusters where Hub can read the CR directly.
            Callers should provide the CR that is currently
            present in the cluster during Create or Update,
            or leave this field empty if none exists. The CR
            manifest is used to validate the cluster has not
            been registered with another Membership.
        membership_resources (Sequence[google.cloud.gkehub_v1alpha2.types.ResourceManifest]):
            Output only. Additional Kubernetes resources
            that need to be applied to the cluster after
            Membership creation, and after every update.
            This field is only populated in the Membership
            returned from a successful long-running
            operation from CreateMembership or
            UpdateMembership. It is not populated during
            normal GetMembership or ListMemberships
            requests. To get the resource manifest after the
            initial registration, the caller should make a
            UpdateMembership call with an empty field mask.
        connect_resources (Sequence[google.cloud.gkehub_v1alpha2.types.ResourceManifest]):
            Output only. The Kubernetes resources for
            installing the GKE Connect agent.
            This field is only populated in the Membership
            returned from a successful long-running
            operation from CreateMembership or
            UpdateMembership. It is not populated during
            normal GetMembership or ListMemberships
            requests. To get the resource manifest after the
            initial registration, the caller should make a
            UpdateMembership call with an empty field mask.
        resource_options (google.cloud.gkehub_v1alpha2.types.ResourceOptions):
            Optional. Options for Kubernetes resource
            generation.
    """

    membership_cr_manifest = proto.Field(
        proto.STRING,
        number=1,
    )
    membership_resources = proto.RepeatedField(
        proto.MESSAGE,
        number=3,
        message='ResourceManifest',
    )
    connect_resources = proto.RepeatedField(
        proto.MESSAGE,
        number=4,
        message='ResourceManifest',
    )
    resource_options = proto.Field(
        proto.MESSAGE,
        number=5,
        message='ResourceOptions',
    )


class ResourceOptions(proto.Message):
    r"""ResourceOptions represent options for Kubernetes resource
    generation.

    Attributes:
        connect_version (str):
            Optional. The Connect agent version to use for
            connect_resources. Defaults to the latest GKE Connect
            version. The version must be a currently supported version,
            obsolete versions will be rejected.
        v1beta1_crd (bool):
            Optional. Use ``apiextensions/v1beta1`` instead of
            ``apiextensions/v1`` for CustomResourceDefinition resources.
            This option should be set for clusters with Kubernetes
            apiserver versions <1.16.
    """

    connect_version = proto.Field(
        proto.STRING,
        number=1,
    )
    v1beta1_crd = proto.Field(
        proto.BOOL,
        number=2,
    )


class GkeCluster(proto.Message):
    r"""GkeCluster contains information specific to GKE clusters.
    Attributes:
        resource_link (str):
            Immutable. Self-link of the GCP resource for
            the GKE cluster. For example:
                //container.googleapis.com/projects/my-
            project/locations/us-west1-a/clusters/my-cluster
            Zonal clusters are also supported.
    """

    resource_link = proto.Field(
        proto.STRING,
        number=1,
    )


class KubernetesMetadata(proto.Message):
    r"""KubernetesMetadata provides informational metadata for
    Memberships that are created from Kubernetes Endpoints
    (currently, these are equivalent to Kubernetes clusters).

    Attributes:
        kubernetes_api_server_version (str):
            Output only. Kubernetes API server version
            string as reported by '/version'.
        node_provider_id (str):
            Output only. Node providerID as reported by the first node
            in the list of nodes on the Kubernetes endpoint. On
            Kubernetes platforms that support zero-node clusters (like
            GKE-on-GCP), the node_count will be zero and the
            node_provider_id will be empty.
        node_count (int):
            Output only. Node count as reported by
            Kubernetes nodes resources.
        vcpu_count (int):
            Output only. vCPU count as reported by
            Kubernetes nodes resources.
        memory_mb (int):
            Output only. The total memory capacity as
            reported by the sum of all Kubernetes nodes
            resources, defined in MB.
        update_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time at which these details were last
            updated. This update_time is different from the
            Membership-level update_time since EndpointDetails are
            updated internally for API consumers.
    """

    kubernetes_api_server_version = proto.Field(
        proto.STRING,
        number=1,
    )
    node_provider_id = proto.Field(
        proto.STRING,
        number=2,
    )
    node_count = proto.Field(
        proto.INT32,
        number=3,
    )
    vcpu_count = proto.Field(
        proto.INT32,
        number=4,
    )
    memory_mb = proto.Field(
        proto.INT32,
        number=5,
    )
    update_time = proto.Field(
        proto.MESSAGE,
        number=100,
        message=timestamp_pb2.Timestamp,
    )


class Authority(proto.Message):
    r"""Authority encodes how Google will recognize identities from
    this Membership. See the workload identity documentation for
    more details: https://cloud.google.com/kubernetes-
    engine/docs/how-to/workload-identity

    Attributes:
        issuer (str):
            Optional. A JSON Web Token (JWT) issuer URI. ``issuer`` must
            start with ``https://`` and be a valid URL with length <2000
            characters.

            If set, then Google will allow valid OIDC tokens from this
            issuer to authenticate within the workload_identity_pool.
            OIDC discovery will be performed on this URI to validate
            tokens from the issuer, unless ``oidc_jwks`` is set.

            Clearing ``issuer`` disables Workload Identity. ``issuer``
            cannot be directly modified; it must be cleared (and
            Workload Identity disabled) before using a new issuer (and
            re-enabling Workload Identity).
        oidc_jwks (bytes):
            Optional. OIDC verification keys for this Membership in JWKS
            format (RFC 7517).

            When this field is set, OIDC discovery will NOT be performed
            on ``issuer``, and instead OIDC tokens will be validated
            using this field.
        identity_provider (str):
            Output only. An identity provider that reflects the
            ``issuer`` in the workload identity pool.
        workload_identity_pool (str):
            Output only. The name of the workload identity pool in which
            ``issuer`` will be recognized.

            There is a single Workload Identity Pool per Hub that is
            shared between all Memberships that belong to that Hub. For
            a Hub hosted in {PROJECT_ID}, the workload pool format is
            ``{PROJECT_ID}.hub.id.goog``, although this is subject to
            change in newer versions of this API.
    """

    issuer = proto.Field(
        proto.STRING,
        number=1,
    )
    oidc_jwks = proto.Field(
        proto.BYTES,
        number=5,
    )
    identity_provider = proto.Field(
        proto.STRING,
        number=3,
    )
    workload_identity_pool = proto.Field(
        proto.STRING,
        number=4,
    )


class MembershipState(proto.Message):
    r"""MembershipState describes the state of a Membership resource.
    Attributes:
        code (google.cloud.gkehub_v1alpha2.types.MembershipState.Code):
            Output only. The current state of the
            Membership resource.
    """
    class Code(proto.Enum):
        r"""Code describes the state of a Membership resource."""
        CODE_UNSPECIFIED = 0
        CREATING = 1
        READY = 2
        DELETING = 3
        UPDATING = 4
        SERVICE_UPDATING = 5

    code = proto.Field(
        proto.ENUM,
        number=1,
        enum=Code,
    )


class ListMembershipsRequest(proto.Message):
    r"""Request message for ``GkeHub.ListMemberships`` method.
    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Memberships will be listed. Specified in the format
            ``projects/*/locations/*``.
        page_size (int):
            Optional. When requesting a 'page' of resources,
            ``page_size`` specifies number of resources to return. If
            unspecified or set to 0, all resources will be returned.
        page_token (str):
            Optional. Token returned by previous call to
            ``ListMemberships`` which specifies the position in the list
            from where to continue listing the resources.
        filter (str):
            Optional. Lists Memberships that match the filter
            expression, following the syntax outlined in
            https://google.aip.dev/160.

            Examples:

            -  Name is ``bar`` in project ``foo-proj`` and location
               ``global``:

               name =
               "projects/foo-proj/locations/global/membership/bar"

            -  Memberships that have a label called ``foo``:

               labels.foo:\*

            -  Memberships that have a label called ``foo`` whose value
               is ``bar``:

               labels.foo = bar

            -  Memberships in the CREATING state:

               state = CREATING
        order_by (str):
            Optional. One or more fields to compare and
            use to sort the output. See
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


class ListMembershipsResponse(proto.Message):
    r"""Response message for the ``GkeHub.ListMemberships`` method.
    Attributes:
        resources (Sequence[google.cloud.gkehub_v1alpha2.types.Membership]):
            The list of matching Memberships.
        next_page_token (str):
            A token to request the next page of resources from the
            ``ListMemberships`` method. The value of an empty string
            means that there are no more resources to return.
        unreachable (Sequence[str]):
            List of locations that could not be reached
            while fetching this list.
    """

    @property
    def raw_page(self):
        return self

    resources = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='Membership',
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )
    unreachable = proto.RepeatedField(
        proto.STRING,
        number=3,
    )


class GetMembershipRequest(proto.Message):
    r"""Request message for ``GkeHub.GetMembership`` method.
    Attributes:
        name (str):
            Required. The Membership resource name in the format
            ``projects/*/locations/*/memberships/*``.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class CreateMembershipRequest(proto.Message):
    r"""Request message for the ``GkeHub.CreateMembership`` method.
    Attributes:
        parent (str):
            Required. The parent (project and location) where the
            Memberships will be created. Specified in the format
            ``projects/*/locations/*``.
        membership_id (str):
            Required. Client chosen ID for the membership.
            ``membership_id`` must be a valid RFC 1123 compliant DNS
            label:

            1. At most 63 characters in length
            2. It must consist of lower case alphanumeric characters or
               ``-``
            3. It must start and end with an alphanumeric character

            Which can be expressed as the regex:
            ``[a-z0-9]([-a-z0-9]*[a-z0-9])?``, with a maximum length of
            63 characters.
        resource (google.cloud.gkehub_v1alpha2.types.Membership):
            Required. The membership to create.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    membership_id = proto.Field(
        proto.STRING,
        number=2,
    )
    resource = proto.Field(
        proto.MESSAGE,
        number=3,
        message='Membership',
    )


class DeleteMembershipRequest(proto.Message):
    r"""Request message for ``GkeHub.DeleteMembership`` method.
    Attributes:
        name (str):
            Required. The Membership resource name in the format
            ``projects/*/locations/*/memberships/*``.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class UpdateMembershipRequest(proto.Message):
    r"""Request message for ``GkeHub.UpdateMembership`` method.
    Attributes:
        name (str):
            Required. The Membership resource name in the format
            ``projects/*/locations/*/memberships/*``.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. Mask of fields to update.
        resource (google.cloud.gkehub_v1alpha2.types.Membership):
            Required. Only fields specified in update_mask are updated.
            If you specify a field in the update_mask but don't specify
            its value here that field will be deleted. If you are
            updating a map field, set the value of a key to null or
            empty string to delete the key from the map. It's not
            possible to update a key's value to the empty string.
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
        message='Membership',
    )


class GenerateConnectManifestRequest(proto.Message):
    r"""Request message for ``GkeHub.GenerateConnectManifest`` method. .
    Attributes:
        name (str):
            Required. The Membership resource name the Agent will
            associate with, in the format
            ``projects/*/locations/*/memberships/*``.
        namespace (str):
            Optional. Namespace for GKE Connect agent resources.
            Defaults to ``gke-connect``.

            The Connect Agent is authorized automatically when run in
            the default namespace. Otherwise, explicit authorization
            must be granted with an additional IAM binding.
        proxy (bytes):
            Optional. URI of a proxy if connectivity from the agent to
            gkeconnect.googleapis.com requires the use of a proxy.
            Format must be in the form ``http(s)://{proxy_address}``,
            depending on the HTTP/HTTPS protocol supported by the proxy.
            This will direct the connect agent's outbound traffic
            through a HTTP(S) proxy.
        version (str):
            Optional. The Connect agent version to use.
            Defaults to the most current version.
        is_upgrade (bool):
            Optional. If true, generate the resources for
            upgrade only. Some resources generated only for
            installation (e.g. secrets) will be excluded.
        registry (str):
            Optional. The registry to fetch the connect
            agent image from. Defaults to gcr.io/gkeconnect.
        image_pull_secret_content (bytes):
            Optional. The image pull secret content for
            the registry, if not public.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    namespace = proto.Field(
        proto.STRING,
        number=2,
    )
    proxy = proto.Field(
        proto.BYTES,
        number=3,
    )
    version = proto.Field(
        proto.STRING,
        number=4,
    )
    is_upgrade = proto.Field(
        proto.BOOL,
        number=5,
    )
    registry = proto.Field(
        proto.STRING,
        number=6,
    )
    image_pull_secret_content = proto.Field(
        proto.BYTES,
        number=7,
    )


class GenerateConnectManifestResponse(proto.Message):
    r"""GenerateConnectManifestResponse contains manifest information
    for installing/upgrading a Connect agent.

    Attributes:
        manifest (Sequence[google.cloud.gkehub_v1alpha2.types.ConnectAgentResource]):
            The ordered list of Kubernetes resources that
            need to be applied to the cluster for GKE
            Connect agent installation/upgrade.
    """

    manifest = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message='ConnectAgentResource',
    )


class ConnectAgentResource(proto.Message):
    r"""ConnectAgentResource represents a Kubernetes resource
    manifest for Connect Agent deployment.

    Attributes:
        type_ (google.cloud.gkehub_v1alpha2.types.TypeMeta):
            Kubernetes type of the resource.
        manifest (str):
            YAML manifest of the resource.
    """

    type_ = proto.Field(
        proto.MESSAGE,
        number=1,
        message='TypeMeta',
    )
    manifest = proto.Field(
        proto.STRING,
        number=2,
    )


class ResourceManifest(proto.Message):
    r"""ResourceManifest represents a single Kubernetes resource to
    be applied to the cluster.

    Attributes:
        manifest (str):
            YAML manifest of the resource.
        cluster_scoped (bool):
            Whether the resource provided in the manifest is
            ``cluster_scoped``. If unset, the manifest is assumed to be
            namespace scoped.

            This field is used for REST mapping when applying the
            resource in a cluster.
    """

    manifest = proto.Field(
        proto.STRING,
        number=1,
    )
    cluster_scoped = proto.Field(
        proto.BOOL,
        number=2,
    )


class TypeMeta(proto.Message):
    r"""TypeMeta is the type information needed for content
    unmarshalling of Kubernetes resources in the manifest.

    Attributes:
        kind (str):
            Kind of the resource (e.g. Deployment).
        api_version (str):
            APIVersion of the resource (e.g. v1).
    """

    kind = proto.Field(
        proto.STRING,
        number=1,
    )
    api_version = proto.Field(
        proto.STRING,
        number=2,
    )


class InitializeHubRequest(proto.Message):
    r"""Request message for the InitializeHub method.
    Attributes:
        project (str):
            Required. The Hub to initialize, in the format
            ``projects/*/locations/*/memberships/*``.
    """

    project = proto.Field(
        proto.STRING,
        number=1,
    )


class InitializeHubResponse(proto.Message):
    r"""Response message for the InitializeHub method.
    Attributes:
        service_identity (str):
            Name of the Hub default service identity, in the format:

            ::

                service-<project-number>@gcp-sa-gkehub.iam.gserviceaccount.com

            The service account has ``roles/gkehub.serviceAgent`` in the
            Hub project.
        workload_identity_pool (str):
            The Workload Identity Pool used for Workload
            Identity-enabled clusters registered with this Hub. Format:
            ``<project-id>.hub.id.goog``
    """

    service_identity = proto.Field(
        proto.STRING,
        number=1,
    )
    workload_identity_pool = proto.Field(
        proto.STRING,
        number=2,
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
