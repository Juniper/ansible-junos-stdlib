PWD = $(shell pwd)
UNAME_S := $(shell uname -s)

ifeq ($(UNAME_S),Darwin)
	SED := sed -i ''
else
	SED := sed -i
endif

include Makefile.variable

all:prequisite virtual-env ansible-awx docker-start docker-exec ## install ansible-junos-awx

 
.PHONY: prequisite
prequisite:
	pip install virtualenv
	rm -rf ./awx ./awx-env        
	
.PHONY: virtual-env
virtual-env:
	virtualenv awx-env --no-site-packages
	. awx-env/bin/activate && \
	pip install ansible docker-py 

.PHONY: ansible-awx
ansible-awx:
	. awx-env/bin/activate && \
        git clone https://github.com/ansible/awx.git --single-branch --depth 1
	
.PHONY: docker-start 
docker-start:
ifneq '$(PROJECT_DATA_DIR)' ''
	mkdir -p $(PROJECT_DATA_DIR)
	@${SED} '/project_data_dir/s/^#//g' $(PWD)/awx/installer/inventory
	@${SED} 's|project_data_dir=.*|project_data_dir=$(PROJECT_DATA_DIR)|g' $(PWD)/awx/installer/inventory
endif
ifneq '$(AWX_TASK_TAG)' ''
	@${SED} 's/dockerhub_version=.*/dockerhub_version=$(AWX_TASK_TAG)/g' $(PWD)/awx/installer/inventory
endif
ifneq '$(POSTGRES_DATA_DIR)' ''
	@${SED} 's|postgres_data_dir=.*|postgres_data_dir=$(POSTGRES_DATA_DIR)|g' $(PWD)/awx/installer/inventory
	@mkdir -p ${POSTGRES_DATA_DIR}/pg_snapshots && touch ${POSTGRES_DATA_DIR}/pg_snapshots/.keep
	@mkdir -p ${POSTGRES_DATA_DIR}/pg_replslot && touch ${POSTGRES_DATA_DIR}/pg_replslot/.keep
	@mkdir -p ${POSTGRES_DATA_DIR}/pg_stat_tmp && touch ${POSTGRES_DATA_DIR}/pg_stat_tmp/.keep
	@mkdir -p ${POSTGRES_DATA_DIR}/pg_stat && touch ${POSTGRES_DATA_DIR}/pg_stat/.keep
	@mkdir -p ${POSTGRES_DATA_DIR}/pg_twophase && touch ${POSTGRES_DATA_DIR}/pg_twophase/.keep
	@mkdir -p ${POSTGRES_DATA_DIR}/pg_tblspc && touch ${POSTGRES_DATA_DIR}/pg_tblspc/.keep
endif
ifneq '$(HOST_FILE)' ''
	cp $(HOST_FILE) $(strip $(PROJECT_DATA_DIR))/hosts
endif

	. awx-env/bin/activate && \
	ansible-playbook -i $(PWD)/awx/installer/inventory $(PWD)/awx/installer/install.yml
	sleep 120

.PHONY: docker-exec
docker-exec:
	docker exec -it awx_task pip install jsnapy jxmlease junos-eznc
	docker exec -it awx_task ansible-galaxy install Juniper.junos,$(ANSIBLE_JUNOS_VERSION) -p  /etc/ansible/roles
	docker exec -it awx_task /bin/bash -c 'sed -i '/roles_path/s/^#//g' /etc/ansible/ansible.cfg'
ifneq '$(HOST_FILE)' ''	
	curl -u admin:password --noproxy '*' http://localhost/api/v2/inventories/ --header "Content-Type: application/json" -x POST -d '{"name":"$(INVENTORY_NAME)" , "organization": 1}'
	docker exec -it awx_task /bin/bash -c 'awx-manage inventory_import --source=/var/lib/awx/projects/hosts --inventory-name=$(INVENTORY_NAME) --overwrite'
endif

.PHONY: docker-stop
docker-stop: ## stop the docker
	docker stop awx_task 
	docker stop awx_web
	docker stop memcached
	docker stop rabbitmq
	docker stop postgres

.PHONY: docker-remove
docker-remove: docker-stop ##clean the docker
	docker rm awx_task
	docker rm awx_web
	docker rm memcached
	docker rm rabbitmq
	docker rm postgres

clean: prequisite  ## clean the project
	docker system prune -f
