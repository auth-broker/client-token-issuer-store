from typing import *
from typing import Literal

from pydantic import BaseModel, Field

from .Oauth2Client import Oauth2Client
from .Oauth2Flow import Oauth2Flow
from .TokenIssuerType import TokenIssuerType


class OAuth2TokenIssuer_Output(BaseModel):
    """
    OAuth2TokenIssuer model
    """

    model_config = {"populate_by_name": True, "validate_assignment": True}

    oauth2_flow: Oauth2Flow = Field(validation_alias="oauth2_flow")

    oauth2_client: Oauth2Client = Field(validation_alias="oauth2_client")

    identity_provider: Optional[str] = Field(validation_alias="identity_provider", default="Google")

    response_type: Optional[str] = Field(validation_alias="response_type", default="code")

    scope: Optional[str] = Field(validation_alias="scope", default="openid email profile")

    type: Literal[TokenIssuerType.OAUTH2] = Field(validation_alias="type", default=TokenIssuerType.OAUTH2)
