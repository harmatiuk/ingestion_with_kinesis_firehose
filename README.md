# Data Ingestion with Kinesis Firehose

The purpose of this repository is to apply a data ingestion with Amazon Kinesis Firehose saving that data to S3. After that I use AWS Glue to catalog and Athena to query the data.
Basically I created this scenario:

![image](https://user-images.githubusercontent.com/32557663/202899919-ab26e7ae-3459-476e-8e94-3327e338fd5b.png)

---
# The Data

For the data, I used the Fake Web Events lib (https://github.com/andresionek91/fake-web-events) which is a fake web event generator. Where you can use to generate semi-random web events for your study.

---
# Tools

 * **Kinesis Data Firehose:** <br>
  Amazon Kinesis Data Firehose is an extract, transform, and load (ETL) service that reliably captures, transforms, and delivers streaming data to data lakes, data stores, and analytics services.
 * **S3 Bucket:** <br>
   Amazon S3 buckets, which are similar to file folders, store objects, which consist of data and its descriptive metadata.
 * **Glue Data Catalog:** <br>
   Amazon Glue Data Catalog provides a uniform repository where disparate systems can store and find metadata to keep track of data in data silos. You can then use the metadata to query and transform that data in a consistent manner across a wide variety of applications.
 * **Athena:** <br>
  Amazon Athena is a serverless, interactive query service to query data and analyze big data in Amazon S3 using standard SQL.
 * **Boto3:** <br>
  Boto3 makes it easy to integrate your Python application, library, or script with AWS services including Amazon S3, Amazon EC2, Amazon DynamoDB, and more.
