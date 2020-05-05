# Locator

Generic description of a file location according to the EBU FIMS specification.
## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_s3_bucket** | **str** | Name of an AWS S3 bucket | 
**aws_s3_key** | **str** | Name of a file in the AWS S3 bucket. For example, name of media file to be indexed in an Input Locator or name of a JSON file in an Output Locator. | 
**http_endpoint** | **str** | Public URL to access the file in the bucket. Must be computed using the AWS SDK method &#x60;GeneratePresignedUrl&#x60; | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


