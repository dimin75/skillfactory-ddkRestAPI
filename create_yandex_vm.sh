yc compute instance create \
  --name virtual-django \
  --zone ru-central1-d \
  --network-interface subnet-name=ru-central1-d,nat-ip-version=ipv4 \
  --create-boot-disk image-folder-id=standard-images,image-family=ubuntu-2004-lts \
  --ssh-key ~/.ssh/id_ed25519.pub
  --service-account-name dimarestapi-acc
