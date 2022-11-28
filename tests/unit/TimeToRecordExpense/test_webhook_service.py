import pytest
from unittest import mock

import linebot.exceptions

from TimeToRecordExpense import webhook_service


@pytest.mark.asyncio
async def test_webhook_api_should_return_400_if_signature_validation_failed():
    with mock.patch("TimeToRecordExpense.message_handlers.handler") as mock_handler:
        mock_request = mock.AsyncMock()
        mock_handler.handle.side_effect = linebot.exceptions.InvalidSignatureError

        response = await webhook_service.callback(mock_request, "signature")

        assert response.status_code == 400


@pytest.mark.asyncio
async def test_webhook_api_should_return_200_if_signature_validation_pass():
    with mock.patch("TimeToRecordExpense.message_handlers.handler"):
        mock_request = mock.AsyncMock()

        response = await webhook_service.callback(mock_request, "signature")

        assert response.status_code == 200
