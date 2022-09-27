#!/usr/bin/env bash

docker build -t mirrorclockserver .

docker tag mirrorclockserver ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPOSITORY}

docker login -u AWS -p $(aws ecr get-login-password --region ${REGION}) ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com

docker push ${AWS_ACCOUNT_ID}.dkr.ecr.${REGION}.amazonaws.com/${REPOSITORY}
