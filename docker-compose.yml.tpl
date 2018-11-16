#----------------------------------------------------------------------------
# This is used to do the deploy using docker-swarm
#----------------------------------------------------------------------------
# It will:
#    1) copy this file to the server after the replacements have been done
#    2) docker stack deploy -c docker-compose.yml --prune up
#    3) rm docker-compose.yml
##----------------------------------------------------------------------------

version: '3.2'

services:
   translate_api_nilportugues_com:
      image: ${DOCKER_IMAGE}:${GIT_BRANCH}
      ports: 
        - 80:80
#      labels:
#          traefik.enable: "true"
#          traefik.port: 80
#          traefik.docker.network: "up_traefik_default"
#          traefik.backend: "translate.api.nilportugues.com"
#          traefik.frontend.rule: "Host:translate.api.nilportugues.com"
#      networks:
#         shared_services:
#            aliases:
#              - translate.api.nilportugues.com
#         traefik_default:
#            aliases:
#              - translate.api.nilportugues.com


#networks:
#  shared_services:
#    external:
#      name: up_shared_services
#  traefik_default:
#    external:
#      name: up_traefik_default