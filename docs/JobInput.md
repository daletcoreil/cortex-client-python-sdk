# JobInput

Can be either VideoAnalysisInput or SpeechToTextInput.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_input_type** | **str** |  | 

## Example

```python
from cortex_client.models.job_input import JobInput

# TODO update the JSON string below
json = "{}"
# create an instance of JobInput from a JSON string
job_input_instance = JobInput.from_json(json)
# print the JSON string representation of the object
print(JobInput.to_json())

# convert the object into a dict
job_input_dict = job_input_instance.to_dict()
# create an instance of JobInput from a dict
job_input_from_dict = JobInput.from_dict(job_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


