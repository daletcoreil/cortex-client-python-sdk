# coding: utf-8

"""
    Dalet Media Cortex API

    # Scope Dalet Mediator API allows you to submit long running media jobs managed by Dalet services.  Long running media jobs include: - **Media processing** such as transcoding or automatic QC. - **Automatic metadata extraction** such as automatic speech transcription or face detection.  The Dalet Mediator API is a REST API with typed schema for the payload. # Architecture Job processing is performed on the cloud via dynamic combination of microservices. Dalet Mediator adopts the [EBU MCMA] architecture.  The key objectives of this architecture are to support: - Job management and monitoring - Long running transactions - Event based communication pattern - Service registration and discovery - Horizontal scalability in an elastic manner  The architecture is implemented using the serverless approach - relying on  independent microservices accessible through well documented REST endpoints and sharing a common object model. ## Roles The following services are involved in the processing of media jobs exposed through the Dalet Media Mediator API: - **Mediator**: this is the main entry point to the architecture; this API endpoint supports: 1. Checking authentication using an API key and a token mechanism 2. Verifying quota restrictions before accepting a submitted job 3. Keeping track of usage so that job processing can be tracked and billed 4. Keeping track of jobs metadata as a job repository - **Job Processor**: once a job request is accepted by the mediator, it is assigned to a Job Processor. The Job Processor dispatches the job to an appropriate Job Worker (depending on the job profile and other criteria such as load on the system and cost of operation).  It then keeps track of the progress of the job and its status until completion and possible failures and timeout.  It reports progress to the Mediator through notifications. - **Job Worker**: The Job Worker performs the actual work on the media object, for example, AI metadata extraction (AME) or essence transcoding.  It reports progress to the Job Processor through notifications. - **Service Registry**: The Service Registry keeps track of all active services in the architecture. It is queried by the Mediator and by Processors to discover candidate services to perform jobs.  It is updated whenever a new service is launched or stopped.  The Service Registry also stores the list of all job profiles supported by one of the Job Workers deployed in the architecture. The Dalet Mediator API abstracts away from the complexity of this orchestration and provides a simple endpoint to submit long running jobs and monitor the progress of their execution.  It serves as a facade for the additional technical services for authentication, usage monitoring and service registry.  [EBU MCMA]: /https://tech.ebu.ch/groups/mcma 'EBU MCMA' ## Job Lifecycle ![Job Lifecyle Diagram](./job_lifecycle.svg 'Job Lifecycle Diagram')  ## Authentication To use the Dalet Mediator API - you must obtain an APIKey from Dalet.  This key comes in the form of two parameters: * client ID * secret  Given these two parameters, a client program must first obtain an access token (GET /auth/access-token) and then associate this token to every subsequent calls.  When the token expires, the API will return a 401 error code.  In this case, the client must request a new token and resubmit the request.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: cortexsupport@dalet.com
    Generated by: https://openapi-generator.tech
"""


try:
    from inspect import getfullargspec
except ImportError:
    from inspect import getargspec as getfullargspec
import pprint
import re  # noqa: F401
import six

from cortex_client.configuration import Configuration


