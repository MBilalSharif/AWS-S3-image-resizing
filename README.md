# 🖼️ AWS S3 Image Resizer using Lambda
# 📌 Overview

This project is a serverless image processing pipeline built using AWS services. It automatically resizes images uploaded to an S3 bucket and stores the processed images in a separate folder. The system is designed with security, scalability, and cost-efficiency in mind using the least privilege IAM principle.

Additionally, a scheduled cleanup mechanism was implemented using a cron-based trigger to empty the bucket at the end of the day (EOD). This was tested and removed afterward to avoid unintended data loss or charges.

# 🚀 Architecture
Upload image → S3 uploads/ folder
Trigger → AWS Lambda function
Processing → Image resizing using Python (Pillow)
Output → S3 resized/ folder
Cleanup → EventBridge scheduled Lambda (temporary cron job)

# 🧰 Tech Stack
AWS Lambda
Amazon S3
Amazon EventBridge
Python
Pillow (PIL)
Boto3 (AWS SDK for Python)

# ⚙️ Features
📥 Automatic image processing on upload
🖼️ Image resizing using Lambda
📂 Organized folder structure (uploads/, resized/)
🔐 Secure IAM role with least privilege access
⏰ Scheduled cleanup using cron (EventBridge)
💰 Cost-aware design (cleanup removed after validation)
🔐 IAM Security (Least Privilege)

The Lambda execution role is restricted to only required actions:

s3:GetObject → Read uploaded images
s3:PutObject → Save resized images

No unnecessary permissions are granted, following AWS security best practices.

📂 **Project Structure**

```
AWS-S3-image-resizing/
│
├── lambda_function.py      # Main Lambda function (image resizing logic)
├── requirements.txt        # Python dependencies
├── iam-policy.json         # IAM role permissions (least privilege)
├── event.json              # Sample S3 event for testing
├── README.md               # Project documentation
```


# 🔄 Workflow
User uploads image to S3 uploads/ folder
AWS Lambda is triggered automatically
Image is processed and resized
Resized image is stored in resized/ folder
(Optional) Scheduled cleanup removes files at EOD via Amazon EventBridge
# 🧪 How to Test

Upload an image to:

s3://your-bucket/uploads/
Lambda triggers automatically

Check output in:

s3://your-bucket/resized/

# 📊 Key Learning Outcomes
Event-driven architecture on AWS
Serverless computing with Lambda
S3 event triggers
IAM security best practices
Scheduled automation using EventBridge
Real-world cloud cost optimization techniques

<img width="1357" height="403" alt="image" src="https://github.com/user-attachments/assets/0fcb2a97-e7de-413d-b81a-8dbf84311e5f" />
<img width="1354" height="530" alt="image" src="https://github.com/user-attachments/assets/924506a3-964b-4e4b-87f4-197dc8f015d6" />


# ⚠️ Important Note

The cron-based cleanup function was temporarily used for testing purposes only and removed after verification to prevent accidental data loss or unexpected AWS charges.
