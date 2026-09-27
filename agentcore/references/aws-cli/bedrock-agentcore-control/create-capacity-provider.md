---
title: aws bedrock-agentcore-control create-capacity-provider
description: \ [aws . bedrock-agentcore-control \]
product: Amazon Bedrock AgentCore
section: References / AWS CLI / bedrock-agentcore-control
source_url: https://docs.aws.amazon.com/cli/latest/reference/bedrock-agentcore-control/create-capacity-provider.html
fetched: '2026-09-26'
tags:
- agentcore
- aws-cli
- bedrock-agentcore-control
- core
- reference
---

\[ [aws](../index.html#cli-aws) . [bedrock-agentcore-control](index.html#cli-aws-bedrock-agentcore-control) \]

# create-capacity-provider

## Description

Creates a capacity provider. A capacity provider defines the Amazon EC2 infrastructure for AgentCore Runtime, including the operating system, allowed instance types, networking, and storage. It also specifies the IAM permissions that AgentCore uses to manage those instances.

The capacity provider name must be unique within your account. After you create the capacity provider, it enters a `CREATING` state and transitions to `READY` when it is available for use.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/bedrock-agentcore-control-2023-06-05/CreateCapacityProvider)

## Synopsis

      create-capacity-provider
    --name <value>
    [--description <value>]
    --permissions-configuration <value>
    [--client-token <value>]
    [--tags <value>]
    --compute-configuration <value>
    [--cli-input-json | --cli-input-yaml]
    [--generate-cli-skeleton <value>]
    [--debug]
    [--endpoint-url <value>]
    [--no-verify-ssl]
    [--no-paginate]
    [--output <value>]
    [--query <value>]
    [--profile <value>]
    [--region <value>]
    [--version <value>]
    [--color <value>]
    [--no-sign-request]
    [--ca-bundle <value>]
    [--cli-read-timeout <value>]
    [--cli-connect-timeout <value>]
    [--cli-binary-format <value>]
    [--no-cli-pager]
    [--cli-auto-prompt]
    [--no-cli-auto-prompt]
    [--cli-error-format <value>]

## Options

`--name` (string) \[required\]

> The name of the capacity provider. The name must be unique within your account.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

`--description` (string)

> An optional description of the capacity provider. If you don’t specify a description, the service creates the capacity provider without one.
>
> Constraints:
>
> - min: `1`
> - max: `4096`

`--permissions-configuration` (structure) \[required\]

> The permissions configuration for the capacity provider. This specifies the IAM role that AgentCore uses to manage the Amazon EC2 instances on your behalf.
>
> capacityProviderOperatorRoleArn -\> (string) \[required\]
>
> > The Amazon Resource Name (ARN) of the IAM role that AgentCore assumes to manage the capacity provider, including launching, tagging, and terminating instances and their network interfaces. We recommend scoping this role to the minimum permissions that your workloads require.
> >
> > Constraints:
> >
> > - min: `1`
> > - max: `2048`
> > - pattern: `arn:aws(-[^:]+)?:iam::([0-9]{12})?:role/.+`

Shorthand Syntax:

    capacityProviderOperatorRoleArn=string

JSON Syntax:

    {
      "capacityProviderOperatorRoleArn": "string"
    }

`--client-token` (string)

> A unique, case-sensitive identifier to ensure that the API request completes no more than one time. If you don’t specify this field, a value is randomly generated for you. If this token matches a previous request, the service ignores the request, but doesn’t return an error. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html) .
>
> Constraints:
>
> - min: `33`
> - max: `256`
> - pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,256}`

`--tags` (map)

> A map of tag keys and values to associate with the capacity provider. If you don’t specify tags, the capacity provider is created with no tags.
>
> Constraints:
>
> - min: `0`
> - max: `50`
>
> key -\> (string)
>
> > Constraints:
> >
> > - min: `1`
> > - max: `128`
> > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
>
> value -\> (string)
>
> > Constraints:
> >
> > - min: `0`
> > - max: `256`
> > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`

