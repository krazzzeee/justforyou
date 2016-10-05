"""
WSGI config for justForYou project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""


import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "justForYou.settings")

application = get_wsgi_application()




# import os
# import sys
# import site
#
# vepath = '/home/mjl/sports/iathlete_blackhawks_venv/lib/python2.7/site-packages'
#
# prev_sys_path = list(sys.path)
# # add the site-packages of our virtualenv as a site dir
# site.addsitedir(vepath)
# # add the app's directory to the PYTHONPATH
# #sys.path.append('/path/to/app/%s/' % ('stage' if STAGE else 'live')
# sys.path.append('/home/mjl/sports/iathlete_blackhawks_venv/iathlete_blackhawks/')
# sys.path.append('/home/mjl/sports/iathlete_blackhawks_venv/iathlete_blackhawks/iathlete_blackhawks/')
#
# # reorder sys.path so new directories from the addsitedir show up first
# new_sys_path = [p for p in sys.path if p not in prev_sys_path]
# for item in new_sys_path:
#     sys.path.remove(item)
# sys.path[:0] = new_sys_path
#
# os.environ.setdefault("DJANGO_SETTINGS_MODULE", "iathlete_blackhawks.settings")
#
# # This application object is used by any WSGI server configured to use this
# # file. This includes Django's development server, if the WSGI_APPLICATION
# # setting points here.
# from django.core.wsgi import get_wsgi_application
# application = get_wsgi_application()










