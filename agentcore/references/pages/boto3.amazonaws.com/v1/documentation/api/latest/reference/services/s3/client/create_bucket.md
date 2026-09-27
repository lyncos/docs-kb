---
title: create_bucket[¶](#create-bucket "Link to this heading")
description: S3 / Client / create_bucket
product: Amazon Bedrock AgentCore
section: References / boto3.amazonaws.com
source_url: https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/s3/client/create_bucket.html
fetched: '2026-09-26'
tags:
- agentcore
- boto3-amazonaws-com
- reference
- related
referenced_by:
- runtime-get-started-code-deploy-python.md
conversion: pandoc
---

[S3](../../s3.html) / Client / create_bucket

# create_bucket[¶](#create-bucket "Link to this heading")

S3.Client.create_bucket(*\*\*kwargs*)[¶](#S3.Client.create_bucket "Link to this definition")  
### Note

This action creates an Amazon S3 bucket. To create an Amazon S3 on Outposts bucket, see [CreateBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_CreateBucket.html).

Creates a new S3 bucket. To create a bucket, you must set up Amazon S3 and have a valid Amazon Web Services Access Key ID to authenticate requests. Anonymous requests are never allowed to create buckets. By creating the bucket, you become the bucket owner.

There are two types of buckets: general purpose buckets and directory buckets. For more information about these bucket types, see [Creating, configuring, and working with Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/creating-buckets-s3.html) in the *Amazon S3 User Guide*.

General purpose buckets exist in a global namespace, which means that each bucket name must be unique across all Amazon Web Services accounts in all the Amazon Web Services Regions within a partition. A partition is a grouping of Regions. Amazon Web Services currently has four partitions: `aws` (Standard Regions), `aws-cn` (China Regions), `aws-us-gov` (Amazon Web Services GovCloud (US)), and `aws-eusc` (European Sovereign Cloud). When you create a general purpose bucket, you can choose to create a bucket in the shared global namespace or you can choose to create a bucket in your account regional namespace. Your account regional namespace is a subdivision of the global namespace that only your account can create buckets in. For more information on account regional namespaces, see [Namespaces for general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/gpbucketnamespaces.html).

### Note

- **General purpose buckets** - If you send your `CreateBucket` request to the `s3.amazonaws.com` global endpoint, the request goes to the `us-east-1` Region. So the signature calculations in Signature Version 4 must use `us-east-1` as the Region, even if the location constraint in the request specifies another Region where the bucket is to be created. If you create a bucket in a Region other than US East (N. Virginia), your application must be able to handle 307 redirect. For more information, see [Virtual hosting of buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/VirtualHosting.html) in the *Amazon S3 User Guide*.

- **Directory buckets** - For directory buckets, you must make requests for this API operation to the Regional endpoint. These endpoints support path-style requests in the format [\`\`](#id1)[https://s3express-control.region-code.amazonaws.com/bucket-name](https://s3express-control.region-code.amazonaws.com/bucket-name) [\`\`](#id3). Virtual-hosted-style requests aren’t supported. For more information about endpoints in Availability Zones, see [Regional and Zonal endpoints for directory buckets in Availability Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/endpoint-directory-buckets-AZ.html) in the *Amazon S3 User Guide*. For more information about endpoints in Local Zones, see [Concepts for directory buckets in Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-lzs-for-directory-buckets.html) in the *Amazon S3 User Guide*.

Permissions

- **General purpose bucket permissions** - In addition to the `s3:CreateBucket` permission, the following permissions are required in a policy when your `CreateBucket` request includes specific headers:

  - **Access control lists (ACLs)** - In your `CreateBucket` request, if you specify an access control list (ACL) and set it to `public-read`, `public-read-write`, `authenticated-read`, or if you explicitly specify any other custom ACLs, both `s3:CreateBucket` and `s3:PutBucketAcl` permissions are required. In your `CreateBucket` request, if you set the ACL to `private`, or if you don’t specify any ACLs, only the `s3:CreateBucket` permission is required.

  - **Object Lock** - In your `CreateBucket` request, if you set `x-amz-bucket-object-lock-enabled` to true, the `s3:PutBucketObjectLockConfiguration` and `s3:PutBucketVersioning` permissions are required.

  - **S3 Object Ownership** - If your `CreateBucket` request includes the `x-amz-object-ownership` header, then the `s3:PutBucketOwnershipControls` permission is required.

  ### Warning

  To set an ACL on a bucket as part of a `CreateBucket` request, you must explicitly set S3 Object Ownership for the bucket to a different value than the default, `BucketOwnerEnforced`. Additionally, if your desired bucket ACL grants public access, you must first create the bucket (without the bucket ACL) and then explicitly disable Block Public Access on the bucket before using `PutBucketAcl` to set the ACL. If you try to create a bucket with a public ACL, the request will fail. For the majority of modern use cases in S3, we recommend that you keep all Block Public Access settings enabled and keep ACLs disabled. If you would like to share data with users outside of your account, you can use bucket policies as needed. For more information, see [Controlling ownership of objects and disabling ACLs for your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) and [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) in the *Amazon S3 User Guide*.

  - **S3 Block Public Access** - If your specific use case requires granting public access to your S3 resources, you can disable Block Public Access. Specifically, you can create a new bucket with Block Public Access enabled, then separately call the [DeletePublicAccessBlock](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeletePublicAccessBlock.html) API. To use this operation, you must have the `s3:PutBucketPublicAccessBlock` permission. For more information about S3 Block Public Access, see [Blocking public access to your Amazon S3 storage](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-control-block-public-access.html) in the *Amazon S3 User Guide*.

- **Directory bucket permissions** - You must have the `s3express:CreateBucket` permission in an IAM identity-based policy instead of a bucket policy. Cross-account access to this API operation isn’t supported. This operation can only be performed by the Amazon Web Services account that owns the resource. For more information about directory bucket policies and permissions, see [Amazon Web Services Identity and Access Management (IAM) for S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-security-iam.html) in the *Amazon S3 User Guide*.

### Warning

The permissions for ACLs, Object Lock, S3 Object Ownership, and S3 Block Public Access are not supported for directory buckets. For directory buckets, all Block Public Access settings are enabled at the bucket level and S3 Object Ownership is set to Bucket owner enforced (ACLs disabled). These settings can’t be modified. For more information about permissions for creating and working with directory buckets, see [Directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-overview.html) in the *Amazon S3 User Guide*. For more information about supported S3 features for directory buckets, see [Features of S3 Express One Zone](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-one-zone.html#s3-express-features) in the *Amazon S3 User Guide*.

HTTP Host header syntax

**Directory buckets** - The HTTP Host header syntax is `s3express-control.region-code.amazonaws.com`.

The following operations are related to `CreateBucket`:

- [PutObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_PutObject.html)

- [DeleteBucket](https://docs.aws.amazon.com/AmazonS3/latest/API/API_DeleteBucket.html)

### Warning

You must URL encode any signed header values that contain spaces. For example, if your header value is `my`` ``file.txt`, containing two spaces after `my`, you must URL encode this value to `my%20%20file.txt`.

See also: [AWS API Documentation](https://docs.aws.amazon.com/goto/WebAPI/s3-2006-03-01/CreateBucket)

### Request Syntax

    response = client.create_bucket(
        ACL='private'|'public-read'|'public-read-write'|'authenticated-read',
        Bucket='string',
        CreateBucketConfiguration={
            'LocationConstraint': 'af-south-1'|'ap-east-1'|'ap-east-2'|'ap-northeast-1'|'ap-northeast-2'|'ap-northeast-3'|'ap-south-1'|'ap-south-2'|'ap-southeast-1'|'ap-southeast-2'|'ap-southeast-3'|'ap-southeast-4'|'ap-southeast-5'|'ap-southeast-6'|'ap-southeast-7'|'ca-central-1'|'ca-west-1'|'cn-north-1'|'cn-northwest-1'|'EU'|'eu-central-1'|'eu-central-2'|'eu-north-1'|'eu-south-1'|'eu-south-2'|'eu-west-1'|'eu-west-2'|'eu-west-3'|'il-central-1'|'me-central-1'|'me-south-1'|'mx-central-1'|'sa-east-1'|'us-east-2'|'us-gov-east-1'|'us-gov-west-1'|'us-west-1'|'us-west-2',
            'Location': {
                'Type': 'AvailabilityZone'|'LocalZone',
                'Name': 'string'
            },
            'Bucket': {
                'DataRedundancy': 'SingleAvailabilityZone'|'SingleLocalZone',
                'Type': 'Directory'
            },
            'Tags': [
                {
                    'Key': 'string',
                    'Value': 'string'
                },
            ]
        },
        GrantFullControl='string',
        GrantRead='string',
        GrantReadACP='string',
        GrantWrite='string',
        GrantWriteACP='string',
        ObjectLockEnabledForBucket=True|False,
        ObjectOwnership='BucketOwnerPreferred'|'ObjectWriter'|'BucketOwnerEnforced',
        BucketNamespace='account-regional'|'global'
    )

Parameters:  
- **ACL** (*string*) –

  The canned ACL to apply to the bucket.

  ### Note

  This functionality is not supported for directory buckets.

- **Bucket** (*string*) –

  **\[REQUIRED\]**

  The name of the bucket to create.

  **General purpose buckets** - For information about bucket naming restrictions, see [Bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) in the *Amazon S3 User Guide*.

  **Directory buckets** - When you use this operation with a directory bucket, you must use path-style requests in the format `https://s3express-control.region-code.amazonaws.com/bucket-name`` ```` ``. ```` ``Virtual-hosted-style`` ``requests`` ``aren't`` ``supported.`` ``Directory`` ``bucket`` ``names`` ``must`` ``be`` ``unique`` ``in`` ``the`` ``chosen`` ``Zone`` ``(Availability`` ``Zone`` ``or`` ``Local`` ``Zone).`` ``Bucket`` ``names`` ``must`` ``also`` ``follow`` ``the`` ``format`` ```` ``bucket-base-name--zone-id--x-s3 ``` (for example, `DOC-EXAMPLE-BUCKET--usw2-az1--x-s3`). For information about bucket naming restrictions, see [Directory bucket naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-bucket-naming-rules.html) in the *Amazon S3 User Guide*

- **CreateBucketConfiguration** (*dict*) –

  The configuration information for the bucket.

  - **LocationConstraint** *(string) –*

    Specifies the Region where the bucket will be created. You might choose a Region to optimize latency, minimize costs, or address regulatory requirements. For example, if you reside in Europe, you will probably find it advantageous to create buckets in the Europe (Ireland) Region.

    If you don’t specify a Region, the bucket is created in the US East (N. Virginia) Region (us-east-1) by default. Configurations using the value `EU` will create a bucket in `eu-west-1`.

    For a list of the valid values for all of the Amazon Web Services Regions, see [Regions and Endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html#s3_region).

    ### Note

    This functionality is not supported for directory buckets.

  - **Location** *(dict) –*

    Specifies the location where the bucket will be created.

    **Directory buckets** - The location type is Availability Zone or Local Zone. To use the Local Zone location type, your account must be enabled for Local Zones. Otherwise, you get an HTTP `403`` ``Forbidden` error with the error code `AccessDenied`. To learn more, see [Enable accounts for Local Zones](https://docs.aws.amazon.com/AmazonS3/latest/userguide/opt-in-directory-bucket-lz.html) in the *Amazon S3 User Guide*.

    ### Note

    This functionality is only supported by directory buckets.

    - **Type** *(string) –*

      The type of location where the bucket will be created.

    - **Name** *(string) –*

      The name of the location where the bucket will be created.

      For directory buckets, the name of the location is the Zone ID of the Availability Zone (AZ) or Local Zone (LZ) where the bucket will be created. An example AZ ID value is `usw2-az1`.

  - **Bucket** *(dict) –*

    Specifies the information about the bucket that will be created.

    ### Note

    This functionality is only supported by directory buckets.

    - **DataRedundancy** *(string) –*

      The number of Zone (Availability Zone or Local Zone) that’s used for redundancy for the bucket.

    - **Type** *(string) –*

      The type of bucket.

  - **Tags** *(list) –*

    An array of tags that you can apply to the bucket that you’re creating. Tags are key-value pairs of metadata used to categorize and organize your buckets, track costs, and control access.

    You must have the `s3:TagResource` permission to create a general purpose bucket with tags or the `s3express:TagResource` permission to create a directory bucket with tags.

    When creating buckets with tags, note that tag-based conditions using `aws:ResourceTag` and `s3:BucketTag` condition keys are applicable only after ABAC is enabled on the bucket. To learn more, see [Enabling ABAC in general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/buckets-tagging-enable-abac.html).

    - *(dict) –*

      A container of a key value name pair.

      - **Key** *(string) –* **\[REQUIRED\]**

        Name of the object key.

      - **Value** *(string) –* **\[REQUIRED\]**

        Value of the tag.

- **GrantFullControl** (*string*) –

  Allows grantee the read, write, read ACP, and write ACP permissions on the bucket.

  ### Note

  This functionality is not supported for directory buckets.

- **GrantRead** (*string*) –

  Allows grantee to list the objects in the bucket.

  ### Note

  This functionality is not supported for directory buckets.

- **GrantReadACP** (*string*) –

  Allows grantee to read the bucket ACL.

  ### Note

  This functionality is not supported for directory buckets.

- **GrantWrite** (*string*) –

  Allows grantee to create new objects in the bucket.

  For the bucket and object owners of existing objects, also allows deletions and overwrites of those objects.

  ### Note

  This functionality is not supported for directory buckets.

- **GrantWriteACP** (*string*) –

  Allows grantee to write the ACL for the applicable bucket.

  ### Note

  This functionality is not supported for directory buckets.

- **ObjectLockEnabledForBucket** (*boolean*) –

  Specifies whether you want S3 Object Lock to be enabled for the new bucket.

  ### Note

  This functionality is not supported for directory buckets.

- **ObjectOwnership** (*string*) –

  The container element for object ownership for a bucket’s ownership controls.

  `BucketOwnerPreferred` - Objects uploaded to the bucket change ownership to the bucket owner if the objects are uploaded with the `bucket-owner-full-control` canned ACL.

  `ObjectWriter` - The uploading account will own the object if the object is uploaded with the `bucket-owner-full-control` canned ACL.

  `BucketOwnerEnforced` - Access control lists (ACLs) are disabled and no longer affect permissions. The bucket owner automatically owns and has full control over every object in the bucket. The bucket only accepts PUT requests that don’t specify an ACL or specify bucket owner full control ACLs (such as the predefined `bucket-owner-full-control` canned ACL or a custom ACL in XML format that grants the same permissions).

  By default, `ObjectOwnership` is set to `BucketOwnerEnforced` and ACLs are disabled. We recommend keeping ACLs disabled, except in uncommon use cases where you must control access for each object individually. For more information about S3 Object Ownership, see [Controlling ownership of objects and disabling ACLs for your bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/about-object-ownership.html) in the *Amazon S3 User Guide*.

  ### Note

  This functionality is not supported for directory buckets. Directory buckets use the bucket owner enforced setting for S3 Object Ownership.

- **BucketNamespace** (*string*) –

  Specifies the namespace where you want to create your general purpose bucket. When you create a general purpose bucket, you can choose to create a bucket in the shared global namespace or you can choose to create a bucket in your account regional namespace. Your account regional namespace is a subdivision of the global namespace that only your account can create buckets in. For more information on bucket namespaces, see [Namespaces for general purpose buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/gpbucketnamespaces.html).

  General purpose buckets in your account regional namespace must follow a specific naming convention. These buckets consist of a bucket name prefix that you create, and a suffix that contains your 12-digit Amazon Web Services Account ID, the Amazon Web Services Region code, and ends with `-an`. Bucket names must follow the format `bucket-name-prefix-accountId-region-an` (for example, `amzn-s3-demo-bucket-111122223333-us-west-2-an`). For information about bucket naming restrictions, see [Account regional namespace naming rules](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html#account-regional-naming-rules) in the *Amazon S3 User Guide*.

  ### Note

  This functionality is not supported for directory buckets.

Return type:  
dict

Returns:  
### Response Syntax

    {
        'Location': 'string',
        'BucketArn': 'string'
    }

### Response Structure

- *(dict) –*

  - **Location** *(string) –*

    A forward slash followed by the name of the bucket for all account regional namespace buckets and all global general purpose buckets created in us-east-1. For example, `/amzn-s3-demo-bucket`. For global general purpose buckets created in other Amazon Web Services Regions, the Location field is the global endpoint URL. For example, `http://amzn-s3-demo-bucket.s3.amazonaws.com/`.

  - **BucketArn** *(string) –*

    The Amazon Resource Name (ARN) of the S3 bucket. ARNs uniquely identify Amazon Web Services resources across all of Amazon Web Services.

    ### Note

    This parameter is only supported for S3 directory buckets. For more information, see [Using tags with directory buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/directory-buckets-tagging.html).

### Exceptions

- `S3.Client.exceptions.BucketAlreadyExists`

- `S3.Client.exceptions.BucketAlreadyOwnedByYou`

### Examples

The following example creates a bucket. The request specifies an AWS region where to create the bucket.

    response = client.create_bucket(
        Bucket='examplebucket',
        CreateBucketConfiguration={
            'LocationConstraint': 'eu-west-1',
        },
    )

    print(response)

Expected Output:

    {
        'Location': 'http://examplebucket.s3.amazonaws.com/',
        'ResponseMetadata': {
            '...': '...',
        },
    }

The following example creates a bucket.

    response = client.create_bucket(
        Bucket='examplebucket',
    )

    print(response)

Expected Output:

    {
        'Location': '/examplebucket',
        'ResponseMetadata': {
            '...': '...',
        },
    }
