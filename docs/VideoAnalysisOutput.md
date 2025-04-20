# VideoAnalysisOutput


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_file** | [**Locator**](Locator.md) |  | [optional] 

## Example

```python
from cortex_client.models.video_analysis_output import VideoAnalysisOutput

# TODO update the JSON string below
json = "{}"
# create an instance of VideoAnalysisOutput from a JSON string
video_analysis_output_instance = VideoAnalysisOutput.from_json(json)
# print the JSON string representation of the object
print(VideoAnalysisOutput.to_json())

# convert the object into a dict
video_analysis_output_dict = video_analysis_output_instance.to_dict()
# create an instance of VideoAnalysisOutput from a dict
video_analysis_output_from_dict = VideoAnalysisOutput.from_dict(video_analysis_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


