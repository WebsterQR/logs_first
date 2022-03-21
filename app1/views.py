from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)

# Create your views here.
def main(request):
    logger.debug("logger1 - debug")
    logger.info("logger1 - info")
    logger.warning("logger1 - warning")
    logger.error("logger1 - error")
    return HttpResponse("<a href='#'>Click1</a>")