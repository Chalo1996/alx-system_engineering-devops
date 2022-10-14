# Configuration Management(CM)
---
## CM tool: Puppet
---
### Installations: NB: use sudo if permissions required.
```
apt-get install -y ruby=1:2.7+1 --allow-downgrades
apt-get install -y ruby-augeas
apt-get install -y ruby-shadow
apt-get install -y puppet
gem install puppet-lint
```

### Confirm puppent-lint version
```
puppet-lint --version
```

### Usage: puppent-lint <puppet-file_name>
```
puppet-lint 0-create_a_file.pp
puppet apply 0-create_a_file.pp
```
