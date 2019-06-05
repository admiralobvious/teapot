import teapot


class HTTPAPI:
    def __init__(self, base_url="", headers=None, client_options=None, **kwargs):
        if not client_options:
            client_options = {}
        client_options["headers"] = headers

        self.client = teapot.HTTPClient(base_url, **client_options)
        self._attrs = kwargs
        self._resources = {}

    def _add_attributes(self, resource):
        for k, v in self._attrs.items():
            resource.__setattr__(k, v)

    def add_resource(self, resource, name=None):
        if name is None:
            name = resource.__class__.__name__

        if name in self._resources:
            raise NameError("Resource name '{}' already in-use".format(name))

        resource.__setattr__("client", self.client)
        self._add_attributes(resource)
        self.__setattr__(name, resource)
        self._resources[name] = resource

    def __getattr__(self, item):
        if item in self._resources.keys():
            return self._resources[item]
