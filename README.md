# Data Ingestion with Kinesis Firehose

The purpose of this repository is to apply a data ingestion with Amazon Kinesis Firehose saving that data to S3 using the boto3. After that I use AWS Glue to catalog and Athena to query the data.
Basically I created this scenario:

![image](https://user-images.githubusercontent.com/32557663/202899919-ab26e7ae-3459-476e-8e94-3327e338fd5b.png)

---
# The Data

For the data, I used the Fake Web Events lib (https://github.com/andresionek91/fake-web-events) which is a fake web event generator. Where you can use to generate semi-random web events for your study.
