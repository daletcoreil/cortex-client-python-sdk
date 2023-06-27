# coding: utf-8

"""
    Dalet Media Cortex API

    # Scope Dalet Mediator API allows you to submit long running media jobs managed by Dalet services.  Long running media jobs include: - **Media processing** such as transcoding or automatic QC. - **Automatic metadata extraction** such as automatic speech transcription or face detection.  The Dalet Mediator API is a REST API with typed schema for the payload. # Architecture Job processing is performed on the cloud via dynamic combination of microservices. Dalet Mediator adopts the [EBU MCMA] architecture.  The key objectives of this architecture are to support: - Job management and monitoring - Long running transactions - Event based communication pattern - Service registration and discovery - Horizontal scalability in an elastic manner  The architecture is implemented using the serverless approach - relying on  independent microservices accessible through well documented REST endpoints and sharing a common object model. ## Roles The following services are involved in the processing of media jobs exposed through the Dalet Media Mediator API: - **Mediator**: this is the main entry point to the architecture; this API endpoint supports: 1. Checking authentication using an API key and a token mechanism 2. Verifying quota restrictions before accepting a submitted job 3. Keeping track of usage so that job processing can be tracked and billed 4. Keeping track of jobs metadata as a job repository - **Job Processor**: once a job request is accepted by the mediator, it is assigned to a Job Processor. The Job Processor dispatches the job to an appropriate Job Worker (depending on the job profile and other criteria such as load on the system and cost of operation).  It then keeps track of the progress of the job and its status until completion and possible failures and timeout.  It reports progress to the Mediator through notifications. - **Job Worker**: The Job Worker performs the actual work on the media object, for example, AI metadata extraction (AME) or essence transcoding.  It reports progress to the Job Processor through notifications. - **Service Registry**: The Service Registry keeps track of all active services in the architecture. It is queried by the Mediator and by Processors to discover candidate services to perform jobs.  It is updated whenever a new service is launched or stopped.  The Service Registry also stores the list of all job profiles supported by one of the Job Workers deployed in the architecture. The Dalet Mediator API abstracts away from the complexity of this orchestration and provides a simple endpoint to submit long running jobs and monitor the progress of their execution.  It serves as a facade for the additional technical services for authentication, usage monitoring and service registry.  [EBU MCMA]: /https://tech.ebu.ch/groups/mcma 'EBU MCMA' ## Job Lifecycle ![Job Lifecyle Diagram](./job_lifecycle.svg 'Job Lifecycle Diagram')  ## Authentication To use the Dalet Mediator API - you must obtain an APIKey from Dalet.  This key comes in the form of two parameters: * client ID * secret  Given these two parameters, a client program must first obtain an access token (GET /auth/access-token) and then associate this token to every subsequent calls.  When the token expires, the API will return a 401 error code.  In this case, the client must request a new token and resubmit the request.   # noqa: E501

    The version of the OpenAPI document: 2.0.0
    Contact: cortexsupport@dalet.com
    Generated by: https://openapi-generator.tech
"""


from __future__ import absolute_import

import unittest
import datetime

import cortex_client
from cortex_client.models.job_mediator_input import JobMediatorInput  # noqa: E501
from cortex_client.rest import ApiException

class TestJobMediatorInput(unittest.TestCase):
    """JobMediatorInput unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional):
        """Test JobMediatorInput
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # model = cortex_client.models.job_mediator_input.JobMediatorInput()  # noqa: E501
        if include_optional :
            return JobMediatorInput(
                project_service_id = 'cjor5rew6n6y2075817kkq4vu', 
                quantity = 50, 
                tracking = None, 
                notification_endpoint = '', 
                job = cortex_client.models.job.Job(
                    job_type = 'AIJob', 
                    job_profile = 'MediaCortexSpeechToText', 
                    region_name = 'eu-west-1', 
                    max_region_latency = 100, 
                    job_input = cortex_client.models.job_input.JobInput(
                        job_input_type = '', ), )
            )
        else :
            return JobMediatorInput(
                project_service_id = 'cjor5rew6n6y2075817kkq4vu',
                quantity = 50,
                job = cortex_client.models.job.Job(
                    job_type = 'AIJob', 
                    job_profile = 'MediaCortexSpeechToText', 
                    region_name = 'eu-west-1', 
                    max_region_latency = 100, 
                    job_input = cortex_client.models.job_input.JobInput(
                        job_input_type = '', ), ),
        )

    def testJobMediatorInput(self):
        """Test JobMediatorInput"""
        inst_req_only = self.make_instance(include_optional=False)
        inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
