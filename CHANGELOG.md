
## v12.0.5
- 115649c Merge pull request #7 from Stonie24/test/ansible
- 82164f6 type(fix): fix the test so it work , we cant assert with a value that isnt pushed yet
- df5939e type(fix):Update version check in integration test
- 2f90a57 type(fix): make test errors
- ff9b4e7 type(fix): Updated change log
- 7616311 type(fix): Remove dynamic inventory generation playbook
- 28a2985 type(fix): Update SSH paths and deployment configuration
- 7dff61a type(try): try3
- 8a7a73f TEST
- cb943c9 Merge remote-tracking branch 'origin/feature/ansible' into test/ansible get latest
- 25c338e Add dynamic inventory and version endpoint, update deployment
- 86181f8 Update Docker tags in CI/CD workflow
- 2af4b47 Modify CD workflow to use workflow_run trigger
- c9672db Remove Ansible deployment from CD workflow
- 7fd8e2f jag är för trött godnatt , (la till versionen igen så att vi automatiskt kan köra playbooken för micro blog)
- 314640f Refactor CI/CD workflow for Docker actions(im stupid)
- 1f1858b Update CI/CD workflow for Docker and add Ansible deployment
- d2b9397 Change playbook from deploy_app.yml to microblog.yml
- a690dcd Refactor GitHub Actions workflow for Python app
- d6c1a4b Add GitHub Actions workflow for Ansible deployment
- eb5d7f1 type(try): try2
- 3a4b9ec type(try): push to try that it works for both
- 5a1e3b7 type(fix): fix muliple sshkeys problem
- 6cbd7ba type(fix): change ssh key path
- cc1784e type(fix): change remote user to deply
- a1d9b14 type(fix): add sshkey files
- d44a481 type(feat): add github ssh key
- 930ecf6 type(feat): add github ssh-key
- 9172dfc type(fix): add password
- a88a73a git(fix): update to ubuntu latest
- d89cc53 type(feat): add hosts
- b549b02 type(feat): add hashed password
- b0e7f09 git(feat): add appserver1 and appserver2
- ae91077 type(fix): changed from .venv to venv
- eb9ab00 Merge branch 'master' into feature/ansible get latest
- 9925b27 type(fix): add ssh key
- 9936489 type(fix): add local variables
- 11140f0 Merge branch 'dbwebb-se:master' into master
- c986dcd ger kod för sätta upp LB i ansible. och fixat installera ansible deps
- 2760a7c Merge pull request #6 from Stonie24/dev
- 3380636 type(docs): add changelog
- bba5251 Merge branch 'master' into dev type(fix): fix file path in CD test
- e3bf547 Specify Dockerfile path for production build
- bfd0f14 Merge branch 'dev' of github.com:Stonie24/devops into dev Merge origin dev
- 63c7649 Merge pull request #5 from Stonie24/feature/followers
- d095d27 Merge branch 'master' into dev type(CI): get CI chian to dev
- 3916b2a Allow workflow on 'dev' branch in addition to 'master'
- c219236 type(fix): fix lint erors
- b0e7d24 type(fix): Fixed Dockerfile
- 9d4b798 type(fix): fix docker issues
- 2a5e03c type(fix): fixed Dockerfile_prod typo
- 80b83c4 type(feat): Add follow func to frontend
- 8e80a4b type(feat): Add follow routes
- ee20b5c type(test): add follow pytests
- 34c4fbd type(build): Migrate followers to database
- 1e76ee8 type(feature): add followers functionlity
- dbba691 Merge pull request #3 from Stonie24/build/docker
- 921ba18 Add Continuous Delivery workflow configuration
- 1eb5d31 Add workflow_call trigger to Python app workflow
- 52550db Merge pull request #2 from Stonie24/docs/badge
- 54b407c type(Build): Add test runner script for Docker environment
- ea09315 type(Build): Add Dockerfile for test environment
- 172d473 type(Build): Add production Dockerfile for Flask app
- fa0503a Delete dockerfile
- 1adc0d1 type(build) Add test service to docker-compose configuration
- 2f4c9b3 type(docs): add status badge to README
- 56f3d77 type(ci): Add GitHub Actions workflow for Python application
- 6104550 type(build): Add Dockerfile for Python Flask app
- 058e66b type(build): create dockercompose.yml
- 644ec12 Merge pull request #1 from Stonie24/chore/git-repo
- b296c03 type(chore): add commit-template for project
- ec33895 changed versions for ansible and azure
- 6aa87dc Remove root password setting from 1.update.sh
- 91b9089 bumbped azure deps to 3.0.0
- 692c4e5 fixes installing certbot with scripts. apt sources no longer needed
- 4e876d8 small fixes
- 79433d7 cleans up vars file from my info
- e9ce3ad Adds 10-first-minutes playbook
- 59a393a cleanes up new ansible code
- 3c8d6af New provisioning and terminate structure. More than halves execution time!
- a0d5172 Updates Ansible to new structure
- 372175c addes version for sqlalchemy
- 56a981b Removes deploy requirements from dev.txt
- a557c8d Sets python interpreter for devops hosts.
- ff7d399 added location of venv for local again. Dont know why it wasnt needed last week but now i need it....
- 6d6eebd prepared kmom03 for release
- 365fc93 fixed azure collections version
- 05309d6 added pylint folder from docker test to gitignore
- e6a1e3e Fixed py.test in makefile
- 7f81842 updated dependencies to validate and test code
- ceaf4b8 clarified
- 59ac634 added more about testing/debugging in ansible readme
- d370707 add all vms under host devops in ansible when gather facts
- 2026f12 rewrote deprectade functionality in ansible
- f94d309 changed to .venv
- de48182 ansible roles for azure now include azure collection
- e7a0cfc cleaned up ansible readme
- 6ec9507 removed tenant from readme, for azurecli. We dont need it with the new setup from IT
- f6bea78 bumbed ansible to 4.8.0 and install azure modules as galazy collection
- 7609d88 updated tests to work with new versions
- 3e51dbe upped versions to remove warnings in tests
- cf01eee validation
- 02fa6c5 spelling
- 4dc43ca disabled pylint rule for accessing imported attributes
- 494d8ab removed aws skript for kubernetes
- 505d599 added step to terminate to refresh hosts after
- 3785af2 added tenant var
- a1f7e9e commented out non working row
- 6149227 disable hadolint errors in docker fix
- d4c8ea4 fixed ssh key location variable
- a7e8409 removed line that destroys nginx script
- fca87f6 changed to camel case for hostsname
- 34d683a changed tmp var strucutre
- f0cc06c cleaned up renaming
- 14424e7 fixed comment
- 5cc649e reread of ansible README
- 1ef46e0 handle ansible[azure]
- 7621483 renaded ansible azure files
- d219fbd updated README with CircleCI more info
- 0ae3d55 changed ansible-vault information
- 4012581 updated README file
- f72bc92 changed ansible version
- e5d53dd update ansible to support azure
- 6fb6c55 Merge pull request #5 from pereriksson/python-dotenv-version
- 361d7f6 probably a typo in python-dotenv version
- f7bb355 added make command validate-ci
- cd7c867 added filer to docker validation
- 2c6e97e clarified text in readme
- 66c70e6 added Make command to validate Dockerfile
- e556a2e locked flask dependencies versions
- f3a3c72 fixed integration test for new version
- 4698834 Fixed validation
- b930dcb updated scripts for azure
- fa8fe20 added to remove deault nginx site in scripts
- 7b7f735 kmom01 changes for azure
- 7ea109c added better explanation
- 28294d2 chmods log folder
- cb5b29b new dep for email_validation in forms
- a9b3f21 more explanation to readme
- add392f env exporter for kubernetes tools
- 11cb286 removed . from venv
- d6be409 removed aws keys from task
- aef96d7 fixed makefile target add-ssh
- 3b8b5aa added explenation of docker gcc solution
- 5781b4a changed from aws_keys.yml to env variables
- e9f682a add-ssh target
- 8ee8a81 removed need for elastic ip
- 6d5e604 added bash to insert script instructions
- 4a95324 fixed warning
- 1d9d9b0 sets name on aws dashboard correctly
- 7f2e9e2 Name column on aws added
- 7f9b335 added venv to docker error
- d7b72f2 added mac support inster script
- 851d1e5 how to fixe cygwin gcc error
- 82307f3 fixed script where \n crashed ssh
- bf04abb more ansible fixes for kmom03
- 05b2d98 cleaned up ansible for kmom03
- f58796d added docker folder and readme
- 72e790e added comment on how to debug var from console
- 044b2af added section to readme about production
- 51d4745 added gunicorn logging for app
- b627a6a not running in dev as default
- 149abef correct gitter badge link
- 78cbfe2 renamed scripts file for new repo
- b66af34 fixed readme file name
- c0658cb added ansible site.yml file
- fe9c5ff added readme for group_vars
- 8fbedc1 added domain_name to group_vars
- 9465263 fixed path to python3 venv
- 2794db0 aws key script fixed
- 130af71 removed comments
- 2f2ff00 rearranged termination
- 411e07f indentation
- f7be287 add ssh key to ssh agent
- 409adb2 Removed hosts from gitignore
- cc7a0c7 fixed scripts
- d4e71a0 updated scripts for new repo
- b75d028 Initial commit. Check rest of the files

