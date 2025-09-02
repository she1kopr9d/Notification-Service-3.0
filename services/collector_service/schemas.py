import pydantic
import typing


class HandshakeRequest(pydantic.BaseModel):
    deviceId: str
    username: str
    codeWord: str
    model: typing.Optional[str] = "Неизвестно"
    manufacturer: typing.Optional[str] = "Неизвестно"
    osVersion: typing.Optional[str] = "Неизвестно"


class HandshakeResponse(pydantic.BaseModel):
    status: str
    message: typing.Optional[str] = None
    error: typing.Optional[str] = None


class DeviceInfo(pydantic.BaseModel):
    deviceId: typing.Optional[str] = None
    username: typing.Optional[str] = None
    codeWord: typing.Optional[str] = None
    model: typing.Optional[str] = None
    manufacturer: typing.Optional[str] = None
    osVersion: typing.Optional[str] = None


class NotificationCollectRequest(pydantic.BaseModel):
    deviceInfo: DeviceInfo
    data: typing.Optional[typing.Dict[str, typing.Any]] = None


class NotificationCollectResponse(pydantic.BaseModel):
    status: str
    error: typing.Optional[str] = None
