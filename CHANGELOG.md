# Change Log

## [0.17.2](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2020-04-24)
**Fixed bugs:**

- Fixed alertmanager\_http\_config setting failing deploy [\#122](https://github.com/cloudalchemy/ansible-alertmanager/pull/122) ([graudeejs](https://github.com/graudeejs))

## [0.17.1](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2020-03-29)
**Merged pull requests:**

- add deprecation warnings [\#120](https://github.com/cloudalchemy/ansible-alertmanager/pull/120) ([paulfantom](https://github.com/paulfantom))

## [0.17.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2020-03-29)
**Implemented enhancements:**

- Http config unable to set basic auth [\#115](https://github.com/cloudalchemy/ansible-alertmanager/issues/115)

**Fixed bugs:**

- binary checksum seems broken [\#117](https://github.com/cloudalchemy/ansible-alertmanager/issues/117)
- "No package policycoreutils-python available." [\#111](https://github.com/cloudalchemy/ansible-alertmanager/issues/111)

**Merged pull requests:**

- \[REPO SYNC\] lock molecule to v2 [\#118](https://github.com/cloudalchemy/ansible-alertmanager/pull/118) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Modify http\_config to handle basic auth [\#116](https://github.com/cloudalchemy/ansible-alertmanager/pull/116) ([mcsammac](https://github.com/mcsammac))
- Corrected typo on preflight check [\#114](https://github.com/cloudalchemy/ansible-alertmanager/pull/114) ([WilliamBriot](https://github.com/WilliamBriot))
- Flush handlers after configuration [\#113](https://github.com/cloudalchemy/ansible-alertmanager/pull/113) ([jstaffans](https://github.com/jstaffans))
- move installing selinux package dependencies into separate tasks [\#112](https://github.com/cloudalchemy/ansible-alertmanager/pull/112) ([wikro](https://github.com/wikro))
- \[REPO SYNC\] Merge pull request \#4 from cloudalchemy/travis\_fix [\#110](https://github.com/cloudalchemy/ansible-alertmanager/pull/110) ([cloudalchemybot](https://github.com/cloudalchemybot))
- \[REPO SYNC\] use latest available python [\#109](https://github.com/cloudalchemy/ansible-alertmanager/pull/109) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Remove alertmanager\_child\_routes [\#101](https://github.com/cloudalchemy/ansible-alertmanager/pull/101) ([paulfantom](https://github.com/paulfantom))

## [0.16.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2020-01-11)
**Implemented enhancements:**

- Having the choice to install the package or not [\#49](https://github.com/cloudalchemy/ansible-alertmanager/issues/49)

**Merged pull requests:**

- Switch user login shell to /usr/sbin/nologin [\#108](https://github.com/cloudalchemy/ansible-alertmanager/pull/108) ([paulfantom](https://github.com/paulfantom))
- \[REPO SYNC\] use latest available python [\#107](https://github.com/cloudalchemy/ansible-alertmanager/pull/107) ([cloudalchemybot](https://github.com/cloudalchemybot))
- \[REPO SYNC\] remove IRC link [\#105](https://github.com/cloudalchemy/ansible-alertmanager/pull/105) ([cloudalchemybot](https://github.com/cloudalchemybot))
- New prometheus/alertmanager upstream release! [\#104](https://github.com/cloudalchemy/ansible-alertmanager/pull/104) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Do not fail when using a custom config template file [\#103](https://github.com/cloudalchemy/ansible-alertmanager/pull/103) ([DaazKu](https://github.com/DaazKu))
- Add restart handler on configuration template change [\#102](https://github.com/cloudalchemy/ansible-alertmanager/pull/102) ([iwagner-inmar](https://github.com/iwagner-inmar))
- \[REPO SYNC\] add declarative label sync; add autolabelling PRs [\#97](https://github.com/cloudalchemy/ansible-alertmanager/pull/97) ([cloudalchemybot](https://github.com/cloudalchemybot))
- \[REPO SYNC\] molecule: use CI images from quay.io instead of dockerhub [\#95](https://github.com/cloudalchemy/ansible-alertmanager/pull/95) ([cloudalchemybot](https://github.com/cloudalchemybot))
- add option to propagate binaries without access to internet [\#83](https://github.com/cloudalchemy/ansible-alertmanager/pull/83) ([paulfantom](https://github.com/paulfantom))

## [0.15.1](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2019-11-11)
**Merged pull requests:**

- \[REPO SYNC\] Update releaser.sh [\#93](https://github.com/cloudalchemy/ansible-alertmanager/pull/93) ([cloudalchemybot](https://github.com/cloudalchemybot))
- \[REPO SYNC\] add support for CentOS8 [\#92](https://github.com/cloudalchemy/ansible-alertmanager/pull/92) ([cloudalchemybot](https://github.com/cloudalchemybot))
- make order of cluster args deterministic [\#91](https://github.com/cloudalchemy/ansible-alertmanager/pull/91) ([slomo](https://github.com/slomo))

## [0.15.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2019-10-02)
**Implemented enhancements:**

- Allow using `latest` as a version specifier [\#44](https://github.com/cloudalchemy/ansible-alertmanager/issues/44)

**Closed issues:**

- cluster setup broken in default [\#87](https://github.com/cloudalchemy/ansible-alertmanager/issues/87)
- systemd: Failed to start Alertmanager \(when Prometheus is not running yet\) [\#74](https://github.com/cloudalchemy/ansible-alertmanager/issues/74)

**Merged pull requests:**

- Adjust systemd restrictions [\#90](https://github.com/cloudalchemy/ansible-alertmanager/pull/90) ([corny](https://github.com/corny))
- New prometheus/alertmanager upstream release! [\#89](https://github.com/cloudalchemy/ansible-alertmanager/pull/89) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Cluster fix [\#88](https://github.com/cloudalchemy/ansible-alertmanager/pull/88) ([gajowi](https://github.com/gajowi))
- Synchronize files from cloudalchemy/skeleton [\#86](https://github.com/cloudalchemy/ansible-alertmanager/pull/86) ([cloudalchemybot](https://github.com/cloudalchemybot))
- add support for RHEL8 \(without automated testing\) [\#84](https://github.com/cloudalchemy/ansible-alertmanager/pull/84) ([paulfantom](https://github.com/paulfantom))
- drop testing on debian jessie and add support for debian buster [\#82](https://github.com/cloudalchemy/ansible-alertmanager/pull/82) ([paulfantom](https://github.com/paulfantom))
- update to fedora 30 and bring in mechanism for installing SELinux deps known from ansible-prometheus [\#81](https://github.com/cloudalchemy/ansible-alertmanager/pull/81) ([paulfantom](https://github.com/paulfantom))
- increase systemd service security restrictions [\#80](https://github.com/cloudalchemy/ansible-alertmanager/pull/80) ([paulfantom](https://github.com/paulfantom))
- propagate support for 'latest' version specifier from ansible-prometheus [\#79](https://github.com/cloudalchemy/ansible-alertmanager/pull/79) ([paulfantom](https://github.com/paulfantom))
- Update minimum required ansible version [\#78](https://github.com/cloudalchemy/ansible-alertmanager/pull/78) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Moving to python 3 and dropping support for python 2.x \(on deployer host\) [\#77](https://github.com/cloudalchemy/ansible-alertmanager/pull/77) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Synchronize files from cloudalchemy/skeleton [\#75](https://github.com/cloudalchemy/ansible-alertmanager/pull/75) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [0.14.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2019-07-11)
**Merged pull requests:**

- New prometheus/alertmanager upstream release! [\#73](https://github.com/cloudalchemy/ansible-alertmanager/pull/73) ([cloudalchemybot](https://github.com/cloudalchemybot))
- New prometheus/alertmanager upstream release! [\#69](https://github.com/cloudalchemy/ansible-alertmanager/pull/69) ([cloudalchemybot](https://github.com/cloudalchemybot))
- support copying of alertmanager templates [\#68](https://github.com/cloudalchemy/ansible-alertmanager/pull/68) ([mjbnz](https://github.com/mjbnz))

## [0.13.12](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2019-05-04)
**Merged pull requests:**

- Synchronize files from cloudalchemy/skeleton [\#71](https://github.com/cloudalchemy/ansible-alertmanager/pull/71) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Wait for network to be online [\#70](https://github.com/cloudalchemy/ansible-alertmanager/pull/70) ([paulfantom](https://github.com/paulfantom))
- added proxy support [\#67](https://github.com/cloudalchemy/ansible-alertmanager/pull/67) ([thirdeye-oleksandr](https://github.com/thirdeye-oleksandr))

## [0.13.11](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2019-04-05)
**Merged pull requests:**

- New prometheus/alertmanager upstream release! [\#66](https://github.com/cloudalchemy/ansible-alertmanager/pull/66) ([cloudalchemybot](https://github.com/cloudalchemybot))
- Change auth\_require\_tls to require\_tls [\#65](https://github.com/cloudalchemy/ansible-alertmanager/pull/65) ([lunarthegrey](https://github.com/lunarthegrey))

## [0.13.10](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2019-03-04)
**Merged pull requests:**

- changed 'result|success' to 'result is success' in install.yml file t… [\#64](https://github.com/cloudalchemy/ansible-alertmanager/pull/64) ([sardarhalip](https://github.com/sardarhalip))
- Download package locally during check mode [\#63](https://github.com/cloudalchemy/ansible-alertmanager/pull/63) ([etcet](https://github.com/etcet))
- New alertmanager upstream release and template improvements [\#62](https://github.com/cloudalchemy/ansible-alertmanager/pull/62) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [0.13.9](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2019-01-14)
**Fixed bugs:**

- Service command line flags set during `install` but not during `configure` [\#56](https://github.com/cloudalchemy/ansible-alertmanager/issues/56)

**Merged pull requests:**

- Fix faulty hipchat configuration parameters [\#61](https://github.com/cloudalchemy/ansible-alertmanager/pull/61) ([schewara](https://github.com/schewara))
- Fix typo in preflight checks for routes [\#59](https://github.com/cloudalchemy/ansible-alertmanager/pull/59) ([slomo](https://github.com/slomo))
- Add support for multi-line ansible\_managed strings [\#58](https://github.com/cloudalchemy/ansible-alertmanager/pull/58) ([etcet](https://github.com/etcet))

## [0.13.8](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-12-03)
**Merged pull requests:**

- Move service creation from install to configure [\#57](https://github.com/cloudalchemy/ansible-alertmanager/pull/57) ([mgrecar](https://github.com/mgrecar))

## [0.13.7](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-11-30)
**Merged pull requests:**

- New alertmanager upstream release! [\#55](https://github.com/cloudalchemy/ansible-alertmanager/pull/55) ([cloudalchemybot](https://github.com/cloudalchemybot))
- fix tags, remove always [\#54](https://github.com/cloudalchemy/ansible-alertmanager/pull/54) ([rlex](https://github.com/rlex))
- Fix: --cluster.nickname does not exist in 0.15.2 [\#53](https://github.com/cloudalchemy/ansible-alertmanager/pull/53) ([till](https://github.com/till))

## [0.13.6](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-10-23)
**Merged pull requests:**

- Update opsgenie global configs [\#52](https://github.com/cloudalchemy/ansible-alertmanager/pull/52) ([nikosmeds](https://github.com/nikosmeds))

## [0.13.5](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-10-08)
**Merged pull requests:**

- move to ansible 2.7 [\#51](https://github.com/cloudalchemy/ansible-alertmanager/pull/51) ([paulfantom](https://github.com/paulfantom))

## [0.13.4](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-09-06)
## [0.13.3](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-08-15)
**Merged pull requests:**

- New alertmanager upstream release! [\#48](https://github.com/cloudalchemy/ansible-alertmanager/pull/48) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [0.13.2](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-08-09)
## [0.13.1](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-07-26)
**Merged pull requests:**

- New alertmanager upstream release! [\#46](https://github.com/cloudalchemy/ansible-alertmanager/pull/46) ([cloudalchemybot](https://github.com/cloudalchemybot))

## [0.13.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-07-01)
**Merged pull requests:**

- use tox, ansible 2.6, and allow using remote docker host [\#45](https://github.com/cloudalchemy/ansible-alertmanager/pull/45) ([paulfantom](https://github.com/paulfantom))
- bump alertmanager version to 0.15.0 [\#43](https://github.com/cloudalchemy/ansible-alertmanager/pull/43) ([paulfantom](https://github.com/paulfantom))

## [0.12.0](https://galaxy.ansible.com/cloudalchemy/alertmanager) (2018-06-21)
**Fixed bugs:**

- fix architecture var parsing [\#39](https://github.com/cloudalchemy/ansible-alertmanager/pull/39) ([paulfantom](https://github.com/paulfantom))

**Merged pull requests:**

- add wechat configs vars [\#42](https://github.com/cloudalchemy/ansible-alertmanager/pull/42) ([soloradish](https://github.com/soloradish))
- add tags [\#41](https://github.com/cloudalchemy/ansible-alertmanager/pull/41) ([paulfantom](https://github.com/paulfantom))
- Fix failing role on non-SELinux RedHat [\#40](https://github.com/cloudalchemy/ansible-alertmanager/pull/40) ([noraab](https://github.com/noraab))
- Offer a better IRC Web clients to users [\#38](https://github.com/cloudalchemy/ansible-alertmanager/pull/38) ([Porkepix](https://github.com/Porkepix))
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