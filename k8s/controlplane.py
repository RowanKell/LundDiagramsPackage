# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _K8S


class _Controlplane(_K8S):
    _type = "controlplane"
    _icon_dir = "resources/k8s/controlplane"


class API(_Controlplane):
    _icon = "api.png"


class CCM(_Controlplane):
    _icon = "c-c-m.png"


class CM(_Controlplane):
    _icon = "c-m.png"


class KProxy(_Controlplane):
    _icon = "k-proxy.png"


class Kubelet(_Controlplane):
    _icon = "kubelet.png"


class Sched(_Controlplane):
    _icon = "sched.png"


# Aliases

APIServer = API
ControllerManager = CM
KubeProxy = KProxy
Scheduler = Sched
