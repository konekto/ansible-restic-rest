import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_restic_systemd_service(host):
    cr = host.run('find /etc/systemd/system -type f -iname "rest-server*.service"')

    services = cr.stdout.splitlines()

    for service in services:
        s = host.service(os.path.basename(service))

        assert s.is_running



