# SpeechToTextOutput

Specifies where the captions computed by the Media Cortex service are to be stored.  Different formats can be requested (EBU-TT, SRT, JSON or text). <ul> <li>jsonFormat - Location of the output file into which metadata will be stored in JSON format.  The JSON format provides a timestamp for each transcribed. </li> <li>ttmlFormat - Location of the output file into which the speech transcription will be stored as subtitles encode in EBU-TT (TTML) format.  See https://tech.ebu.ch/docs/tech/tech3350.pdf. </li> <li>srtFormat - Location of the output file into which the speech transcription will be stored as subtitles encode in SRT format. See https://en.wikipedia.org/wiki/SubRip. </li> <li>textFormat - Location of the output file into which the text of the speech transcription will be stored in simple format with no timestamps. </li> <li>draftjsFormat - Location of the output file into which the text of the speech transcription will be stored in draftjs format. </li> </ul>

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**json_format** | [**Locator**](Locator.md) |  | [optional] 
**ttml_format** | [**Locator**](Locator.md) |  | [optional] 
**srt_format** | [**Locator**](Locator.md) |  | [optional] 
**text_format** | [**Locator**](Locator.md) |  | [optional] 
**draftjs_format** | [**Locator**](Locator.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


