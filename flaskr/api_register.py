import pkgutil

from flaskr.app import api, app


def _list_modules(path):
    modules = pkgutil.iter_modules(path=[path])
    mode_names = []
    for _, mod_name, __ in modules:
        mode_names.append(str.replace(path, '/', '.') + '.' + mod_name)
    return mode_names


def _rollout_api(module_path, source=''):
    module = __import__(module_path, fromlist=[source])
    ns = getattr(module, 'ns')
    if ns:
        api.add_namespace(ns, path='/')
        app.logger.info("rolling out API - [{}]".format(ns.name))
    return ns


def register(api_dir):
    for mp in _list_modules(api_dir):
        _rollout_api(mp, source=str.replace(api_dir, '/', '.'))
