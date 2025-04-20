# VideoAnalysisInput

Describe the input and expected output of the job to be executed by Media Cortex. Files are specified using FIMS Essence Locators.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file** | [**Locator**](Locator.md) |  | 
**output_location** | [**Locator**](Locator.md) |  | 
**data_filter** | **List[str]** | Determine which types of AI analyses are to be indexed. | [optional] 
**language** | **str** | Language of the media file to be indexed according to ISO 639-1 Language Name. See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes.  Used in Job/inputFile | [optional] 
**start_of_material** | **float** | Indicate the timecode of the first frame in the media in seconds.  Generated subtitles start from this time. | [optional] 

## Example

```python
from cortex_client.models.video_analysis_input import VideoAnalysisInput

# TODO update the JSON string below
json = "{}"
# create an instance of VideoAnalysisInput from a JSON string
video_analysis_input_instance = VideoAnalysisInput.from_json(json)
# print the JSON string representation of the object
print(VideoAnalysisInput.to_json())

# convert the object into a dict
video_analysis_input_dict = video_analysis_input_instance.to_dict()
# create an instance of VideoAnalysisInput from a dict
video_analysis_input_from_dict = VideoAnalysisInput.from_dict(video_analysis_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


