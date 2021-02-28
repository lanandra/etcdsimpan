import datetime
from sudo import run_as_sudo

# set datetime
datenow = datetime.datetime.now()
datenow_formatted = datenow.strftime("%A, %d-%m-%Y %H:%M:%S %Z")

# sudo as root and run etcd backup
sudo_user = "root"
etcd_backup = "ETCDCTL_API=3 etcdctl --endpoints https://127.0.0.1:2379 snapshot save snapshot_k8s_ludes.db --cacert=/etc/kubernetes/pki/etcd/ca.crt --cert=/etc/kubernetes/pki/etcd/healthcheck-client.crt --key /etc/kubernetes/pki/etcd/healthcheck-client.key"
run_as_sudo(sudo_user, etcd_backup)

# inform backup has been done
print("Backup has been done at " + str(datenow_formatted))