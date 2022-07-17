# This module is automatically generated by autogen.sh. DO NOT EDIT.

from . import _OnPrem


class _Workflow(_OnPrem):
    _type = "workflow"
    _icon_dir = "resources/onprem/workflow"


class Airflow(_Workflow):
    _icon = "airflow.png"


class Digdag(_Workflow):
    _icon = "digdag.png"


class Kubeflow(_Workflow):
    _icon = "kubeflow.png"


class Nifi(_Workflow):
    _icon = "nifi.png"


# Aliases

KubeFlow = Kubeflow
NiFi = Nifi
