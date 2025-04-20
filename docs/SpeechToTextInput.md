# SpeechToTextInput

Describe the input and expected output of the job to be executed by Media Cortex. Files are specified using FIMS Essence Locators. Specifies which media file is to be indexed by the Media Cortex service, its language, and a user defined name associated to the job.  This job produces captions for the media in EBU-TT, JSON and textual formats

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**input_file** | [**Locator**](Locator.md) |  | 
**output_location** | [**SpeechToTextOutput**](SpeechToTextOutput.md) |  | 
**title** | **str** | Readable name associated to the job when submitted to Media Cortex service. | [optional] 
**language** | **str** | Language of the media file to be indexed according to ISO 639-1 Language Name. See https://en.wikipedia.org/wiki/List_of_ISO_639-1_codes.  Used in Job/inputFile | [optional] 
**start_of_material** | **float** | Indicate the timecode of the first frame in the media in seconds.  Generated subtitles start from this time. | [optional] 
**vocabulary** | [**List[SpeechToTextVocabulary]**](SpeechToTextVocabulary.md) |  | [optional] 
**caption_format_standard** | **str** | Which standard will be used for caption formatting. EBU-TT, CEA-608 and CEA-708 are supported standards. | [optional] 

## Example

```python
from cortex_client.models.speech_to_text_input import SpeechToTextInput

# TODO update the JSON string below
json = "{}"
# create an instance of SpeechToTextInput from a JSON string
speech_to_text_input_instance = SpeechToTextInput.from_json(json)
# print the JSON string representation of the object
print(SpeechToTextInput.to_json())

# convert the object into a dict
speech_to_text_input_dict = speech_to_text_input_instance.to_dict()
# create an instance of SpeechToTextInput from a dict
speech_to_text_input_from_dict = SpeechToTextInput.from_dict(speech_to_text_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


