# JobType

List of job profiles accossiated to job type.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**profiles** | **List[str]** |  | 

## Example

```python
from cortex_client.models.job_type import JobType

# TODO update the JSON string below
json = "{}"
# create an instance of JobType from a JSON string
job_type_instance = JobType.from_json(json)
# print the JSON string representation of the object
print(JobType.to_json())

# convert the object into a dict
job_type_dict = job_type_instance.to_dict()
# create an instance of JobType from a dict
job_type_from_dict = JobType.from_dict(job_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


