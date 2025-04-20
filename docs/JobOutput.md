# JobOutput

Where the output of the job analysis will be stored. Can be either VideoAnalysisOutput or SpeechToTextOutput.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_output_type** | **str** |  | 

## Example

```python
from cortex_client.models.job_output import JobOutput

# TODO update the JSON string below
json = "{}"
# create an instance of JobOutput from a JSON string
job_output_instance = JobOutput.from_json(json)
# print the JSON string representation of the object
print(JobOutput.to_json())

# convert the object into a dict
job_output_dict = job_output_instance.to_dict()
# create an instance of JobOutput from a dict
job_output_from_dict = JobOutput.from_dict(job_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


