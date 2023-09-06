#!/bin/sh

# Decrypt the file
# mkdir $HOME/
# --batch to prevent interactive command
# --yes to assume "yes" for questions
# git update-index --chmod=+x src/bash/decrypt.sh 
gpg --quiet --batch --yes --decrypt --passphrase="$ENCRYPT_KEY" \
--output config/gcloud_service_account.json config/gcloud_service_account.json.gpg