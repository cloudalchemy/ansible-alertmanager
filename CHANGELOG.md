# Change Log

## [**Next release**](https://galaxy.ansible.com/cloudalchemy/alertmanager)

**Merged pull requests:**

- upgrade to molecule 2.x [\#37](https://github.com/cloudalchemy/ansible-alertmanager/pull/37) ([paulfantom](https://github.com/paulfantom))

## [0.11.6](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-04-21)
**Merged pull requests:**

- don't treat false, true, null as strings when templating smtp configuration [\#36](https://github.com/cloudalchemy/ansible-alertmanager/pull/36) ([walczakp](https://github.com/walczakp))

## [0.11.5](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-04-13)
**Merged pull requests:**

- Make template compatible with both Python 2 and 3 [\#35](https://github.com/cloudalchemy/ansible-alertmanager/pull/35) ([nikosgraser](https://github.com/nikosgraser))

## [0.11.4](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-04-07)
**Merged pull requests:**

- Quick fix to allow multi-arch environments support [\#34](https://github.com/cloudalchemy/ansible-alertmanager/pull/34) ([paulfantom](https://github.com/paulfantom))

## [0.11.3](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-04-06)
**Merged pull requests:**

- Fix success test done with a filter [\#33](https://github.com/cloudalchemy/ansible-alertmanager/pull/33) ([Porkepix](https://github.com/Porkepix))

## [0.11.2](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-04-06)
**Merged pull requests:**

- Fix version\_compare test done with a filter [\#32](https://github.com/cloudalchemy/ansible-alertmanager/pull/32) ([Porkepix](https://github.com/Porkepix))

## [0.11.1](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-04-05)
**Implemented enhancements:**

- Prevent misconfiguration [\#5](https://github.com/cloudalchemy/ansible-alertmanager/issues/5)

**Closed issues:**

- Unify variables naming [\#10](https://github.com/cloudalchemy/ansible-alertmanager/issues/10)

**Merged pull requests:**

- Retry when connecting to external services [\#31](https://github.com/cloudalchemy/ansible-alertmanager/pull/31) ([paulfantom](https://github.com/paulfantom))

## [0.11.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-03-30)
**Merged pull requests:**

- Major rework [\#30](https://github.com/cloudalchemy/ansible-alertmanager/pull/30) ([paulfantom](https://github.com/paulfantom))

## [0.10.4](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-03-27)
**Merged pull requests:**

- Fix default config [\#29](https://github.com/cloudalchemy/ansible-alertmanager/pull/29) ([paulfantom](https://github.com/paulfantom))

## [0.10.3](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-03-24)
**Merged pull requests:**

- ansible 2.5 [\#28](https://github.com/cloudalchemy/ansible-alertmanager/pull/28) ([paulfantom](https://github.com/paulfantom))

## [0.10.2](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-03-21)
**Merged pull requests:**

- Ubuntu bionic \(18.04\) support [\#27](https://github.com/cloudalchemy/ansible-alertmanager/pull/27) ([paulfantom](https://github.com/paulfantom))

## [0.10.1](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-03-21)
**Merged pull requests:**

- SELinux support [\#26](https://github.com/cloudalchemy/ansible-alertmanager/pull/26) ([paulfantom](https://github.com/paulfantom))

## [0.10.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-02-25)
**Fixed bugs:**

- Not able to configure a mesh [\#20](https://github.com/cloudalchemy/ansible-alertmanager/issues/20)

**Closed issues:**

- Use 0.14.0 as default [\#23](https://github.com/cloudalchemy/ansible-alertmanager/issues/23)

**Merged pull requests:**

- Locking testinfra version [\#25](https://github.com/cloudalchemy/ansible-alertmanager/pull/25) ([paulfantom](https://github.com/paulfantom))
- add support for HA [\#22](https://github.com/cloudalchemy/ansible-alertmanager/pull/22) ([paulfantom](https://github.com/paulfantom))

## [0.9.4](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-02-23)
**Merged pull requests:**

- Update default version [\#24](https://github.com/cloudalchemy/ansible-alertmanager/pull/24) ([SuperQ](https://github.com/SuperQ))

## [0.9.3](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-02-21)
**Merged pull requests:**

- Remove variable alertmanager\_log\_dir, as this has been removed in PR \#16 [\#21](https://github.com/cloudalchemy/ansible-alertmanager/pull/21) ([swesterveld](https://github.com/swesterveld))

## [0.9.2](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-02-14)
**Merged pull requests:**

- Make Prometheus alertmanager service restart/reload with sudo privileges [\#19](https://github.com/cloudalchemy/ansible-alertmanager/pull/19) ([swesterveld](https://github.com/swesterveld))
- \[ci skip\] readme and contribution guide; fixed tagging [\#11](https://github.com/cloudalchemy/ansible-alertmanager/pull/11) ([paulfantom](https://github.com/paulfantom))

## [0.9.1](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-01-27)
**Fixed bugs:**

- Not working with latest release of alertmanager \(0.13.0\) [\#17](https://github.com/cloudalchemy/ansible-alertmanager/issues/17)

## [0.9.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-01-26)
**Fixed bugs:**

- Do not create a directory for alertmanager logs [\#15](https://github.com/cloudalchemy/ansible-alertmanager/issues/15)

**Merged pull requests:**

- bump version to 0.13.0; support newer version in systemd [\#18](https://github.com/cloudalchemy/ansible-alertmanager/pull/18) ([paulfantom](https://github.com/paulfantom))

## [0.8.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-01-19)
**Merged pull requests:**

- removed log dir [\#16](https://github.com/cloudalchemy/ansible-alertmanager/pull/16) ([rdemachkovych](https://github.com/rdemachkovych))

## [0.7.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-01-13)
**Merged pull requests:**

- refactor tests [\#14](https://github.com/cloudalchemy/ansible-alertmanager/pull/14) ([paulfantom](https://github.com/paulfantom))
- support more OSes; use custom docker images [\#13](https://github.com/cloudalchemy/ansible-alertmanager/pull/13) ([paulfantom](https://github.com/paulfantom))

## [0.6.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-01-07)
**Merged pull requests:**

- added i386 arch [\#12](https://github.com/cloudalchemy/ansible-alertmanager/pull/12) ([rdemachkovych](https://github.com/rdemachkovych))

## [0.5.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-01-02)
**Merged pull requests:**

- Update generatetag.sh [\#9](https://github.com/cloudalchemy/ansible-alertmanager/pull/9) ([paulfantom](https://github.com/paulfantom))
- add system architecture autodetection [\#8](https://github.com/cloudalchemy/ansible-alertmanager/pull/8) ([paulfantom](https://github.com/paulfantom))

## [0.4.7](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-12-18)
**Merged pull requests:**

- Version bump [\#7](https://github.com/cloudalchemy/ansible-alertmanager/pull/7) ([paulfantom](https://github.com/paulfantom))

## [0.4.6](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-12-08)
**Merged pull requests:**

- Enable ability to change config file [\#6](https://github.com/cloudalchemy/ansible-alertmanager/pull/6) ([ecksun](https://github.com/ecksun))

## [0.4.5](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-12-06)
**Merged pull requests:**

- Stop pipeline on any error [\#4](https://github.com/cloudalchemy/ansible-alertmanager/pull/4) ([paulfantom](https://github.com/paulfantom))

## [0.4.4](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-11-30)
## [0.4.3](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-11-30)
## [0.4.2](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-11-29)
**Merged pull requests:**

- Added template. Update version to 0.11.0 [\#3](https://github.com/cloudalchemy/ansible-alertmanager/pull/3) ([rdemachkovych](https://github.com/rdemachkovych))
- parallel builds [\#2](https://github.com/cloudalchemy/ansible-alertmanager/pull/2) ([paulfantom](https://github.com/paulfantom))

## [0.4.1](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-11-13)
## [0.4.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-10-16)
## [0.3.1](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-10-05)
## [0.3.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-07-21)
## [0.2.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-07-21)
## [0.1.6](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-07-12)
## [0.1.5](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-07-12)
## [0.1.4](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-07-10)
## [0.1.3](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-07-10)
## [0.1.2](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-07-03)
## [0.1.1](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-06-14)
## [0.1.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-06-06)
## [0.0.4](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-05-15)
## [0.0.3](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-05-09)
## [0.0.2](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-05-05)
## [0.0.1](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2017-04-27)


\* *This Change Log was automatically generated by [github_changelog_generator](https://github.com/skywinder/Github-Changelog-Generator)*