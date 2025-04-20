# cortex_client.AuthApi

All URIs are relative to *https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_access_token**](AuthApi.md#get_access_token) | **POST** /auth/access-token | 


# **get_access_token**
> Token get_access_token(client, secret)

Generate new access token

### Example


```python
import cortex_client
from cortex_client.models.token import Token
from cortex_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod
# See configuration.py for a list of all supported configuration parameters.
configuration = cortex_client.Configuration(
    host = "https://svi6ps1cih.execute-api.us-east-1.amazonaws.com/preprod"
)


# Enter a context with an instance of the API client
with cortex_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = cortex_client.AuthApi(api_client)
    client = 'client_example' # str | client_id of the application
    secret = 'secret_example' # str | secret_key of the application

    try:
        api_response = api_instance.get_access_token(client, secret)
        print("The response of AuthApi->get_access_token:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_access_token: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | **str**| client_id of the application | 
 **secret** | **str**| secret_key of the application | 

### Return type

[**Token**](Token.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Success response |  -  |
**401** | Invalid secret or client |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

