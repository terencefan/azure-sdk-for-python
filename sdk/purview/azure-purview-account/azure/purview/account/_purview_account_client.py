# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from copy import deepcopy
from typing import TYPE_CHECKING

from azure.core import PipelineClient
from msrest import Deserializer, Serializer

from ._configuration import PurviewAccountClientConfiguration
from .operations import AccountsOperations, CollectionsOperations, ResourceSetRulesOperations

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Dict, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.rest import HttpRequest, HttpResponse

class PurviewAccountClient(object):
    """Creates a Microsoft.Purview data plane account client.

    :ivar accounts: AccountsOperations operations
    :vartype accounts: azure.purview.account.operations.AccountsOperations
    :ivar collections: CollectionsOperations operations
    :vartype collections: azure.purview.account.operations.CollectionsOperations
    :ivar resource_set_rules: ResourceSetRulesOperations operations
    :vartype resource_set_rules: azure.purview.account.operations.ResourceSetRulesOperations
    :param endpoint: The account endpoint of your Purview account. Example:
     https://{accountName}.purview.azure.com/account/.
    :type endpoint: str
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    """

    def __init__(
        self,
        endpoint,  # type: str
        credential,  # type: "TokenCredential"
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        _endpoint = '{endpoint}'
        self._config = PurviewAccountClientConfiguration(endpoint, credential, **kwargs)
        self._client = PipelineClient(base_url=_endpoint, config=self._config, **kwargs)

        self._serialize = Serializer()
        self._deserialize = Deserializer()
        self._serialize.client_side_validation = False
        self.accounts = AccountsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.collections = CollectionsOperations(self._client, self._config, self._serialize, self._deserialize)
        self.resource_set_rules = ResourceSetRulesOperations(self._client, self._config, self._serialize, self._deserialize)


    def send_request(
        self,
        request,  # type: HttpRequest
        **kwargs  # type: Any
    ):
        # type: (...) -> HttpResponse
        """Runs the network request through the client's chained policies.

        We have helper methods to create requests specific to this service in `azure.purview.account.rest`.
        Use these helper methods to create the request you pass to this method.


        For more information on this code flow, see https://aka.ms/azsdk/python/protocol/quickstart

        For advanced cases, you can also create your own :class:`~azure.core.rest.HttpRequest`
        and pass it in.

        :param request: The network request you want to make. Required.
        :type request: ~azure.core.rest.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to False.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.rest.HttpResponse
        """

        request_copy = deepcopy(request)
        path_format_arguments = {
            "endpoint": self._serialize.url("self._config.endpoint", self._config.endpoint, 'str', skip_quote=True),
        }

        request_copy.url = self._client.format_url(request_copy.url, **path_format_arguments)
        return self._client.send_request(request_copy, **kwargs)

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> PurviewAccountClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
