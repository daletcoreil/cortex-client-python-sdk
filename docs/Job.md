# Job


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_type** | **str** |  | [optional] 
**job_profile** | **str** | Define what type of job is to be executed on the media object. | [optional] 
**region_name** | **str** | If defined, require job to be run on a Worker instance that can serve any of the regions, else can run on any Worker instance. If no service is available for the requested regions, the job fails. | [optional] 
**max_region_latency** | **int** | If defined, require job to be run on a Worker instance that can access the requested region with a latency less than this value | [optional] [default to 100]
**job_input** | [**JobInput**](JobInput.md) |  | [optional] 

## Example

```python
from cortex_client.models.job import Job

# TODO update the JSON string below
json = "{}"
# create an instance of Job from a JSON string
job_instance = Job.from_json(json)
# print the JSON string representation of the object
print(Job.to_json())

# convert the object into a dict
job_dict = job_instance.to_dict()
# create an instance of Job from a dict
job_from_dict = Job.from_dict(job_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


