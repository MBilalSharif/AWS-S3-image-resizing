import boto3
from PIL import Image
import io
import mimetypes

s3 = boto3.client("s3")
RESIZE_TO = (300, 300)

def lambda_handler(event, context):
    bucket = event["Records"][0]["s3"]["bucket"]["name"]
    key = event["Records"][0]["s3"]["object"]["key"]

    if not key.startswith("uploads/"):
        return "Skipped: not an upload"

    # Download, resize, and re-upload
    image = download_image(bucket, key)
    resized = resize_image(image)
    upload_image(resized, bucket, key)

    return f"Done: resized/{key.split('uploads/')[-1]}"


def download_image(bucket, key):
    data = s3.get_object(Bucket=bucket, Key=key)["Body"].read()
    return Image.open(io.BytesIO(data))


def resize_image(img):
    fmt = img.format or "JPEG"

    # JPEG doesn't support transparency — convert if needed
    if fmt.upper() == "JPEG" and img.mode in ("RGBA", "P"):
        img = img.convert("RGB")

    return img.resize(RESIZE_TO, Image.LANCZOS), fmt


def upload_image(image_and_fmt, bucket, key):
    img, fmt = image_and_fmt
    new_key = key.replace("uploads/", "resized/")

    buffer = io.BytesIO()
    img.save(buffer, format=fmt)
    buffer.seek(0)

    content_type, _ = mimetypes.guess_type(new_key)
    s3.put_object(
        Bucket=bucket,
        Key=new_key,
        Body=buffer,
        ContentType=content_type or "image/jpeg"
    )
    print(f"Uploaded → {new_key}")