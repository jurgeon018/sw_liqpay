from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _
from .settings import sw_liqpay_appname

class LiqpayConfig(AppConfig):
    name = sw_liqpay_appname
    verbose_name = _("Liqpay")
    verbose_name_plural = verbose_name

default_app_config = f'{sw_liqpay_appname}.LiqpayConfig'


