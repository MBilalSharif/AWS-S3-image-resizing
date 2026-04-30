import boto3

s3 = boto3.client("s3")

def lambda_handler(event, context):
    bucket = "image-bucket-bilal"

    print("Starting cleanup...")

    # List objects
    objects = s3.list_objects_v2(Bucket=bucket)

    if "Contents" not in objects:
        print("Bucket already empty")
        return "Nothing to delete"

    # Collect keys
    keys = [{"Key": obj["Key"]} for obj in objects["Contents"]]

    # Delete in batch
    s3.delete_objects(
        Bucket=bucket,
        Delete={"Objects": keys}
    )

    print(f"Deleted {len(keys)} objects")
    return "Cleanup done"