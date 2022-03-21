from django.shortcuts import render
from django.http import HttpResponse
import logging

logger = logging.getLogger(__name__)
# Create your views here.
def main(request):
    logger.debug("logger2 - debug")
    logger.info("logger2 - info")
    logger.warning("logger2 - warning")
    logger.error("logger2 - error")
    return HttpResponse("<a href='#'>Click2</a>")