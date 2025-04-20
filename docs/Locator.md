# Locator

Generic description of a file location according to the EBU FIMS specification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_s3_bucket** | **str** | Name of an AWS S3 bucket | 
**aws_s3_key** | **str** | Name of a file in the AWS S3 bucket. For example, name of media file to be indexed in an Input Locator or name of a JSON file in an Output Locator. | 
**http_endpoint** | **str** | Public URL to access the file in the bucket. Must be computed using the AWS SDK method &#x60;GeneratePresignedUrl&#x60; | 

## Example

```python
from cortex_client.models.locator import Locator

# TODO update the JSON string below
json = "{}"
# create an instance of Locator from a JSON string
locator_instance = Locator.from_json(json)
# print the JSON string representation of the object
print(Locator.to_json())

# convert the object into a dict
locator_dict = locator_instance.to_dict()
# create an instance of Locator from a dict
locator_from_dict = Locator.from_dict(locator_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


