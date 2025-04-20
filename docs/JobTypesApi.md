# cortex_client.JobTypesApi

All URIs are relative to *https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_all_job_types**](JobTypesApi.md#get_all_job_types) | **GET** /job-types | 


# **get_all_job_types**
> List[JobType] get_all_job_types(project_service_id)

Get all job types including their metadata.

### Example

* Api Key Authentication (tokenSignature):

```python
import cortex_client
from cortex_client.models.job_type import JobType
from cortex_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod
# See configuration.py for a list of all supported configuration parameters.
configuration = cortex_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: tokenSignature
configuration.api_key['tokenSignature'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['tokenSignature'] = 'Bearer'

# Enter a context with an instance of the API client
with cortex_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cortex_client.JobTypesApi(api_client)
    project_service_id = 'project_service_id_example' # str | Project service id of the client which associated to the request

    try:
        api_response = api_instance.get_all_job_types(project_service_id)
        print("The response of JobTypesApi->get_all_job_types:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling JobTypesApi->get_all_job_types: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **project_service_id** | **str**| Project service id of the client which associated to the request | 

### Return type

[**List[JobType]**](JobType.md)

### Authorization

[tokenSignature](../README.md#tokenSignature)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