Shorthand Syntax:

    KeyName1=string,KeyName2=string

JSON Syntax:

    {"string": "string"
      ...}

`--compute-configuration` (tagged union structure) \[required\]

> The compute configuration for the capacity provider. This defines the Amazon EC2 compute resources used to launch instances: the operating system, allowed instance types, networking, and storage.
>
> ### Note
>
> This is a Tagged Union structure. Only one of the following top level keys can be set: `ec2Configuration`.
>
> ec2Configuration -\> (structure)
>
> > The Amazon EC2 compute configuration for the capacity provider.
> >
> > launchTemplateSource -\> (tagged union structure) \[required\]
> >
> > > The source of the launch template configuration that defines how instances are launched.
> > >
> > > ### Note
> > >
> > > This is a Tagged Union structure. Only one of the following top level keys can be set: `launchParameters`.
> > >
> > > launchParameters -\> (structure)
> > >
> > > > The parameters that AgentCore uses to create the launch template.
> > > >
> > > > operatingSystem -\> (string) \[required\]
> > > >
> > > > > The operating system and CPU architecture for the instances.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `LINUX_X86_64`
> > > > > - `LINUX_ARM64`
> > > >
> > > > instanceRequirements -\> (structure) \[required\]
> > > >
> > > > > The requirements that determine which instance types can be launched.
> > > > >
> > > > > allowedInstanceTypes -\> (list) \[required\]
> > > > >
> > > > > > The list of allowed instance types. You can specify up to 30 instance types.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `30`
> > > > > >
> > > > > > (string)
> > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > >
> > > > ephemeralVolumes -\> (list)
> > > >
> > > > > The block device mappings for instance store (ephemeral) volumes. You can specify up to five mappings.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `5`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > A block device mapping for an instance store (ephemeral) volume.
> > > > > >
> > > > > > deviceName -\> (string)
> > > > > >
> > > > > > > The device name, for example `/dev/sdh` or `xvdh` .
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > > > - pattern: `[a-zA-Z0-9/._-]+`
> > > > > >
> > > > > > virtualName -\> (string)
> > > > > >
> > > > > > > The virtual device name (`ephemeralN` ). Instance store volumes are numbered starting from 0. The number of available instance store volumes depends on the instance type. After you connect to the instance, you must mount the volume.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > > > - pattern: `ephemeral[0-9]+`
> > > > > >
> > > > > > ebs -\> (structure)
> > > > > >
> > > > > > > The shared Amazon EBS performance and encryption properties for a volume. These properties are common across the different volume configurations for a capacity provider.
> > > > > > >
> > > > > > > volumeType -\> (string)
> > > > > > >
> > > > > > > > The Amazon EBS volume type. If you do not specify a type, the default is `gp3` .
> > > > > > > >
> > > > > > > > Possible values:
> > > > > > > >
> > > > > > > > - `standard`
> > > > > > > > - `io1`
> > > > > > > > - `io2`
> > > > > > > > - `gp2`
> > > > > > > > - `sc1`
> > > > > > > > - `st1`
> > > > > > > > - `gp3`
> > > > > > >
> > > > > > > iops -\> (integer)
> > > > > > >
> > > > > > > > The number of IOPS to provision. For `gp3` , `io1` , and `io2` volumes, this is the number of IOPS provisioned for the volume. For `gp2` volumes, this sets the baseline IOPS performance. It also controls the rate at which the volume accumulates I/O credits for bursting. Supported values: `gp3` , 3,000–80,000; `io1` , 100–64,000; `io2` , 100–256,000.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `100`
> > > > > > > > - max: `256000`
> > > > > > >
> > > > > > > throughput -\> (integer)
> > > > > > >
> > > > > > > > The throughput to provision, in MiB/s. Valid only for `gp3` volumes. Valid range: 125–2,000 MiB/s.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `125`
> > > > > > > > - max: `2000`
> > > > > > >
> > > > > > > encrypted -\> (boolean)
> > > > > > >
> > > > > > > > Specifies whether to encrypt the volume. Encrypted volumes can be attached only to instances that support Amazon EBS encryption. If you create a volume from a snapshot, you cannot specify an encryption value.
> > > > > > >
> > > > > > > kmsKeyId -\> (string)
> > > > > > >
> > > > > > > > The identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for Amazon EBS encryption.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `20`
> > > > > > > > - max: `2048`
> > > > > > > > - pattern: `arn:aws(-[^:]+)?:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
> > > > > > >
> > > > > > > snapshotId -\> (string)
> > > > > > >
> > > > > > > > The ID of the snapshot.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `13`
> > > > > > > > - max: `64`
> > > > > > > > - pattern: `snap-[a-f0-9]{8,17}`
> > > > > > >
> > > > > > > volumeSize -\> (integer)
> > > > > > >
> > > > > > > > The size of the volume, in GiB. You must specify either a snapshot ID or a volume size. Supported sizes: `gp2` , 1–16,384; `gp3` , 1–65,536; `io1` , 4–16,384; `io2` , 4–65,536.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `1`
> > > > > > > > - max: `65536`
> > > > > > >
> > > > > > > volumeInitializationRate -\> (integer)
> > > > > > >
> > > > > > > > The rate at which the volume is initialized after creation, in MiB/s. Supported only for volumes created from snapshots. Valid range: 100–300 MiB/s.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `100`
> > > > > > > > - max: `300`
> > > > > > >
> > > > > > > ebsCardIndex -\> (integer)
> > > > > > >
> > > > > > > > The index of the Amazon EBS card. Applies to instances with multiple Amazon EBS cards.
> > > > > > > >
> > > > > > > > Constraints:
> > > > > > > >
> > > > > > > > - min: `0`
> > > >
> > > > monitoring -\> (string)
> > > >
> > > > > The monitoring level for the instances.
> > > > >
> > > > > Possible values:
> > > > >
> > > > > - `BASIC`
> > > > > - `DETAILED`
> > > >
> > > > licenseSpecifications -\> (list)
> > > >
> > > > > The license configurations to associate with the instances. You can specify up to five configurations.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `5`
> > > > >
> > > > > (structure)
> > > > >
> > > > > > A license configuration to associate with the instances.
> > > > > >
> > > > > > licenseConfigurationArn -\> (string) \[required\]
> > > > > >
> > > > > > > The Amazon Resource Name (ARN) of the license configuration.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:license-manager:[a-z0-9-]+:[0-9]{12}:license-configuration:[a-zA-Z0-9_-]+`
> > > >
> > > > capacityReservationSpecification -\> (structure)
> > > >
> > > > > The Capacity Reservation targeting option for the instances.
> > > > >
> > > > > capacityReservationPreference -\> (string)
> > > > >
> > > > > > The Capacity Reservation preference for the instances.
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `capacity-reservations-only`
> > > > > > - `open`
> > > > > > - `none`
> > > > >
> > > > > capacityReservationTarget -\> (structure)
> > > > >
> > > > > > The target Capacity Reservation or Capacity Reservation group for the instances.
> > > > > >
> > > > > > capacityReservationId -\> (string)
> > > > > >
> > > > > > > The ID of the Capacity Reservation in which to run the instances.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `255`
> > > > > > > - pattern: `cr-[0-9a-z]+`
> > > > > >
> > > > > > capacityReservationResourceGroupArn -\> (string)
> > > > > >
> > > > > > > The Amazon Resource Name (ARN) of the Capacity Reservation resource group in which to run the instances.
> > > > > > >
> > > > > > > Constraints:
> > > > > > >
> > > > > > > - min: `1`
> > > > > > > - max: `2048`
> > > > > > > - pattern: `arn:aws(-[^:]+)?:resource-groups:[a-z0-9-]+:[0-9]{12}:group/[a-zA-Z0-9_-]+`
> > > >
> > > > sshKeyName -\> (string)
> > > >
> > > > > The name of the SSH key pair to configure on the instances for SSH connectivity.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `255`
> > > > > - pattern: `[!-~][`` ``-~]*[!-~]$|^[!-~]`
> > > >
> > > > instanceProfileArn -\> (string)
> > > >
> > > > > The Amazon Resource Name (ARN) of the IAM instance profile to associate with launched instances. If provided, this overrides the default instance profile.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `1`
> > > > > - max: `2048`
> > > > > - pattern: `arn:aws(-[^:]+)?:iam::[0-9]{12}:instance-profile/([!-~]{1,510}/)?([\w+=,.@-]{1,128})`
> > > >
> > > > propagatedTags -\> (map)
> > > >
> > > > > The tags to propagate to all Amazon EC2 resources (instances, volumes, and network interfaces) that the capacity provider creates.
> > > > >
> > > > > Constraints:
> > > > >
> > > > > - min: `0`
> > > > > - max: `50`
> > > > >
> > > > > key -\> (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `128`
> > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> > > > >
> > > > > value -\> (string)
> > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `0`
> > > > > > - max: `256`
> > > > > > - pattern: `[a-zA-Z0-9\s._:/=+@-]*`
> >
> > vpcConfiguration -\> (structure) \[required\]
> >
> > > The VPC configuration for launching instances, including subnets and security groups.
> > >
> > > subnets -\> (list) \[required\]
> > >
> > > > The IDs of the subnets in which to launch instances. You must specify at least one subnet.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `16`
> > > >
> > > > (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `subnet-[0-9a-zA-Z]{8,17}`
> > >
> > > securityGroups -\> (list) \[required\]
> > >
> > > > The IDs of the security groups to associate with the instances. You must specify at least one security group.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `1`
> > > > - max: `16`
> > > >
> > > > (string)
> > > >
> > > > > Constraints:
> > > > >
> > > > > - pattern: `sg-[0-9a-zA-Z]{8,17}`
> >
> > volumes -\> (list)
> >
> > > The named persistent Amazon EBS volumes for the capacity provider. A capacity provider can define up to five volumes.
> > >
> > > Constraints:
> > >
> > > - min: `0`
> > > - max: `5`
> > >
> > > (tagged union structure)
> > >
> > > > The configuration for a persistent volume attached to a capacity provider. This structure defines the storage backing for the persistent volumes used by agents that run on capacity provider instances.
> > > >
> > > > ### Note
> > > >
> > > > This is a Tagged Union structure. Only one of the following top level keys can be set: `ebsConfiguration`.
> > > >
> > > > ebsConfiguration -\> (structure)
> > > >
> > > > > The configuration for an Amazon EBS-backed persistent volume.
> > > > >
> > > > > name -\> (string) \[required\]
> > > > >
> > > > > > The logical name of the volume. Use this name to reference the volume when you mount it into an agent runtime.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `48`
> > > > > > - pattern: `[a-zA-Z][a-zA-Z0-9_-]{0,47}`
> > > > >
> > > > > sizeGiB -\> (integer) \[required\]
> > > > >
> > > > > > The size of the volume, in GiB.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `1`
> > > > > > - max: `65536`
> > > > >
> > > > > volumeType -\> (string)
> > > > >
> > > > > > The Amazon EBS volume type. If you do not specify a type, the default is `gp3` .
> > > > > >
> > > > > > Possible values:
> > > > > >
> > > > > > - `standard`
> > > > > > - `io1`
> > > > > > - `io2`
> > > > > > - `gp2`
> > > > > > - `sc1`
> > > > > > - `st1`
> > > > > > - `gp3`
> > > > >
> > > > > iops -\> (integer)
> > > > >
> > > > > > The number of IOPS to provision. Valid only for `gp3` , `io1` , and `io2` volumes.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `100`
> > > > > > - max: `256000`
> > > > >
> > > > > throughput -\> (integer)
> > > > >
> > > > > > The throughput, in MiB/s. Valid only for `gp3` volumes.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `125`
> > > > > > - max: `2000`
> > > > >
> > > > > encrypted -\> (boolean)
> > > > >
> > > > > > Specifies whether to encrypt the volume. If `true` , the service encrypts the volume with the KMS key that you specify in `kmsKeyId` , or the default KMS key for Amazon EBS if you do not specify one. The default is `true` .
> > > > >
> > > > > kmsKeyId -\> (string)
> > > > >
> > > > > > The identifier of the KMS key to use for encryption.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `20`
> > > > > > - max: `2048`
> > > > > > - pattern: `arn:aws(-[^:]+)?:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
> > > > >
> > > > > snapshotId -\> (string)
> > > > >
> > > > > > An optional Amazon EBS snapshot ID. If provided, the volume is initialized from this snapshot the first time it is created. On subsequent restarts, the existing volume is used and the snapshot is ignored.
> > > > > >
> > > > > > Constraints:
> > > > > >
> > > > > > - min: `13`
> > > > > > - max: `64`
> > > > > > - pattern: `snap-[a-f0-9]{8,17}`
> >
> > lifecycleConfiguration -\> (structure)
> >
> > > The lifecycle configuration for instances in the capacity provider.
> > >
> > > idleInstanceTimeout -\> (integer)
> > >
> > > > The number of seconds an instance can remain idle before it is stopped. An instance is considered idle when all of its agents are idle. The default is 900 seconds (15 minutes).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `60`
> > > > - max: `1209600`
> > >
> > > maxLifetime -\> (integer)
> > >
> > > > The maximum lifetime of an instance, in seconds. When an instance reaches this limit, the service terminates it regardless of activity. The default is 28800 seconds (8 hours). The maximum is 1209600 seconds (14 days).
> > > >
> > > > Constraints:
> > > >
> > > > - min: `60`
> > > > - max: `1209600`
> >
> > rootVolume -\> (structure)
> >
> > > The configuration for the instance root volume. Specify the amount of free space to guarantee and, optionally, the Amazon EBS performance and encryption settings. The device name and delete-on-termination behavior are not configurable.
> > >
> > > volumeType -\> (string)
> > >
> > > > The Amazon EBS volume type. If you do not specify a type, the default is `gp3` .
> > > >
> > > > Possible values:
> > > >
> > > > - `standard`
> > > > - `io1`
> > > > - `io2`
> > > > - `gp2`
> > > > - `sc1`
> > > > - `st1`
> > > > - `gp3`
> > >
> > > iops -\> (integer)
> > >
> > > > The number of IOPS to provision. For `gp3` , `io1` , and `io2` volumes, this is the number of IOPS provisioned for the volume. For `gp2` volumes, this sets the baseline IOPS performance. It also controls the rate at which the volume accumulates I/O credits for bursting. Supported values: `gp3` , 3,000–80,000; `io1` , 100–64,000; `io2` , 100–256,000.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `100`
> > > > - max: `256000`
> > >
> > > throughput -\> (integer)
> > >
> > > > The throughput to provision, in MiB/s. Valid only for `gp3` volumes. Valid range: 125–2,000 MiB/s.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `125`
> > > > - max: `2000`
> > >
> > > encrypted -\> (boolean)
> > >
> > > > Specifies whether to encrypt the volume. Encrypted volumes can be attached only to instances that support Amazon EBS encryption. If you create a volume from a snapshot, you cannot specify an encryption value.
> > >
> > > kmsKeyId -\> (string)
> > >
> > > > The identifier (key ID, key alias, key ARN, or alias ARN) of the customer managed KMS key to use for Amazon EBS encryption.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `20`
> > > > - max: `2048`
> > > > - pattern: `arn:aws(-[^:]+)?:kms:[a-z0-9-]+:[0-9]{12}:key/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
> > >
> > > freeSpaceGiB -\> (integer)
> > >
> > > > The free space guaranteed on the root volume, in GiB. AgentCore adds the operating system overhead on top of this value. The default is 8 GiB.
> > > >
> > > > Constraints:
> > > >
> > > > - min: `2`
> > > > - max: `65000`

JSON Syntax:

    {
      "ec2Configuration": {
        "launchTemplateSource": {
          "launchParameters": {
            "operatingSystem": "LINUX_X86_64"|"LINUX_ARM64",
            "instanceRequirements": {
              "allowedInstanceTypes": ["string", ...]
            },
            "ephemeralVolumes": [
              {
                "deviceName": "string",
                "virtualName": "string",
                "ebs": {
                  "volumeType": "standard"|"io1"|"io2"|"gp2"|"sc1"|"st1"|"gp3",
                  "iops": integer,
                  "throughput": integer,
                  "encrypted": true|false,
                  "kmsKeyId": "string",
                  "snapshotId": "string",
                  "volumeSize": integer,
                  "volumeInitializationRate": integer,
                  "ebsCardIndex": integer
                }
              }
              ...
            ],
            "monitoring": "BASIC"|"DETAILED",
            "licenseSpecifications": [
              {
                "licenseConfigurationArn": "string"
              }
              ...
            ],
            "capacityReservationSpecification": {
              "capacityReservationPreference": "capacity-reservations-only"|"open"|"none",
              "capacityReservationTarget": {
                "capacityReservationId": "string",
                "capacityReservationResourceGroupArn": "string"
              }
            },
            "sshKeyName": "string",
            "instanceProfileArn": "string",
            "propagatedTags": {"string": "string"
              ...}
          }
        },
        "vpcConfiguration": {
          "subnets": ["string", ...],
          "securityGroups": ["string", ...]
        },
        "volumes": [
          {
            "ebsConfiguration": {
              "name": "string",
              "sizeGiB": integer,
              "volumeType": "standard"|"io1"|"io2"|"gp2"|"sc1"|"st1"|"gp3",
              "iops": integer,
              "throughput": integer,
              "encrypted": true|false,
              "kmsKeyId": "string",
              "snapshotId": "string"
            }
          }
          ...
        ],
        "lifecycleConfiguration": {
          "idleInstanceTimeout": integer,
          "maxLifetime": integer
        },
        "rootVolume": {
          "volumeType": "standard"|"io1"|"io2"|"gp2"|"sc1"|"st1"|"gp3",
          "iops": integer,
          "throughput": integer,
          "encrypted": true|false,
          "kmsKeyId": "string",
          "freeSpaceGiB": integer
        }
      }
    }

`--cli-input-json` \| `--cli-input-yaml` (string) Reads arguments from the JSON string provided. The JSON string follows the format provided by `--generate-cli-skeleton`. If other arguments are provided on the command line, those values will override the JSON-provided values. It is not possible to pass arbitrary binary values using a JSON-provided value as the string will be taken literally. This may not be specified along with `--cli-input-yaml`.

`--generate-cli-skeleton` (string) Prints a JSON skeleton to standard output without sending an API request. If provided with no value or the value `input`, prints a sample input JSON that can be used as an argument for `--cli-input-json`. Similarly, if provided `yaml-input` it will print a sample input YAML that can be used with `--cli-input-yaml`. If provided with the value `output`, it validates the command inputs and returns a sample output JSON for that command. The generated JSON skeleton is not stable between versions of the AWS CLI and there are no backwards compatibility guarantees in the JSON skeleton generated.

## Global Options

`--debug` (boolean)

Turn on debug logging.

`--endpoint-url` (string)

Override command’s default URL with the given URL.

`--no-verify-ssl` (boolean)

By default, the AWS CLI uses SSL when communicating with AWS services. For each SSL connection, the AWS CLI will verify SSL certificates. This option overrides the default behavior of verifying SSL certificates.

`--no-paginate` (boolean)

Disable automatic pagination. If automatic pagination is disabled, the AWS CLI will only make one call, for the first page of results.

`--output` (string)

The formatting style for command output.

- json
- text
- table
- yaml
- yaml-stream
- off

`--query` (string)

A JMESPath query to use in filtering the response data.

`--profile` (string)

Use a specific profile from your credential file.

`--region` (string)

The region to use. Overrides config/env settings.

`--version` (string)

Display the version of this tool.

`--color` (string)

Turn on/off color output.

- on
- off
- auto

`--no-sign-request` (boolean)

Do not sign requests. Credentials will not be loaded if this argument is provided.

`--ca-bundle` (string)

The CA certificate bundle to use when verifying SSL certificates. Overrides config/env settings.

`--cli-read-timeout` (int)

The maximum socket read time in seconds. If the value is set to 0, the socket read will be blocking and not timeout. The default value is 60 seconds.

`--cli-connect-timeout` (int)

The maximum socket connect time in seconds. If the value is set to 0, the socket connect will be blocking and not timeout. The default value is 60 seconds.

`--cli-binary-format` (string)

The formatting style to be used for binary blobs. The default format is base64. The base64 format expects binary blobs to be provided as a base64 encoded string. The raw-in-base64-out format preserves compatibility with AWS CLI V1 behavior and binary values must be passed literally. When providing contents from a file that map to a binary blob `fileb://` will always be treated as binary and use the file contents directly regardless of the `cli-binary-format` setting. When using `file://` the file contents will need to properly formatted for the configured `cli-binary-format`.

- base64
- raw-in-base64-out

`--no-cli-pager` (boolean)

Disable cli pager for output.

`--cli-auto-prompt` (boolean)

Automatically prompt for CLI input parameters.

`--no-cli-auto-prompt` (boolean)

Disable automatically prompt for CLI input parameters.

`--cli-error-format` (string)

The formatting style for error output. By default, errors are displayed in enhanced format.

- legacy
- json
- yaml
- text
- table
- enhanced

## Output

capacityProviderId -\> (string)

> The unique identifier of the created capacity provider.
>
> Constraints:
>
> - min: `12`
> - max: `59`
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`

capacityProviderArn -\> (string)

> The Amazon Resource Name (ARN) of the capacity provider.
>
> Constraints:
>
> - pattern: `arn:aws(-[^:]+)?:bedrock-agentcore:[a-z0-9-]+:[0-9]{12}:capacity-provider/[a-zA-Z][a-zA-Z0-9_]{0,47}-[a-zA-Z0-9]{10}`

name -\> (string)

> The name of the capacity provider.
>
> Constraints:
>
> - min: `1`
> - max: `48`
> - pattern: `[a-zA-Z][a-zA-Z0-9_]{0,47}`

status -\> (string)

> The current status of the capacity provider. For possible values, see `CapacityProviderStatus` .
>
> Possible values:
>
> - `CREATING`
> - `CREATE_FAILED`
> - `UPDATING`
> - `UPDATE_FAILED`
> - `READY`
> - `DELETING`
> - `DELETE_FAILED`

- [← create-browser-profile](create-browser-profile.html "previous chapter (use the left arrow)") /
- [create-code-interpreter →](create-code-interpreter.html "next chapter (use the right arrow)")

### Navigation

- [index](../../genindex.html "General Index")
- [next](create-code-interpreter.html "create-code-interpreter") \|
- [previous](create-browser-profile.html "create-browser-profile") \|
- [AWS CLI 2.37.4 Command Reference](../../index.html) »
- [aws](../index.html) »
- [bedrock-agentcore-control](index.html) »
- [create-capacity-provider]()

© Copyright 2026, Amazon Web Services. Created using [Sphinx](https://www.sphinx-doc.org/).