## v12.0.6


## v12.0.7
- 057e2af update workflow

## v12.0.8
- a9402cb Merge remote-tracking branch 'origin/master' get latest
- eef25c6 Update Docker login action to specific commit version

## v12.0.9
- 759d2de type(fix) fixed were old docker was still used and version
- 1ded82c Force install azure.azcollection in CI workflow
- 7a9dc4a Simplify dependency installation in CI workflow
- 09902f6 Update dependency installation steps in workflow
- b3bbd3f Remove pip caching from CD workflow
- da74f2b Update Microblog image name in Ansible tasks
- 1f4ef08 Set fail-on-cache-miss to false in Ansible workflow

## v12.0.10
- e2c6960 type(fix): version

## v12.0.11
- 96cec48 Merge branch 'master' of https://github.com/Stonie24/devops
- 21d603c om inte detta funkar hoppar jag av skolan

## v12.0.12
- 0533c8f type(test): test
- 6e646ce okej skoja förut men nu är jag seriös
- 06086e1 type(fix): version

## v12.0.13
- 5d5baed Update microblog deployment version checks and image

## v12.0.14


## v12.0.15
- 2d2d6f2 test
- 41e37f5 fix(type)

## v12.0.16
- 6c235a9 type(type):test

## v12.0.17
- 6d30c50 Update README.md

