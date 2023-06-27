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
**vocabulary** | [**list[SpeechToTextVocabulary]**](SpeechToTextVocabulary.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


