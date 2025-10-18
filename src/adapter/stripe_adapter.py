from .base import PaymentAdapter, PaymentSession, PaymentAdapterError
import stripe


class StripeAdapter(PaymentAdapter):
    def __init__(self, api_key: str, webhook_secret: str):
        self.api_key = api_key
        self.webhook_secret = webhook_secret
        stripe.api_key = self.api_key

    async def create_checkout_session(self, payment_data):
        pass