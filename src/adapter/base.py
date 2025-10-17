from abc import ABC, abstractmethod
from pydantic import BaseModel


# ============================================================================
# BASE ADAPTER PATTERN - GENERAL PAYMENT INTERFACE
# ============================================================================


# Die BASE soll ein INTERFACE sein, das alle Payment Provider implementieren müssen.
# Allgemein für Stripe, Mollie, PayPal, etc.

# GEDANKENGÄNGE ZUR STRUKTUR:

# 1. PaymentSession Dataclass
#    - Was muss hier rein, damit es für ALLE Provider funktioniert?
#    - Welche Felder sind universal?
#    - Welche sind Provider-spezifisch?

class PaymentSession(BaseModel):
    order_id: int
    amount: float
    currency: str
    payment_url: str

# 2. WebhookEvent Dataclass
#    - Unterschiedliche Provider haben unterschiedliche Event Namen
#      * Stripe: charge.succeeded
#      * Mollie: payment.paid
#    - Wie normalisiere ich diese auf ein Standard Format?
#    - Welche Status-Werte sind universal?

class StandardWebhookEvent(BaseModel):
    event_type: str  # z.B. "payment_succeeded", "payment_failed"
    payment_id: int
    amount: float
    currency: str
    raw_data: dict  # Rohdaten vom Provider

# 3. PaymentAdapter (ABC)
class PaymentAdapter(ABC):
#    - create_checkout_session()
#      * Input: allgemeine Payment-Daten (order_id, amount, currency, etc.)
#      * Output: PaymentSession mit payment_url
#      * Jeder Provider macht das anders!
    @abstractmethod 
    async def create_checkout_session(self, payment_data: dict) -> PaymentSession:
        pass

#    - verify_webhook_signature()
#      * Jeder Provider signiert anders (HMAC-SHA256, unterschiedliche Header)
#      * Aber das Interface sollte gleich bleiben
    @abstractmethod 
    async def verify_webhook_signature(self, payment_data: dict) -> PaymentSession:
        pass

#    - parse_webhook_event()
#      * Stripe sendet andere Event-Struktur als Mollie
#      * Muss auf StandardWebhookEvent normalisiert werden
    @abstractmethod 
    async def parse_webhook_event(self, raw_event: dict) -> StandardWebhookEvent:
        pass

#    - refund_payment()
#      * Jeder Provider hat unterschiedliche API
    @abstractmethod 
    async def refund_payment(self, payment_id: int, amount: float) -> bool:
        pass
#    - get_payment_status()
#      * Status-Namen unterscheiden sich — wie normalisieren?
    @abstractmethod 
    async def get_payment_status(self, payment_id: int) -> str:
        pass

# Error Handling: PaymentAdapterError sollte allgemein sein, nicht Provider-spezifisch

class PaymentAdapterError(Exception):
    pass


# DESIGN FRAGEN:

# - Sollte die Base auch ein AdapterFactory Pattern haben?
#   * Die Factory könnte den richtigen Adapter auswählen (Stripe oder Mollie)

# - Logging: Sollte die Base schon Logging haben oder erst die Implementierung?