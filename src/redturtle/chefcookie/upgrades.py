# -*- coding: utf-8 -*-
from plone import api
from redturtle.chefcookie.interfaces import IChefCookieSettings
from zope.component import getUtility
from plone.registry.interfaces import IRegistry

import json
import logging
<<<<<<< HEAD
import six
=======
from plone import api
from redturtle.chefcookie.interfaces import IChefCookieSettings
>>>>>>> main

logger = logging.getLogger(__name__)

DEFAULT_PROFILE = "profile-redturtle.chefcookie:default"


def update_profile(context, profile, run_dependencies=True):
    context.runImportStepFromProfile(DEFAULT_PROFILE, profile, run_dependencies)


def update_registry(context):
    update_profile(context, "plone.app.registry", run_dependencies=False)
    logger.info("Update registry")


def to_1100(context):
    registry = getUtility(IRegistry)
    analytics = registry[
        "redturtle.chefcookie.interfaces.IChefCookieSettings.analytics_cookies_labels"
    ]
    functional = registry[
        "redturtle.chefcookie.interfaces.IChefCookieSettings.functional_cookies_labels"
    ]

    analytics_id = registry[
        "redturtle.chefcookie.interfaces.IChefCookieSettings.analytics_id"
    ]

    new_conf = {
        "techcookies": json.loads(functional),
    }
    if analytics_id:
        new_conf["analytics"] = json.loads(analytics)

    if six.PY2:
        new_conf_json = json.dumps(new_conf, indent=4).decode("utf-8")
    else:
        new_conf_json = json.dumps(new_conf, indent=4)

    update_registry(context)

    api.portal.set_registry_record(
        "technical_cookies_specific_labels",
        new_conf_json,
        interface=IChefCookieSettings,
    )

    api.portal.set_registry_record("enable_cc", True, interface=IChefCookieSettings)
