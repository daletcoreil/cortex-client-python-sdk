# SpeechToTextVocabulary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**content** | **str** |  | [optional] 
**sounds_like** | **List[str]** |  | [optional] 

## Example

```python
from cortex_client.models.speech_to_text_vocabulary import SpeechToTextVocabulary

# TODO update the JSON string below
json = "{}"
# create an instance of SpeechToTextVocabulary from a JSON string
speech_to_text_vocabulary_instance = SpeechToTextVocabulary.from_json(json)
# print the JSON string representation of the object
print(SpeechToTextVocabulary.to_json())

# convert the object into a dict
speech_to_text_vocabulary_dict = speech_to_text_vocabulary_instance.to_dict()
# create an instance of SpeechToTextVocabulary from a dict
speech_to_text_vocabulary_from_dict = SpeechToTextVocabulary.from_dict(speech_to_text_vocabulary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