class Locator(object):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    """
    Attributes:
      openapi_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    openapi_types = {
        'aws_s3_bucket': 'str',
        'aws_s3_key': 'str',
        'http_endpoint': 'str'
    }

    attribute_map = {
        'aws_s3_bucket': 'awsS3Bucket',
        'aws_s3_key': 'awsS3Key',
        'http_endpoint': 'httpEndpoint'
    }

    def __init__(self, aws_s3_bucket=None, aws_s3_key=None, http_endpoint=None, local_vars_configuration=None):  # noqa: E501
        """Locator - a model defined in OpenAPI"""  # noqa: E501
        if local_vars_configuration is None:
            local_vars_configuration = Configuration.get_default_copy()
        self.local_vars_configuration = local_vars_configuration

        self._aws_s3_bucket = None
        self._aws_s3_key = None
        self._http_endpoint = None
        self.discriminator = None

        self.aws_s3_bucket = aws_s3_bucket
        self.aws_s3_key = aws_s3_key
        self.http_endpoint = http_endpoint

    @property
    def aws_s3_bucket(self):
        """Gets the aws_s3_bucket of this Locator.  # noqa: E501

        Name of an AWS S3 bucket  # noqa: E501

        :return: The aws_s3_bucket of this Locator.  # noqa: E501
        :rtype: str
        """
        return self._aws_s3_bucket

    @aws_s3_bucket.setter
    def aws_s3_bucket(self, aws_s3_bucket):
        """Sets the aws_s3_bucket of this Locator.

        Name of an AWS S3 bucket  # noqa: E501

        :param aws_s3_bucket: The aws_s3_bucket of this Locator.  # noqa: E501
        :type aws_s3_bucket: str
        """
        if self.local_vars_configuration.client_side_validation and aws_s3_bucket is None:  # noqa: E501
            raise ValueError("Invalid value for `aws_s3_bucket`, must not be `None`")  # noqa: E501

        self._aws_s3_bucket = aws_s3_bucket

    @property
    def aws_s3_key(self):
        """Gets the aws_s3_key of this Locator.  # noqa: E501

        Name of a file in the AWS S3 bucket. For example, name of media file to be indexed in an Input Locator or name of a JSON file in an Output Locator.  # noqa: E501

        :return: The aws_s3_key of this Locator.  # noqa: E501
        :rtype: str
        """
        return self._aws_s3_key

    @aws_s3_key.setter
    def aws_s3_key(self, aws_s3_key):
        """Sets the aws_s3_key of this Locator.

        Name of a file in the AWS S3 bucket. For example, name of media file to be indexed in an Input Locator or name of a JSON file in an Output Locator.  # noqa: E501

        :param aws_s3_key: The aws_s3_key of this Locator.  # noqa: E501
        :type aws_s3_key: str
        """
        if self.local_vars_configuration.client_side_validation and aws_s3_key is None:  # noqa: E501
            raise ValueError("Invalid value for `aws_s3_key`, must not be `None`")  # noqa: E501

        self._aws_s3_key = aws_s3_key

    @property
    def http_endpoint(self):
        """Gets the http_endpoint of this Locator.  # noqa: E501

        Public URL to access the file in the bucket. Must be computed using the AWS SDK method `GeneratePresignedUrl`  # noqa: E501

        :return: The http_endpoint of this Locator.  # noqa: E501
        :rtype: str
        """
        return self._http_endpoint

    @http_endpoint.setter
    def http_endpoint(self, http_endpoint):
        """Sets the http_endpoint of this Locator.

        Public URL to access the file in the bucket. Must be computed using the AWS SDK method `GeneratePresignedUrl`  # noqa: E501

        :param http_endpoint: The http_endpoint of this Locator.  # noqa: E501
        :type http_endpoint: str
        """
        if self.local_vars_configuration.client_side_validation and http_endpoint is None:  # noqa: E501
            raise ValueError("Invalid value for `http_endpoint`, must not be `None`")  # noqa: E501

        self._http_endpoint = http_endpoint

    def to_dict(self, serialize=False):
        """Returns the model properties as a dict"""
        result = {}

        def convert(x):
            if hasattr(x, "to_dict"):
                args = getfullargspec(x.to_dict).args
                if len(args) == 1:
                    return x.to_dict()
                else:
                    return x.to_dict(serialize)
            else:
                return x

        for attr, _ in six.iteritems(self.openapi_types):
            value = getattr(self, attr)
            attr = self.attribute_map.get(attr, attr) if serialize else attr
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: convert(x),
                    value
                ))
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], convert(item[1])),
                    value.items()
                ))
            else:
                result[attr] = convert(value)

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Locator):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Locator):
            return True

        return self.to_dict() != other.to_dict()
