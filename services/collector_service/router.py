import config
import faststream.rabbit.fastapi
import utils.linked_routers.faststream_router

import services.collector_service.schemas

import fastapi


router: faststream.rabbit.fastapi.RabbitRouter = (
    utils.linked_routers.faststream_router.FastStreamRouter(
        config.settings.rabbitmq.rabbitmq_url,
    )
)


@router.post(
    "/handshake",
    tags=["Handshake"],
    response_model=services.collector_service.schemas.HandshakeResponse,
)
async def handshake(
    payload: services.collector_service.schemas.HandshakeRequest,
):
    try:
        # TODO: здесь должна быть проверка пользователя и устройства в БД
        # - проверить существует ли пользователь
        # - проверить совпадение codeWord
        # - проверить/создать устройство
        # - запустить/обновить сессию рукопожатия
        #
        # пока сервис возвращает только success без привязки к данным

        result = "success"  # заглушка вместо логики с базой

        if result == "user_not_found":
            raise fastapi.HTTPException(
                status_code=fastapi.status.HTTP_404_NOT_FOUND,
                detail="Пользователь с таким username не найден",
            )
        elif result == "invalid_code_word":
            raise fastapi.HTTPException(
                status_code=fastapi.status.HTTP_403_FORBIDDEN,
                detail="Неверный codeWord",
            )

        return services.collector_service.schemas.HandshakeResponse(
            status="success",
            message="Handshake completed",
        )

    except Exception as e:
        raise fastapi.HTTPException(status_code=500, detail=str(e))


@router.post(
    "/notification",
    tags=["Notification Collection"],
    response_model=(
        services.collector_service.schemas.NotificationCollectResponse
    ),
)
async def notification_collect(
    payload: services.collector_service.schemas.NotificationCollectRequest,
):
    try:
        data = payload.dict() # noqa

        # TODO: здесь должна быть логика работы с уведомлениями:
        # - валидация username и codeWord
        #   (проверка в БД или через внешний сервис)
        # - создание объекта уведомления
        # - отправка уведомления пользователю
        # - сохранение/обработка уведомления в хранилище
        #
        # сейчас сервис возвращает заглушку

        result = "success"  # заглушка вместо логики с базой

        if result == "missing_fields":
            raise fastapi.HTTPException(
                status_code=400, detail="username и codeWord обязательны"
            )
        elif result == "user_not_found":
            raise fastapi.HTTPException(
                status_code=404,
                detail="Пользователь с таким username не найден",
            )
        elif result == "invalid_code_word":
            raise fastapi.HTTPException(
                status_code=403, detail="Неверный codeWord"
            )

        return services.collector_service.schemas.NotificationCollectResponse(
            status="success"
        )

    except Exception as e:
        raise fastapi.HTTPException(status_code=500, detail=str(e))
