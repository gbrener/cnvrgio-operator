import unittest
import os
from common import CommonBase
from kubernetes import client, config
import logging

config.load_kube_config()

CNVRG_SPEC_ISTIO_ONLY = """
apiVersion: mlops.cnvrg.io/v1
kind: CnvrgApp
metadata:
  name: cnvrg-app
  namespace: cnvrg
spec:
  clusterDomain: "sample-domain"
  istio:
    enabled: "true"
  mpi:
    enabled: "false"
  conf:
    enabled: "false"
  conf:
    enabled: "false"
  cnvrgApp:
    enabled: "false"
  pgBackup:
    enabled: "false"
  redis:
    enabled: "false"
  es:
    enabled: "false"
  minio:
    enabled: "false"
  prometheus:
    enabled: "false"
  kibana:
    enabled: "false"
  fluentd:
    enabled: "false"
  nvidiadp:
    enabled: "false"
"""
CNVRG_SPEC_AKS_ISTIO_DEFAULT = """
apiVersion: mlops.cnvrg.io/v1
kind: CnvrgApp
metadata:
  name: cnvrg-app
  namespace: cnvrg
spec:
  clusterDomain: "__BASE_DOMAIN__"
  
"""


class SanityAksIstioTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls.deploy()
        cls.create_cnvrg_spec(CNVRG_SPEC_ISTIO_ONLY)
        cls.wait_for_cnvrg_spec_ready()
        ip = cls.get_nip_nip_url("istio")
        x = 1

    @classmethod
    def tearDownClass(cls):
        return
        cls.delete_cnvrg_spec()
        cls.undeploy()

    def test_app_ready_aks_istio(self):
        pass
        # cmd = "kubectl wait --for=condition=ready pod -l app=app -ncnvrg --timeout=120s"
        # res = self.exec_cmd(cmd)
        # self.assertEqual(0, res[0])
