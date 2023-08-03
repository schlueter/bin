#!/bin/bash

API_URI="https://${OKTA_API_SUBDOMAIN}.okta.com/api/v1"
HEADERS=(
    --header 'Accept: application/json'
    --header 'Content-Type: application/json'
    --header "Authorization: SSWS $OKTA_API_KEY"
)

groups="$(curl -s "$API_URI/apps/$1/groups" "${HEADERS[@]}")"

while read -r id
do
    group_name="$(
        curl -s "$API_URI/groups/$id" "${HEADERS[@]}" \
        | jq -r '.profile.name'
    )"
    export group_name id
    <<<"$groups" jq -r '.[]|select(.id == env.id)|
        {"name": env.group_name,
         "id": .id,
         "samlRoles": .profile.samlRoles
        }'
done <<<"$(<<<"$groups" jq -r '.[]|.id')"