## v12.0.18
- 045a634 try

## v12.0.19
- b0c817a Update cd_ansible.yml
- 7f597a9 type(test)
- 6d30c50 Update README.md
- 6c235a9 type(type):test
- 2d2d6f2 test
- 41e37f5 fix(type)
- 5d5baed Update microblog deployment version checks and image
- 0533c8f type(test): test
- 6e646ce okej skoja förut men nu är jag seriös
- 06086e1 type(fix): version
- 96cec48 Merge branch 'master' of https://github.com/Stonie24/devops
- e2c6960 type(fix): version
- 21d603c om inte detta funkar hoppar jag av skolan

## v12.0.20
- 9bc995e Update cd_ansible.yml

## v12.0.21
- c8adf71 Update cd_ansible.yml

## v12.0.22
- 728829c Update Python version and ansible playbook order
- 7652b17 Merge branch 'dbwebb-se:master' into master
- 2c5e987 set ansible versions

## v12.0.23
- 0dd8fe8 TEST

## v12.0.24
- 0c0e43e Merge branch 'master' of https://github.com/Stonie24/devops
- f7ad333 Update python-app.yml

## v12.0.25
- cbbb89e Update cd_ansible.yml

## v12.0.26
- 181b290 Update cd_ansible.yml

## v12.0.27
- 20ac92a Update cd_ansible.yml

## v12.0.28
- ce798b1 test
- 9a1315e latest
- e1d449b try

## v12.0.29
- 4207a43 type(fix): change python path

## v12.0.30
- 0ddafe0 tet

## v12.0.31
- 1cad5ba type(fix): fix ansible
- aa1eac5 remove --staging
- 79e9982 Co-authored-by: Stonie24 <Stonie24@users.noreply.github.com>
- 3016b5c Remove comments
- 348c250 Update Ansible hosts file
- 197107f debug
- 2d9013a debug
- 14d4020 Simplify Ansible playbook execution step
- 7255182 Add debug step to CI workflow
- 057e975 Update ansible-playbook command with inventory file

## v12.0.32
- b2bd855 type(fix): fix hostname
- 42f7eea type(fix): change python path